# Merchants export sales events in a flat file. The file is tidy on a good day, messy on others. Columns show up in a fixed order most of the time, but sometimes there is whitespace, missing values, or unexpected casing. Your task is to turn this into numbers the finance team can trust. Think totals first, then slices by region or product, then rules that adjust numbers when certain conditions apply. Keep your code readable, write small checks as you go, talk through edge cases.

# Let us stage the work in steps.

# Step 1
# Parse rows that look like this, keep order, ignore completely empty rows.
# product_id,quantity,price,region,date
# p1,2,10.00,EU,2025-01-01
# p2,1,5.50,US,2025-01-01
# p1,3,10.00,EU,2025-01-02
# p3,4,7.25,APAC,2025-01-02
# Trim spaces. Coerce quantity to int, price to float. Skip rows missing product_id or where quantity or price cannot be parsed.

# Step 2
# Compute basic metrics from parsed rows.
# Total revenue, sum of quantity * price
# Totals by region
# Totals by product
# Preserve a stable order for output, for example insertion order of first appearance.

# Step 3
# Apply constraints and adjustments. Examples you may face in practice.
# Filter by a date range, start inclusive, end inclusive
# Exclude a region on request, for example internal test regions
# Apply a bulk discount rule when quantity for a single row exceeds a threshold, for example 5 or more units in one line item gets 10 percent off that line’s extended price; choose and state a clear rule
# Support currency hints if present, for example a currency column; if not present assume a default

# Step 4
# Produce a short report object that callers can consume without more parsing. Include:
# summary, with total revenue across all included rows
# by_region, map of region to revenue
# by_product, map of product to revenue and quantity
# filters_applied, list of any filters or rules that changed results
# If nothing matched the filters, return a clear error object rather than raising.

raw_sales = """product_id,quantity,price,region,date
p1,2,10.00,EU,2025-01-01
p2,1,5.50,US,2025-01-01
p1,3,10.00,EU,2025-01-02
p3,4,7.25,APAC,2025-01-02
p2,5,5.00,US,2025-01-03
pX,,12.00,EU,2025-01-03
p4,6,8.00, EU ,2025-01-04
 ,2,9.99,EU,2025-01-05
p5,three,11.00,US,2025-01-06
p6,1,abc,US,2025-01-07"""

from datetime import datetime
from typing import Optional

class Products:
    def __init__(self, raw_data: str):
        self.products = self._parse(raw_data)

    def set_products(self, products: list[dict]) -> None:
        self.products = products

    def _squash_ws(self, s: str) -> str:
        return "".join(s.split())

    def _format_date(self, date_string: str) -> datetime:
        return datetime.strptime(date_string, "%Y-%m-%d")

    def _parse(self, raw_data: str) -> list[dict]:
        lines = raw_data.splitlines()[1:]  # skip header
        products: list[dict] = []

        for row in lines:
            if not row.strip():
                continue
            parts = [self._squash_ws(p) for p in row.split(",")]
            if len(parts) != 5:
                continue

            product_id, quantity_str, price_str, region, date_str = parts
            if not product_id:
                continue

            try:
                quantity = int(quantity_str)
                price = float(price_str)
            except ValueError:
                continue

            # policy: skip zero or negative quantity or price
            if quantity <= 0 or price <= 0:
                continue

            products.append({
                "product_id": product_id,
                "quantity": quantity,
                "price": price,
                "region": region,
                "date": self._format_date(date_str)
            })

        return products

    # ---------- filtering ----------

    def get_products_by_date_range_and_excluded_region(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        exclude_regions: Optional[list[str]] = None
    ) -> list[dict]:
        start_dt = self._format_date(start_date) if start_date else None
        end_dt = self._format_date(end_date) if end_date else None
        banned = set(exclude_regions or [])
        out: list[dict] = []

        for p in self.products:
            if start_dt and p["date"] < start_dt:
                continue
            if end_dt and p["date"] > end_dt:
                continue
            if p["region"] in banned:
                continue
            out.append(p)

        return out

    # ---------- helpers for aggregation ----------

    def _line_revenue(self, item: dict, apply_bulk_discount: bool) -> float:
        rev = item["price"] * item["quantity"]
        if apply_bulk_discount and item["quantity"] >= 5:
            rev -= rev * 0.10
        return rev

    # ---------- aggregations (pure, accept optional rows) ----------

    def get_total_revenue(
        self,
        apply_bulk_discount: bool = False,
        rows: Optional[list[dict]] = None
    ) -> float:
        items = rows if rows is not None else self.products
        total = 0.0
        for p in items:
            total += self._line_revenue(p, apply_bulk_discount)
        return round(total, 2)

    def get_revenue_by_region(
        self,
        apply_bulk_discount: bool = False,
        rows: Optional[list[dict]] = None
    ) -> dict[str, float]:
        items = rows if rows is not None else self.products
        out: dict[str, float] = {}
        for p in items:
            line = self._line_revenue(p, apply_bulk_discount)
            out[p["region"]] = out.get(p["region"], 0.0) + line
        # round for display
        return {region: round(amount, 2) for region, amount in out.items()}

    def get_revenue_and_quantity_by_product(
        self,
        apply_bulk_discount: bool = False,
        rows: Optional[list[dict]] = None
    ) -> dict[str, dict[str, float | int]]:
        items = rows if rows is not None else self.products
        out: dict[str, dict[str, float | int]] = {}
        for p in items:
            pid = p["product_id"]
            line = self._line_revenue(p, apply_bulk_discount)
            if pid not in out:
                out[pid] = {"revenue": 0.0, "quantity": 0}
            out[pid]["revenue"] += line
            out[pid]["quantity"] += p["quantity"]
        # round revenue for display
        for pid in out:
            out[pid]["revenue"] = round(out[pid]["revenue"], 2)
        return out

    # ---------- report ----------

    def get_report(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        exclude_regions: Optional[list[str]] = None,
        apply_bulk_discount: bool = True
    ) -> dict:
        rows = self.get_products_by_date_range_and_excluded_region(
            start_date=start_date,
            end_date=end_date,
            exclude_regions=exclude_regions
        )

        filters_applied: list[str] = []
        if start_date or end_date:
            s = start_date if start_date else "-inf"
            e = end_date if end_date else "+inf"
            filters_applied.append(f"date: {s}..{e}")
        if exclude_regions:
            filters_applied.append(f"exclude_regions: {exclude_regions}")
        if apply_bulk_discount:
            filters_applied.append("bulk_discount_qty>=5 at 10% off per row")

        report =  {
            "total_revenue": self.get_total_revenue(apply_bulk_discount, rows),
            "revenue_by_region": self.get_revenue_by_region(apply_bulk_discount, rows),
            "revenue_and_quantity_by_product": self.get_revenue_and_quantity_by_product(apply_bulk_discount, rows),
            "filters_applied": filters_applied
        }
        return report


