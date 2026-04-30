import csv
from collections import defaultdict, Counter
import math

# ---------------------------
# FILE PATH (CHANGE IF NEEDED)
# ---------------------------
file = "C:/Users/sindy/Downloads/2024_tw_posts_president_scored_anon.csv"

# ---------------------------
# LOAD DATA
# ---------------------------
with open(file, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

columns = list(rows[0].keys())

print("\n===== DATASET OVERVIEW =====")
print("Rows:", len(rows))
print("Columns:", len(columns))

# ---------------------------
# HELPERS
# ---------------------------
def is_number(x):
    try:
        float(x)
        return True
    except:
        return False

def mean(v): return sum(v)/len(v)

def median(v):
    v = sorted(v)
    n = len(v)
    return (v[n//2-1] + v[n//2]) / 2 if n % 2 == 0 else v[n//2]

def std(v):
    m = mean(v)
    return math.sqrt(sum((x - m)**2 for x in v)/len(v))

# ---------------------------
# MISSING VALUES
# ---------------------------
print("\n===== MISSING VALUES =====")
for col in columns:
    miss = sum(1 for r in rows if r[col] == "" or r[col] is None)
    print(col, ":", miss)

# ---------------------------
# COLUMN TYPES
# ---------------------------
num_cols = []
cat_cols = []

for col in columns:
    sample = [r[col] for r in rows[:1000] if r[col] != ""]

    if len(sample) > 0:
        ratio = sum(1 for v in sample if is_number(v)) / len(sample)
        if ratio > 0.7:
            num_cols.append(col)
        else:
            cat_cols.append(col)
    else:
        cat_cols.append(col)

# ---------------------------
# NUMERIC STATS
# ---------------------------
print("\n===== NUMERIC STATS =====")

for col in num_cols:
    vals = [float(r[col]) for r in rows if r[col] != ""]
    if not vals:
        continue

    print(f"\nColumn: {col}")
    print("Count:", len(vals))
    print("Mean:", mean(vals))
    print("Min:", min(vals))
    print("Max:", max(vals))
    print("Std:", std(vals))
    print("Median:", median(vals))

# ---------------------------
# CATEGORICAL STATS
# ---------------------------
print("\n===== CATEGORICAL STATS =====")

for col in cat_cols:
    vals = [r[col] for r in rows if r[col] != ""]
    c = Counter(vals)

    print(f"\nColumn: {col}")
    print("Count:", len(vals))
    print("Unique:", len(c))
    if c:
        print("Mode:", c.most_common(1)[0])
    print("Top 5:", c.most_common(5))

# ---------------------------
# GROUP BY page_id
# ---------------------------
if "page_id" in columns:
    print("\n===== GROUP BY page_id =====")
    g = defaultdict(list)

    for r in rows:
        g[r["page_id"]].append(r)

    for i, (k, v) in enumerate(g.items()):
        if i == 5: break
        print(k, "->", len(v))

# ---------------------------
# GROUP BY page_id + ad_id
# ---------------------------
if "page_id" in columns and "ad_id" in columns:
    print("\n===== GROUP BY page_id + ad_id =====")
    g = defaultdict(list)

    for r in rows:
        g[(r["page_id"], r["ad_id"])].append(r)

    for i, (k, v) in enumerate(g.items()):
        if i == 5: break
        print(k, "->", len(v))

import csv
from collections import defaultdict, Counter
import math

# ---------------------------
# FILE PATH (CHANGE IF NEEDED)
# ---------------------------
file = "C:/Users/sindy/Downloads/2024_fb_posts_president_scored_anon.csv"

# ---------------------------
# LOAD DATA
# ---------------------------
with open(file, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

columns = list(rows[0].keys())

print("\n===== DATASET OVERVIEW =====")
print("Rows:", len(rows))
print("Columns:", len(columns))

# ---------------------------
# HELPERS
# ---------------------------
def is_number(x):
    try:
        float(x)
        return True
    except:
        return False

def mean(v): return sum(v)/len(v)

def median(v):
    v = sorted(v)
    n = len(v)
    return (v[n//2-1] + v[n//2]) / 2 if n % 2 == 0 else v[n//2]

def std(v):
    m = mean(v)
    return math.sqrt(sum((x - m)**2 for x in v)/len(v))

# ---------------------------
# MISSING VALUES
# ---------------------------
print("\n===== MISSING VALUES =====")
for col in columns:
    miss = sum(1 for r in rows if r[col] == "" or r[col] is None)
    print(col, ":", miss)

# ---------------------------
# COLUMN TYPES
# ---------------------------
num_cols = []
cat_cols = []

for col in columns:
    sample = [r[col] for r in rows[:1000] if r[col] != ""]

    if len(sample) > 0:
        ratio = sum(1 for v in sample if is_number(v)) / len(sample)
        if ratio > 0.7:
            num_cols.append(col)
        else:
            cat_cols.append(col)
    else:
        cat_cols.append(col)

# ---------------------------
# NUMERIC STATS
# ---------------------------
print("\n===== NUMERIC STATS =====")

for col in num_cols:
    vals = [float(r[col]) for r in rows if r[col] != ""]
    if not vals:
        continue

    print(f"\nColumn: {col}")
    print("Count:", len(vals))
    print("Mean:", mean(vals))
    print("Min:", min(vals))
    print("Max:", max(vals))
    print("Std:", std(vals))
    print("Median:", median(vals))

# ---------------------------
# CATEGORICAL STATS
# ---------------------------
print("\n===== CATEGORICAL STATS =====")

for col in cat_cols:
    vals = [r[col] for r in rows if r[col] != ""]
    c = Counter(vals)

    print(f"\nColumn: {col}")
    print("Count:", len(vals))
    print("Unique:", len(c))
    if c:
        print("Mode:", c.most_common(1)[0])
    print("Top 5:", c.most_common(5))

# ---------------------------
# GROUP BY page_id
# ---------------------------
if "page_id" in columns:
    print("\n===== GROUP BY page_id =====")
    g = defaultdict(list)

    for r in rows:
        g[r["page_id"]].append(r)

    for i, (k, v) in enumerate(g.items()):
        if i == 5: break
        print(k, "->", len(v))

# ---------------------------
# GROUP BY page_id + ad_id
# ---------------------------
if "page_id" in columns and "ad_id" in columns:
    print("\n===== GROUP BY page_id + ad_id =====")
    g = defaultdict(list)

    for r in rows:
        g[(r["page_id"], r["ad_id"])].append(r)

    for i, (k, v) in enumerate(g.items()):
        if i == 5: break
        print(k, "->", len(v))