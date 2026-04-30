import polars as pl

file = "C:\Users\sindy\Downloads\2024_fb_ads_president_scored_anon.csv"

df = pl.read_csv(file)

print("\n===== DATASET OVERVIEW =====")
print("Rows:", df.height)
print("Columns:", df.width)

# -----------------------
# MISSING VALUES
# -----------------------
print("\n===== MISSING VALUES =====")
missing = df.null_count()
print(missing)

# -----------------------
# DATA TYPES
# -----------------------
print("\n===== DATA TYPES =====")
print(df.schema)

# -----------------------
# NUMERIC STATS
# -----------------------
print("\n===== NUMERIC STATS =====")
print(df.describe())

# -----------------------
# CATEGORICAL STATS
# -----------------------
print("\n===== CATEGORICAL STATS =====")

cat_cols = [col for col, dtype in df.schema.items() if dtype == pl.Utf8]

for col in cat_cols[:10]:  # limit to avoid spam
    print(f"\nColumn: {col}")
    print(df[col].value_counts().head(5))

# -----------------------
# GROUP BY page_id
# -----------------------
if "page_id" in df.columns:
    print("\n===== GROUP BY page_id =====")
    print(
        df.group_by("page_id")
        .agg(pl.len().alias("count"))
        .sort("count", descending=True)
        .head(5)
    )

# -----------------------
# GROUP BY page_id + ad_id
# -----------------------
if "page_id" in df.columns and "ad_id" in df.columns:
    print("\n===== GROUP BY page_id + ad_id =====")
    print(
        df.group_by(["page_id", "ad_id"])
        .agg(pl.len().alias("count"))
        .sort("count", descending=True)
        .head(5)
    )