# =========================
# Print style tests for Steps 1 to 4
# =========================

print("\n--- Step 1: parsing ---")
product1 = Products(raw_sales)
parsed_rows = product1.products
expected_rows_count = 6  # rows that pass validation
print("parsed rows count matches:", len(parsed_rows) == expected_rows_count)
print("first row sample ok:", parsed_rows[0] == {
    "product_id": "p1",
    "quantity": 2,
    "price": 10.0,
    "region": "EU",
    "date": datetime.strptime("2025-01-01", "%Y-%m-%d")
})

print("\n--- Step 2: totals and slices without filters ---")
# with bulk discount: quantity 5 or more gets ten percent off that line
total_with_discount = product1.get_total_revenue(apply_bulk_discount=True)
print("total revenue with discount:", total_with_discount == 150.2, total_with_discount)

by_region_with_discount = product1.get_revenue_by_region(apply_bulk_discount=True)
print("revenue by region with discount:", by_region_with_discount == {"EU": 93.2, "US": 28.0, "APAC": 29.0}, by_region_with_discount)

by_product_with_discount = product1.get_revenue_and_quantity_by_product(apply_bulk_discount=True)
print("revenue and quantity by product with discount:", by_product_with_discount == {
    "p1": {"revenue": 50.0, "quantity": 5},
    "p2": {"revenue": 28.0, "quantity": 6},
    "p3": {"revenue": 29.0, "quantity": 4},
    "p4": {"revenue": 43.2, "quantity": 6},
}, by_product_with_discount)

print("\n--- Step 3: filters and adjustments ---")
# date range inclusive, exclude EU, keep discount on
start_date="2025-01-01"
end_date="2025-01-03"
exclude_regions=["EU"]
subset = product1.get_products_by_date_range_and_excluded_region(start_date, end_date, exclude_regions)
print("filtered row count:", len(subset) == 3)

total_subset = product1.get_total_revenue(apply_bulk_discount=True, rows=subset)
print("total revenue on filtered subset:", total_subset == 57.0, total_subset)

by_region_subset = product1.get_revenue_by_region(apply_bulk_discount=True, rows=subset)
print("region totals on filtered subset:", by_region_subset == {"US": 28.0, "APAC": 29.0}, by_region_subset)

by_product_subset = product1.get_revenue_and_quantity_by_product(apply_bulk_discount=True, rows=subset)
print("product totals on filtered subset:", by_product_subset == {
    "p2": {"revenue": 28.0, "quantity": 6},
    "p3": {"revenue": 29.0, "quantity": 4},
}, by_product_subset)

print("\n--- Step 4: report object ---")
report = product1.get_report(
    start_date=start_date,
    end_date=end_date,
    exclude_regions=exclude_regions,
    apply_bulk_discount=True
)
expected_report = {
    "total_revenue": 57.0,
    "revenue_by_region": {"US": 28.0, "APAC": 29.0},
    "revenue_and_quantity_by_product": {
        "p2": {"revenue": 28.0, "quantity": 6},
        "p3": {"revenue": 29.0, "quantity": 4},
    },
    "filters_applied": [
        "date: 2025-01-01..2025-01-03",
        "exclude_regions: ['EU']",
        "bulk_discount_qty>=5 at 10% off per row"
    ]
}
print("report matches expected:", report == expected_report, report)
