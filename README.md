🚀 Large-Scale Retail Data Pipeline (4.3M Records)
📌 Project Overview
This project is an end-to-end data engineering solution for a massive sales dataset containing 4.3 million records. The workflow includes raw data extraction, automated Python cleaning, SQL Server storage, and an advanced Power BI dashboard.

🏗️ 1. Data Cleaning & ETL (Python)
The Challenge: The original dataset was massive and "dirty," containing null values, disordered formats, and duplicates that made it impossible to process in traditional tools like Excel.

The Solution: I developed a Python script using the Pandas library to process Big Data efficiently.

Removed duplicate records and managed null values to ensure data quality.

Standardized date formats and numerical columns for accurate analysis.

Automated the export of optimized data into a clean CSV format.

🗄️ 2. Database Integration (SQL Server)
Used a connection script to migrate the 4.3 million clean records directly into a SQL Server database (BASED).

Optimized SQL data types to ensure that queries and Power BI loading remained extremely fast despite the massive volume of information.

📊 3. Power BI Modeling & Insights
Connected Power BI to SQL Server to create a robust, scalable, and high-performance data model.

Developed an interactive report with 3 main perspectives:

Retail Dataset: Global analysis of sales, revenue, and time-series trends.

Inventory: Product performance and stock distribution using Treemaps and Scatter plots.

Operations: Hourly efficiency analysis and geographic revenue heatmaps.

🛠️ 4. Tech Stack
Python (Pandas & NumPy): Big Data cleaning, transformation, and manipulation.

SQL Server: Structured storage and relational database management.

Power BI (DAX & Power Query): Analytical modeling, advanced calculations, and data visualization.

📈 5. Key Results
Scalability: Successful processing and smooth visualization of 4.3 million rows with zero dashboard latency.

Automation: Drastic reduction in data preparation time (from hours of manual cleaning to seconds via code).

Data Integrity: 100% verified data ready for evidence-based business decision-making.
