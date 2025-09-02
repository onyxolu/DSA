# Stage 1, normalize the log

# Goal
# Turn each record into a pair that says whether the store was open, and whether customers were present.

# Function
# parse_record(s: str) -> tuple[bool, bool] | { "error": str }

# Rules

# Accept tokens for open or closed, for example open or closed, 1 or 0

# Accept tokens for customers, for example yes or no, 1 or 0

# Case insensitive, extra spaces allowed

# Reject a record that does not contain both fields, return an error

# Examples

# "open yes" becomes (True, True)

# "closed 0" becomes (False, False)

# "Open\tNo" becomes (True, False)

# "maybe yes" returns an error

# Stage 2, score one log

# Goal
# Given a sequence of (is_open, has_customer) pairs, compute the penalty.
# Add one when the store was open and there were no customers.
# Add one when the store was closed and customers were present.

# Function
# store_penalty_given_open_close(pairs: list[tuple[bool, bool]]) -> int

# Examples

# [(True, True), (True, False), (False, True), (False, False)] returns 2

# All open with customers returns 0

# All closed with no customers returns 0

# Constraints

# Linear time

# Constant extra space

# Stage 3, clean a noisy log then score it

# Goal
# Accept a raw line that may contain junk, pull out the two fields per time slot, normalize them, build the pairs list, then compute the penalty.

# Function
# score_log_line(raw: str) -> int | { "error": str }

# Cleaning rules

# Tokens may be separated by any whitespace

# Accept common synonyms for open or closed, and for yes or no

# Skip unknown tokens until both fields for a slot are found

# If the line ends with an incomplete slot, drop that slot

# If no valid slots remain, return an error

# Examples

# "open yes open no closed yes closed no" returns 2

# "OPEN y xyz CLOSED n maybe" returns 0

# "garbage only" returns an error

# Stage 4, API shape and tests

# Goal
# Process many logs, keep input order, return one result per line with stable error reporting.

# Function
# analyze_store_logs(lines: list[str]) -> list[dict]

# Result per line

# Success, { "log_index": i, "penalty": int }

# Failure, { "log_index": i, "error": "no usable entries" }

# ========== Stage 1, normalize one record ==========

def parse_record(s: str):
    """
    Normalize a single record into (is_open, has_customer).
    Accepts:
      open field: open, closed, 1, 0, true, false, t, f, o, c
      customers field: yes, no, 1, 0, true, false, y, n, t, f
    Case insensitive, extra spaces allowed.
    Returns a tuple on success or {"error": "..."} on failure.
    """
    tokens = s.split()
    if len(tokens) != 2:
        return {"error": "invalid or incomplete record"}

    open_tok, cust_tok = tokens[0].lower(), tokens[1].lower()

    open_true = {"open", "1", "true", "t", "o"}
    open_false = {"closed", "0", "false", "f", "c"}

    cust_true = {"yes", "1", "true", "t", "y"}
    cust_false = {"no", "0", "false", "f", "n"}

    if open_tok in open_true:
        is_open = True
    elif open_tok in open_false:
        is_open = False
    else:
        return {"error": "invalid or incomplete record"}

    if cust_tok in cust_true:
        has_customer = True
    elif cust_tok in cust_false:
        has_customer = False
    else:
        return {"error": "invalid or incomplete record"}

    return (is_open, has_customer)


# ========== Stage 2, score one log given parsed pairs ==========

def store_penalty_given_open_close(pairs: list[tuple[bool, bool]]) -> int:
    """
    Add one when open with no customers.
    Add one when closed with customers.
    """
    pen = 0
    for is_open, has_cust in pairs:
        if is_open and not has_cust:
            pen += 1
        if not is_open and has_cust:
            pen += 1
    return pen


# ========== Stage 3, clean a noisy line then score it ==========

def score_log_line(raw: str):
    """
    Read tokens, build slots of two fields, then score.
    Order is open field first, then customers field.
    Skip junk tokens until both are found.
    Drop a trailing partial slot.
    Return int penalty or {"error": "..."} if no usable slots.
    """
    if not raw or not raw.strip():
        return {"error": "no usable entries"}

    open_true = {"open", "1", "true", "t", "o"}
    open_false = {"closed", "0", "false", "f", "c"}
    cust_true = {"yes", "1", "true", "t", "y"}
    cust_false = {"no", "0", "false", "f", "n"}

    slots: list[tuple[bool, bool]] = []
    have_open = None  # None until set to True or False

    for tok in raw.split():
        low = tok.lower()
        if have_open is None:
            if low in open_true:
                have_open = True
            elif low in open_false:
                have_open = False
            else:
                continue
        else:
            if low in cust_true:
                slots.append((have_open, True))
                have_open = None
            elif low in cust_false:
                slots.append((have_open, False))
                have_open = None
            else:
                continue

    if not slots:
        return {"error": "no usable entries"}

    return store_penalty_given_open_close(slots)


# ========== Stage 4, API for many logs ==========

def analyze_store_logs(lines: list[str]) -> list[dict]:
    """
    Process many lines, keep input order.
    On success, return {'log_index': i, 'penalty': int}.
    On failure, return {'log_index': i, 'error': 'no usable entries'}.
    """
    out: list[dict] = []
    for i, line in enumerate(lines):
        res = score_log_line(line)
        if isinstance(res, int):
            out.append({"log_index": i, "penalty": res})
        else:
            out.append({"log_index": i, "error": res.get("error", "no usable entries")})
    return out



# ========== Prints ==========

# Stage 1
print(parse_record("open yes"), "expected (True, True)")
print(parse_record("closed 0"), "expected (False, False)")
print(parse_record("Open    No"), "expected (True, False)")
print(parse_record("OPEN 1"), "expected (True, True)")
print(parse_record("CLOSED y"), "expected (False, True)")
print(parse_record("1 0"), "expected (True, False)")
print(parse_record("maybe yes"), "expected {'error': 'invalid or incomplete record'}")
print(parse_record("open"), "expected {'error': 'invalid or incomplete record'}")

# Stage 2
pairs = [(True, True), (True, False), (False, True), (False, False)]
print("penalty mixed:", store_penalty_given_open_close(pairs), "expected 2")
print("penalty all good:", store_penalty_given_open_close([(True, True)] * 3), "expected 0")
print("penalty all closed empty:", store_penalty_given_open_close([(False, False)] * 3), "expected 0")

# Stage 3
print("score clean line:",
      score_log_line("open yes open no closed yes closed no"),
      "expected 2")

print("score with junk and tabs:",
      score_log_line("OPEN\ty   xyz   CLOSED   n maybe"),
      "expected 0")

print("score partial trailing slot dropped:",
      score_log_line("open yes open"),
      "expected 1")

print("score junk only:",
      score_log_line("garbage only"),
      "expected {'error': 'no usable entries'}")

print("score empty:",
      score_log_line(""),
      "expected {'error': 'no usable entries'}")

# Stage 4
lines = [
    "Y N Y Y 0 0",            # this is for Q3 style, not for this parser
    "open yes open no closed no",
    "OPEN y junk CLOSED n maybe",
    "garbage only"
]
print("analyze many:",
      analyze_store_logs(lines),
      "expected [{'log_index': 0, 'error': 'no usable entries'}, {'log_index': 1, 'penalty': 1}, {'log_index': 2, 'penalty': 0}, {'log_index': 3, 'error': 'no usable entries'}]")
