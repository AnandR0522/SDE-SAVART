
# ISIN-Based Stock Summary App

## Overview

This is a web application built using **Streamlit** and **BeautifulSoup** that allows users to fetch key stock data and qualitative insights using an **ISIN (International Securities Identification Number)**. The stock data is scraped from [Screener.in](https://www.screener.in), a popular financial website for Indian stocks.

## Features

- ISIN-based search for popular Indian stocks
- Web scraping of financial metrics such as:
  - Market Cap
  - Current Price
  - High / Low
  - Stock P/E
  - Book Value
  - Dividend Yield
  - ROCE
  - ROE
  - Face Value
- Displays qualitative **Pros** and **Cons** extracted from the stock's Screener page
- Clean and interactive UI powered by Streamlit

## Technologies Used

- Python 3
- Streamlit (for frontend)
- BeautifulSoup (for scraping)
- Requests (for HTTP handling)

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/isin-stock-summary.git
cd isin-stock-summary
```

### 2. Install Dependencies

Ensure you have Python 3.8 or above. Install required libraries:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can install manually:

```bash
pip install streamlit beautifulsoup4 requests
```

### 3. Run the App

```bash
streamlit run SDE2.py
```

The app will open in your default browser.

## Sample ISIN Codes

Some sample ISIN codes mapped in the app:

- `INE002A01018` - Reliance Industries
- `INE018A01030` - Infosys
- `INE062A01020` - HDFC
- `INE467B01029` - TCS
- `INE021A01026` - ITC

Feel free to expand the dictionary in `SDE2.py` to support more stocks.

## Folder Structure

```
.
├── SDE2.py              # Main application script
├── README.md            # Project documentation
└── requirements.txt     # (Optional) Python dependencies
```

## Assumptions and Limitations

- The app supports only a predefined set of ISIN codes mapped manually to Screener slugs.
- No real-time database or persistent storage is implemented.
- The scraping logic may break if Screener.in changes its layout or class names.

## Future Improvements

- Add search autocomplete or full-text lookup for ISIN codes.
- Expand ISIN-to-stock mapping dynamically.
- Integrate backend validation and API-based data fetching instead of scraping.
- Convert to a full-stack application with React frontend and Flask backend.

## License

This project is for educational/demo purposes only. Not affiliated with Screener.in.
