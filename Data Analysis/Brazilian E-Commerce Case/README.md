# Brazilian E-Commerce Case

Welcome to the **Brazilian E-Commerce Case** repository!  
This project contains code and notebooks related to the **analysis of e-commerce orders in Brazil**.

## Description

This repository aims to transform raw e-commerce data into a flat table and create a helpful and insightful **dashboard** for stakeholders.  
The main objective is to enable data-informed decision-making by analyzing customer behavior, sales trends, delivery performance, and other key metrics.

## Source Data

There are **9 different tables** that collectively provide information about e-commerce orders in Brazil.  
These tables include:

- Customers (olist_customers_dataset.csv)
- Orders (olist_orders_dataset.csv)
- Order Items (olist_order_items_dataset.csv)
- Payments (olist_order_payments_dataset.csv)
- Reviews (olist_order_reviews_dataset.csv)
- Sellers (olist_sellers_dataset.csv)
- Products (olist_products_dataset.csv)
- Geolocation (olist_geolocation_dataset.csv)
- Product Categories (olist_customers_dataset.csv)

## Flat Table Process

The first step in this project is to combine the 9 tables into a **flat table**.  
This flat table serves as the main data source for the **dashboard**.  
Performing **table merges** (using IDs and relationships).

## Dashboard Content

The dashboard can be accessed at [Brazilian E-Commerce Case Dashboard](https://lookerstudio.google.com/reporting/cb59c434-958d-4613-a67c-b0b1cd75a798/page/Hr91D)

The **dashboard** is designed to enable stakeholders to uncover patterns and generate actionable insight.  
It includes a range of charts, tables, and metrics, such as:

- **Pie Charts** — Distribution of payments, customer locations, or product categories.
- **Bar Charts** — Number of orders by state, delivery performance by region, or customer satisfaction scores.
- **Pivot Table** — An interactive view to break down metrics by multiple dimensions (such as country, delivery time, or seller).

## File Structure

```
E-commerce-Brazil/
 ├── data/
 ├── notebook/
```

- **data/** — Stores raw CSV files with all 9 tables.
- **notebook/** — Stores code for data transformation and flat table preparation.
