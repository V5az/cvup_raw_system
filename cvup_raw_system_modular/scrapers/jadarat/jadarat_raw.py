
import asyncio
from shared.shared_write import write_row

async def run_jadarat_scraper():
    """Placeholder Jadarat scraper – will be implemented later."""
    print("🟡 Jadarat scraper placeholder running (no real scraping yet)...")
    # نكتب صف تجريبي واحد فقط في jobs_jadarat_raw
    try:
        row = ["TEST_RUN", "Placeholder from server", "", "", "", "", "", ""]
        write_row("jobs_jadarat_raw!A:H", row)
        print("✔ Test row written to jobs_jadarat_raw")
    except Exception as e:
        print("⚠ Could not write test row for Jadarat:", e)

    while True:
        await asyncio.sleep(3600)
