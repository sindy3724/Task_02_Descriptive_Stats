# Reflection – Task 02 Descriptive Statistics

## 1. Challenges Faced
One of the main challenges was ensuring consistent results across Pure Python, Pandas, and Polars. Each tool handles missing values, data types, and grouping differently, which required careful validation.

In Pure Python, all operations such as mean, median, and grouping had to be implemented manually, which increased complexity and risk of errors.

---

## 2. Differences Between Approaches

### Pure Python
- Required manual implementation of all statistical logic
- Very flexible but time-consuming
- Helpful for understanding how operations work internally

### Pandas
- Very easy to use with built-in functions like `describe()` and `groupby()`
- Well-suited for exploratory data analysis
- Slight performance limitations on very large datasets

### Polars
- Fastest among the three tools
- Uses expression-based syntax instead of index-based operations
- Requires adjustment in thinking compared to Pandas

---

## 3. Performance Observations
Polars performed significantly faster during grouping and aggregation operations. Pandas was moderately fast and easier to work with. Pure Python was the slowest due to manual iteration over rows.

---

## 4. Data Cleaning Observations
Some columns contained nested structures (lists and dictionaries as strings), which made it difficult to treat them as standard categorical variables. Missing values were mostly represented as empty strings or empty JSON-like structures.

---

## 5. Learning Outcomes
- Understood how statistical operations are implemented at a low level
- Learned the advantages of high-level libraries like Pandas and Polars
- Gained experience in handling large real-world datasets
- Improved understanding of grouped analysis and aggregation logic

---

## 6. AI Tool Usage
AI tools were helpful in generating initial code structures and debugging syntax issues. However, manual adjustments were required to ensure correctness and dataset compatibility across all three implementations.

---

## 7. Final Insight
Each tool serves a different purpose:
- Pure Python → learning fundamentals
- Pandas → general data analysis
- Polars → high-performance production-scale analytics