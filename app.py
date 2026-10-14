import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Interactive Business Dashboard", page_icon="📊", layout="wide")

DATA_PATH = Path(__file__).with_name("dashboard_sample_dataset.csv")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
    df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce").fillna(0)
    for col in ["Active_Users", "Churned_Customers"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
    return df.dropna(subset=["Date", "Region", "Category"])

df = load_data()
st.title("📊 Interactive Business Intelligence Dashboard")
st.caption("Explore revenue, users, churn and average ticket-size proxy. Sample data is synthetic and intended for demonstration.")

with st.sidebar:
    st.header("Filters")
    min_date, max_date = df["Date"].min().date(), df["Date"].max().date()
    date_range = st.date_input("Date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)
    selected_regions = st.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
    selected_categories = st.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = date_range
filtered = df[(df["Date"].dt.date >= start_date) & (df["Date"].dt.date <= end_date)]
filtered = filtered[filtered["Region"].isin(selected_regions) & filtered["Category"].isin(selected_categories)]

if filtered.empty:
    st.warning("No records match the selected filters. Please change the date range, region or category.")
    st.stop()

revenue = filtered["Revenue"].sum()
active_users = int(filtered["Active_Users"].sum())
churned = int(filtered["Churned_Customers"].sum())
churn_rate = (churned / active_users * 100) if active_users else 0
# The sample does not include order counts, so this is revenue per active user, used as an average-ticket proxy.
avg_ticket_proxy = revenue / active_users if active_users else 0

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Revenue", f"₹{revenue:,.0f}")
k2.metric("Active Users", f"{active_users:,}")
k3.metric("Churn Rate", f"{churn_rate:.2f}%")
k4.metric("Avg Ticket Size*", f"₹{avg_ticket_proxy:,.2f}")
st.caption("*For this sample, average ticket size is approximated as revenue ÷ active users because order-count data is not provided. Replace with revenue ÷ orders for a true average order value.")

left, right = st.columns(2)
monthly = filtered.groupby(filtered["Date"].dt.to_period("M").astype(str), as_index=False)["Revenue"].sum().rename(columns={"Date":"Month"})
fig_month = px.line(monthly, x="Month", y="Revenue", markers=True, title="Monthly Revenue Trend", labels={"Revenue":"Revenue (₹)", "Month":"Month"})
left.plotly_chart(fig_month, use_container_width=True)
region_rev = filtered.groupby("Region", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False)
fig_region = px.bar(region_rev, x="Region", y="Revenue", title="Revenue by Region", color="Region", labels={"Revenue":"Revenue (₹)"})
right.plotly_chart(fig_region, use_container_width=True)

left2, right2 = st.columns(2)
cat_rev = filtered.groupby("Category", as_index=False)["Revenue"].sum()
fig_cat = px.pie(cat_rev, names="Category", values="Revenue", hole=0.45, title="Revenue Mix by Category")
left2.plotly_chart(fig_cat, use_container_width=True)
region_users = filtered.groupby("Region", as_index=False)["Active_Users"].sum().sort_values("Active_Users", ascending=False)
fig_users = px.bar(region_users, x="Region", y="Active_Users", title="Active Users by Region", labels={"Active_Users":"Active users"})
right2.plotly_chart(fig_users, use_container_width=True)

st.subheader("Filtered data")
st.dataframe(filtered.sort_values("Date", ascending=False), use_container_width=True, hide_index=True)
st.download_button("Download filtered data as CSV", filtered.to_csv(index=False).encode("utf-8"), file_name="filtered_dashboard_data.csv", mime="text/csv")
st.info("Demo reminder: this dashboard uses synthetic sample data, not actual company records. Validate definitions and replace the CSV before using it for business decisions.")
