import pandas as pd
import sys

# ---------------------------
# LOAD DATA
# ---------------------------
file = "C:/Users/sindy/Downloads/2024_fb_posts_president_scored_anon.csv"
df = pd.read_csv(file, low_memory=False)

print("\n===== DATASET OVERVIEW =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# ---------------------------
# MISSING VALUES
# ---------------------------
print("\n===== MISSING VALUES =====")
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100

print(pd.DataFrame({
    "Missing Count": missing,
    "Missing %": missing_percent
}))

# ---------------------------
# DATA TYPES
# ---------------------------
print("\n===== DATA TYPES =====")
print(df.dtypes)

# ---------------------------
# NUMERIC STATS
# ---------------------------
print("\n===== NUMERIC STATS =====")
numeric = df.select_dtypes(include="number")

print(numeric.describe().T)

# ---------------------------
# CATEGORICAL STATS
# ---------------------------
print("\n===== CATEGORICAL STATS =====")
categorical = df.select_dtypes(exclude="number")

for col in categorical.columns:
    print(f"\nColumn: {col}")
    print("Count:", df[col].count())
    print("Unique:", df[col].nunique())
    print("Mode:", df[col].mode().iloc[0] if not df[col].mode().empty else None)
    print("Top 5:")
    print(df[col].value_counts().head(5))

# ---------------------------
# GROUP BY page_id
# ---------------------------
if "page_id" in df.columns:
    print("\n===== GROUP BY page_id =====")
    print(df.groupby("page_id").mean(numeric_only=True).head())

# ---------------------------
# GROUP BY page_id + ad_id
# ---------------------------
if "page_id" in df.columns and "ad_id" in df.columns:
    print("\n===== GROUP BY page_id + ad_id =====")
    print(
        df.groupby(["page_id", "ad_id"])
        .mean(numeric_only=True)
        .head()
    )


import pandas as pd
import sys

# ---------------------------
# LOAD DATA
# ---------------------------
file = "C:/Users/sindy/Downloads/2024_tw_posts_president_scored_anon.csv"
df = pd.read_csv(file, low_memory=False)

print("\n===== DATASET OVERVIEW =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# ---------------------------
# MISSING VALUES
# ---------------------------
print("\n===== MISSING VALUES =====")
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100

print(pd.DataFrame({
    "Missing Count": missing,
    "Missing %": missing_percent
}))

# ---------------------------
# DATA TYPES
# ---------------------------
print("\n===== DATA TYPES =====")
print(df.dtypes)

# ---------------------------
# NUMERIC STATS
# ---------------------------
print("\n===== NUMERIC STATS =====")
numeric = df.select_dtypes(include="number")

print(numeric.describe().T)

# ---------------------------
# CATEGORICAL STATS
# ---------------------------
print("\n===== CATEGORICAL STATS =====")
categorical = df.select_dtypes(exclude="number")

for col in categorical.columns:
    print(f"\nColumn: {col}")
    print("Count:", df[col].count())
    print("Unique:", df[col].nunique())
    print("Mode:", df[col].mode().iloc[0] if not df[col].mode().empty else None)
    print("Top 5:")
    print(df[col].value_counts().head(5))

# ---------------------------
# GROUP BY page_id
# ---------------------------
if "page_id" in df.columns:
    print("\n===== GROUP BY page_id =====")
    print(df.groupby("page_id").mean(numeric_only=True).head())

# ---------------------------
# GROUP BY page_id + ad_id
# ---------------------------
if "page_id" in df.columns and "ad_id" in df.columns:
    print("\n===== GROUP BY page_id + ad_id =====")
    print(
        df.groupby(["page_id", "ad_id"])
        .mean(numeric_only=True)
        .head()
    )