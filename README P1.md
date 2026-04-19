# 🚀 Large-Scale Retail Data Pipeline (4.3M Records)

## 📌 Project Overview / Resumen del Proyecto
**English:**
This project demonstrates an end-to-end data engineering and analytics solution for a massive retail dataset containing **4.3 million transactions**. The pipeline covers everything from raw data extraction and Python-based automated cleaning to SQL storage and advanced Power BI modeling.

**Español:**
Este proyecto demuestra una solución completa de ingeniería de datos y analítica para un dataset masivo de retail con **4.3 millones de transacciones**. El pipeline abarca desde la extracción de datos crudos y limpieza automatizada con Python, hasta el almacenamiento en SQL y modelado avanzado en Power BI.

---

## 🏗️ Architecture / Arquitectura

### 1. Data Cleaning & ETL (Python)
* **The Challenge:** The original 4.3M record dataset was inconsistent, with null values and disordered formatting that crashed traditional tools like Excel.
* **The Solution:** Developed a custom Python script using `Pandas` to handle big data efficiently.
    * Removed duplicates and handled null values.
    * Standardized date formats and numerical consistency.
    * Automated the export to a clean CSV.

### 2. Database Integration (SQL Server)
* Used a high-performance bridge script to migrate the cleaned 4.3M records into a **SQL Server** database (`BASED`).
* Optimized data types to ensure fast query responses for Power BI.

### 3. Business Intelligence (Power BI)
* **Data Modeling:** Connected Power BI to SQL Server using optimized schemas.
* **Insights:** Created a 3-page interactive report:
    * **Retail Dataset:** Global sales analysis and time-series trends.
    * **Inventory:** Product performance and stock distribution (Treemaps & Scatter plots).
    * **Operations:** Performance by hour and geographic revenue heatmaps.

---

## 🛠️ Tech Stack / Tecnologías
* **Python:** Pandas, NumPy (Data Cleaning)
* **SQL Server:** Data Storage & Management
* **Power BI:** DAX, Power Query, Data Visualization
* **GitHub:** Version Control

---

## 📊 Key Results / Resultados Clave
* **Scalability:** Successfully processed and visualized 4.3 million rows with zero performance lag.
* **Automation:** Reduced manual cleaning time from hours to seconds using Python.
* **Data Integrity:** 100% clean data verified via SQL constraints and Power BI audit measures.

---

## 📸 Dashboard Preview
*(Tip: Aquí arrastra las imágenes de tu Proyecto 1 que me pasaste, como la de Ventas Totales y la de Inventario)*

---
**Developed by:** [Tu Nombre o Usuario de GitHub]