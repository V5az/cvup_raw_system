import asyncio
from raw_sources.telegram_raw import run_telegram_scraper
from raw_sources.jadarat_raw import run_jadarat_scraper

async def main():
    print("🚀 CVUP RAW SYSTEM STARTED")

    # تشغيل كل سكرابر على حدة
    await asyncio.gather(
        run_telegram_scraper(),
        run_jadarat_scraper()
    )

if __name__ == "__main__":
    asyncio.run(main())
