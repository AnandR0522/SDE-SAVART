# app.py
import streamlit as st
import requests
from bs4 import BeautifulSoup

# === ISIN to Screener Slug Mapping ===
ISIN_TO_SLUG = {
    "INE002A01018": "RELIANCE",
    "INE018A01030": "INFY",
    "INE062A01020": "HDFC",
    "INE467B01029": "TCS",
    "INE021A01026": "ITC",
    "INE005A01029": "BHEL",
    "INE237A01028": "BAJAJFINSV",
    "INE528G01035": "JUBLFOOD",
    "INE742F01042": "DMART",
    "INE040A01034": "HCLTECH",
    "INE503A01015": "MRF"
}

def get_stock_summary(slug):
    url = f"https://www.screener.in/company/{slug}/consolidated/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    stock_info = {} 
    pros, cons = [], []
    stock_name = "N/A"

    stock_name_tag = soup.find('h1', class_='page-header-title')
    if stock_name_tag:
        stock_name = stock_name_tag.text.strip()
    else:
        notebook_button = soup.find('button', class_='plausible-event-name=Notebook')
        if notebook_button and 'data-title' in notebook_button.attrs:
            stock_name = notebook_button['data-title'].strip()
        else:
            title_tag = soup.find('title')
            if title_tag:
                stock_name = title_tag.text.strip().split('|')[0].strip()

    top_ratios = soup.find('ul', id='top-ratios')
    if top_ratios:
        for item in top_ratios.find_all('li', class_='flex'):
            name = item.find('span', class_='name')
            value = item.find('span', class_='value')
            if name and value:
                stock_info[name.text.strip()] = ' '.join(value.stripped_strings)

    analysis = soup.find('section', id='analysis')
    if analysis:
        pros_div = analysis.find('div', class_='pros')
        cons_div = analysis.find('div', class_='cons')
        if pros_div:
            pros_ul = pros_div.find('ul')
            if pros_ul:
                pros = [li.text.strip() for li in pros_ul.find_all('li')]
        if cons_div:
            cons_ul = cons_div.find('ul')
            if cons_ul:
                cons = [li.text.strip() for li in cons_ul.find_all('li')]

    return stock_name, stock_info, pros, cons

# === Streamlit Web App ===
st.set_page_config(page_title="Stock Summary", layout="centered")

st.title(" Stock Summary (via ISIN)")
st.markdown("Enter an ISIN to fetch data from [Screener.in](https://www.screener.in)")

isin_input = st.text_input("Enter ISIN", value="INE002A01018").strip().upper()

if st.button("Get Stock Summary"):
    slug = ISIN_TO_SLUG.get(isin_input)

    if slug:
        st.info(f"Fetching data for ISIN: `{isin_input}` (Company: `{slug}`)...")
        stock_name, data, pros, cons = get_stock_summary(slug)

        st.header(f" {stock_name}")
        st.subheader("Key Metrics:")
        for key in ['Market Cap', 'Current Price', 'High / Low', 'Stock P/E', 'Book Value', 'Dividend Yield', 'ROCE', 'ROE', 'Face Value']:
            st.write(f"**{key}:** {data.get(key, 'N/A')}")

        st.subheader(" Pros")
        if pros:
            for p in pros:
                st.markdown(f"- {p}")
        else:
            st.write("No pros found.")

        st.subheader(" Cons")
        if cons:
            for c in cons:
                st.markdown(f"- {c}")
        else:
            st.write("No cons found.")
    else:
        st.error("ISIN not found in mapping.")
