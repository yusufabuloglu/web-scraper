import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(url):
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    for a in soup.select(".titleline a"):
        data.append({
            "title": a.get_text(strip=True),
            "link": a.get("href")
        })
    return pd.DataFrame(data)

def main():
    parser = argparse.ArgumentParser(description="Simple web scraper")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--out", default="output.csv", help="Output CSV file")
    args = parser.parse_args()

    df = scrape(args.url)
    df.to_csv(args.out, index=False)
    print(f"Saved {len(df)} rows to {args.out}")

if __name__ == "__main__":
    main()