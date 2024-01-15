import polars as pl

# Print version
print(f"Polaris version : {pl.__version__}")

# Eager Quickstart

## Import CSV
df = pl.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
print(f"\n\n{df}\n")

## Filter by column value
df_filtered_by_sepal_length = df.filter(pl.col("sepal_length") > 5)
print(f"\n\n{df_filtered_by_sepal_length}\n")