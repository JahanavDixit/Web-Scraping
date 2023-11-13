# Web-Scraping and Content Extraction

## Overview

This Python script extracts content from a list of URLs specified in a CSV file (`Input.csv`). The script utilizes `requests` for making HTTP requests and `BeautifulSoup` for HTML parsing.

## Requirements

- [Python](https://www.python.org/) (version x.x.x)
- [pandas](https://pandas.pydata.org/)
- [requests](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Usage

1. Install the required Python libraries:

   ```bash
   pip install pandas requests beautifulsoup4


2. Run the script:

   ```bash
   python extract_content.py

## Notes
The script looks for content in specific HTML elements, such as `div` with classes `td-post-content tagdiv-type` or `tdb-block-inner td-fix-index`.
It excludes content inside `pre` elements with class `wp-block-preformatted`.

