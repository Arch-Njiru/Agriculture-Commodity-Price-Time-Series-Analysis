# Agricultural Crops and Livestock Analysis in Kenya

## Project Overview
This project focuses on the analysis of agricultural commodities in Kenya, specifically seasonal and perennial crops, livestock, and fresh water fish. The goal of this project is to perform time-series analyses on supply volumes and profitability, ultimately providing actionable insights and recommendations for smallholder farmers.

The analysis covers the period from **2019 - 2024**, based on a dataset containing information about various commodities, markets, and regions in Kenya. The project explores trends in the following categories:
- Seasonal Crops
- Perennial Crops
- Livestock
- Fresh Water Fish
- Salt Water Fish (future analysis)

## Objectives
1. **Data Cleaning and Preprocessing**: Handle missing data, filter out irrelevant entries, and split the dataset into meaningful categories (e.g., seasonal crops, perennial crops, livestock).
2. **Exploratory Data Analysis (EDA)**: Identify key trends, most profitable commodities, and high-performing markets.
3. **Time-Series Analysis**: Visualize trends in supply volumes and profitability over time to predict market performance.
4. **Insights for Smallholder Farmers**: Provide actionable recommendations based on analysis, focusing on improving farmer profits and decision-making.

## Data
The dataset covers the following key columns:
- `commodity`: The name of the agricultural product.
- `market`: The marketplace where the product is sold.
- `county`: The region where the market is located.
- `volume_supplied_tonnes`: The quantity of the commodity supplied (in kilograms).
- `wholesale_price_ksh`: The wholesale price in Kenyan Shillings (KSh).
- `retail_price_ksh`: The retail price in Kenyan Shillings (KSh).

## Notebooks
The analysis is split into the following sections:
1. **Preliminary Data Cleaning**: The first notebook, which handles raw data cleaning and splits the dataset into appropriate categories (e.g., seasonal crops, perennial crops, livestock).
2. **Seasonal Crops Analysis**: Focuses on the time-series analysis and profitability of seasonal crops.
3. **Perennial Crops Analysis**: Time-series analysis and profitability for perennial crops.
4. **Livestock Analysis**: Analysis of livestock and livestock products, segmented by categories (e.g., meat, milk, hide).
5. **Fresh Water Fish Analysis** (Future): Insights on supply trends in the freshwater fish market.
6. **Price Prediction Model** (Future): Build a predictive models for volume and price trends.

## Key Insights
Some of the key insights from the analysis include:
- **Top commodities by volume**: A ranking of the most and least supplied commodities across different categories.
- **Market analysis**: Identification of the highest and lowest-performing markets in terms of volume and profitability.
- **Profitability analysis**: Key commodities with the highest resell profit percentages, and recommendations for smallholder farmers to focus on more profitable products.
  
## Recommendations for Smallholder Farmers
- **Focus on High-Profit Commodities**: Based on resell profit percentages, commodities such as cassava fresh and maize flour present significant profitability opportunities.
- **Target Strategic Markets**: Markets like `Naivasha Market` and `Kitale Municipality Market` show consistently high volumes, suggesting strong demand.
- **Seasonal Crops Strategy**: Farmers should consider timing their harvest and supply during peak market demands to maximize profits.
