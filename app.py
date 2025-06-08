import streamlit as st
import pandas as pd
import re

# Load CSV
df = pd.read_csv("scraped_leads.csv")

# Clean hourly rate
def parse_rate(rate_str):
    if pd.isna(rate_str) or not isinstance(rate_str, str):
        return None, None
    match = re.findall(r"\$?(\d+)", rate_str)
    if len(match) == 2:
        return int(match[0]), int(match[1])
    elif len(match) == 1:
        return int(match[0]), int(match[0])
    return None, None

df[['Min Rate', 'Max Rate']] = df['Hourly Rate'].apply(lambda x: pd.Series(parse_rate(x)))
df = df.dropna(subset=['Min Rate', 'Max Rate'])

# Unique locations for autocomplete
location_options = sorted(df['Location'].dropna().unique())

# Streamlit UI
st.title("💼 Smart Lead Generator")
st.markdown("Search and filter companies by location and hourly rate.")

# Hourly rate filter
min_rate = int(df['Min Rate'].min())
max_rate = int(df['Max Rate'].max())
rate_range = st.sidebar.slider("💲 Hourly Rate", min_value=min_rate, max_value=max_rate, value=(min_rate, max_rate))

# Autocomplete location filter
selected_location = st.selectbox("📍 Filter by Location", options=[""] + location_options)

# Apply filters
filtered_df = df[
    (df['Min Rate'] >= rate_range[0]) &
    (df['Max Rate'] <= rate_range[1])
]

if selected_location:
    filtered_df = filtered_df[filtered_df['Location'] == selected_location]

# Display
st.subheader(f"Showing {len(filtered_df)} matching leads")
if filtered_df.empty:
    st.info("No matching companies found.")
else:
    for _, row in filtered_df.iterrows():
        st.markdown(f"""
        <div style="font-size: 14px; line-height: 1.4; margin-bottom: 20px;">
            <strong style="font-size: 16px;">{row['Company Name']}</strong><br>
            🔗 <a href="{row['Website']}" target="_blank">{'Link'}</a><br>
            💰 <span style="color: #666;">Hourly Rate:</span> {row['Hourly Rate']}<br>
            📍 <span style="color: #666;">Location:</span> {row['Location']}
        </div>
        <hr style="border: 0; border-top: 1px solid #eee; margin: 10px 0;">
        """, unsafe_allow_html=True)

