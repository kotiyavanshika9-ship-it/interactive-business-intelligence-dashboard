# Interactive Business Intelligence Dashboard

## 1. Project Overview

The Interactive Business Intelligence Dashboard is a data visualization project developed using Python, Streamlit, Pandas, and Plotly. It helps users analyze business performance through interactive charts, KPI cards, and filters.

The dashboard displays important business metrics such as total revenue, active users, churn rate, and average ticket size.

## 2. Project Objectives

- Build an interactive business intelligence dashboard.
- Display key performance indicators (KPIs).
- Analyze revenue and user activity across different regions and categories.
- Provide date, region, and category filters.
- Present business data through charts and tables.
- Demonstrate how data visualization supports business decision-making.

## 3. Technologies Used

- **Python:** Main programming language.
- **Streamlit:** Web-based dashboard development.
- **Pandas:** Data cleaning and manipulation.
- **Plotly:** Interactive charts and visualizations.
- **CSV:** Sample dataset storage.
- **GitHub:** Source code management and project submission.
- **Streamlit Community Cloud:** Optional online deployment.

## 4. Key Features

- KPI cards for Total Revenue, Active Users, Churn Rate, and Average Ticket Size.
- Interactive date-range selection.
- Region and category filters.
- Monthly revenue trend chart.
- Revenue comparison by region.
- Category-wise revenue visualization.
- Active users by region.
- Data table and CSV download option.

## 5. Project Structure

```text
Interactive-Dashboard/
├── app.py
├── dashboard_sample_dataset.csv
├── requirements.txt
├── Interactive_BI_Dashboard.ipynb
├── Interactive_Dashboard_Project_Report.pdf
└── README.md
```

## 6. Installation and Setup

### Step 1: Install Python

Install Python on your computer if it is not already installed.

### Step 2: Download the Project

Download or clone this repository and open the project folder in VS Code or a terminal.

### Step 3: Install Dependencies

Run the following command:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Dashboard

Run this command:

```bash
streamlit run app.py
```

The dashboard will open in your browser, usually at `http://localhost:8501`.

## 7. Dataset Description

The project uses a sample CSV dataset containing business information such as:

- Date
- Region
- Category
- Revenue
- Active Users
- Churned Customers

**Note:** The included dataset is synthetic demonstration data. Replace it with verified business data before using the dashboard for real business decisions.

## 8. Key Performance Indicators

- **Total Revenue:** Total revenue for the selected data.
- **Active Users:** Total active users represented in the selected records.
- **Churn Rate:** Estimated percentage of users who discontinued the service, based on the available sample fields and the application's calculation.
- **Average Ticket Size:** Revenue divided by active users in this demonstration. This is a proxy; a standard average order ticket should generally use the number of orders as the denominator.

## 9. Deployment

The dashboard can be deployed online using Streamlit Community Cloud.

1. Upload the project files to a public GitHub repository.
2. Open https://share.streamlit.io/.
3. Sign in and connect your GitHub account.
4. Select the repository and branch.
5. Set the main file path to `app.py`.
6. Deploy the application.
7. Test the public dashboard URL before submitting it.

Deployment requires access to your own GitHub and Streamlit accounts.

## 10. Expected Outcomes

The project demonstrates how interactive dashboards can help users monitor performance, compare regions, explore category trends, and identify areas that may require further business investigation.

## 11. Limitations

- The included dataset is synthetic and may not reflect actual business performance.
- KPI accuracy depends on the dataset and calculation definitions.
- The dashboard's usefulness depends on data quality and completeness.

## 12. Future Enhancements

- Connect the dashboard to a live database.
- Add user authentication and role-based access.
- Include sales forecasting and advanced analytics.
- Add automated data refresh.
- Integrate real business datasets and validated churn definitions.

## 13. Conclusion

This project provides a practical introduction to business intelligence and interactive data visualization. By combining Python, Streamlit, Pandas, and Plotly, it transforms structured data into an accessible dashboard that supports exploratory analysis and informed decision-making.

## 14. Author

**Project:** Interactive Business Intelligence Dashboard  
**Purpose:** Academic / Internship Project  
**Status:** Demonstration version
