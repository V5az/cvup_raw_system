
import asyncio
from scrapers.telegram.telegram_raw import run_telegram_scraper
from scrapers.jadarat.jadarat_raw import run_jadarat_scraper

async def main():
    print("🚀 CVUP RAW SYSTEM started")
    await asyncio.gather(
        run_telegram_scraper(),
        run_jadarat_scraper(),
    )

if __name__ == "__main__":
    asyncio.run(main())
