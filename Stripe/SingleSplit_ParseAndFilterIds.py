
# Sometimes we receive a single field that is meant to contain a handful of identifiers. Partners intend it to be comma separated, but what shows up can vary. Extra spaces slip in, empty positions appear, and a few entries look like they were half typed. We still need to turn that into something our internal tools can use.

# Internally we track which identifiers are actually recognized. Exact matches are preferred, yet there are cases where an incoming token is only the start of something we know. For example, a short form like t2 may line up with one or more records that begin with that text. We want to reflect that relationship without guessing beyond what the data supports.

# Downstream consumers expect a result that is easy to act on. Not just a bag of strings, but a small summary that tells them what was good, what was not, and where partial alignment occurred.

# Now let us stage the work in steps.

# Step 1
# Take the raw string and turn it into a clean list. Trim whitespace, ignore blanks, keep the original order.

# Step 2
# Compare that list to a provided set of recognized identifiers, return only the ones that are recognized, keep the same order.

# Step 3
# For each input token, find any recognized identifiers that begin with that token. Report all such pairs.

# Step 4
# Produce a structured summary per input token, with one of three outcomes: valid, invalid, or prefix of something valid, plus any matched targets where relevant.


class Transactions:
    def __init__(self, raw_data):
        self.transactions = self._parse(raw_data)
        
    def _parse(self, raw_data):
        splitted_token = raw_data.split(",")
        stripped_token = [trans.strip() for trans in splitted_token if trans.strip()]
        return stripped_token
        
    def validate_id(self, valid_ids):
        valid_ids_set = set(valid_ids)
        valid_transactions= [t for t in self.transactions if t in valid_ids_set]
        return valid_transactions
        
    def check_prefix(self, valid_ids):
        prefixes = []
        for trans in self.transactions:
            for valid_id in valid_ids:
                if valid_id.startswith(trans):
                    prefixes.append((trans, valid_id))
        return prefixes
        
    def summarize(self, valid_ids):
        valid_ids_set = set(valid_ids)
        trans_summary = []
        for trans in self.transactions:
            trans_map = {
                "token": trans
            }
            if trans in valid_ids_set:
                trans_map["status"] = "valid"
                trans_summary.append(trans_map)
                continue
            
            prefixes = [id for id in valid_ids if id.startswith(trans)]
            if prefixes:
                trans_map["status"] = "prefix"
                trans_map["matches"] = prefixes
            else:
                trans_map["status"] = "invalid"
                
            trans_summary.append(trans_map)
        return trans_summary
   
     
# ---------- Step 1 tests: _parse ----------  
t11 = Transactions("t1, t2, x3,,  x4 ")
print(t11.transactions)

t12 = Transactions("  ")
print(t12.transactions)

t13 = Transactions("t7")
print(t13.transactions)

t14 = Transactions("t 1, t2")
print(t14.transactions)

t15 = Transactions("t1,\nt2, t3")
print(t15.transactions)


# ---------- Step 2 tests: _parse ----------
t21 = Transactions("t1,t2,x3,,t4, t2")
print(t21.validate_id(["t1","t2","t4"]))

t22 = Transactions("")
print(t22.validate_id(["t1"]))

t23 = Transactions("T1,t1")
print(t23.validate_id(["t1"]))


# ---------- Step 3 tests: _parse ----------
t31 = Transactions("t1, t2, x3, t4, t2, a")
print(t31.check_prefix(["t1", "t22", "abc"]))

t32 = Transactions("x, y")
print(t32.check_prefix(["t1, t2"]))

t33 = Transactions("t2, t2")
print(t33.check_prefix(["t21", "t22"]))


# ---------- Step 4 tests: _parse ----------   
t41 = Transactions("t1, t2, x3, t4, t2, a")
print(t41.summarize(["t1", "t22", "abc"]))

t42 = Transactions("")
print(t42.summarize(["t1"]))

t43 = Transactions("t1")
print(t43.summarize(["t1", "t10"]))

