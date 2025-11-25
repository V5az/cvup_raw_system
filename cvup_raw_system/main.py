
import asyncio
from telegram_raw import run_telegram_scraper
from jadarat_raw import run_jadarat_scraper

async def main():
    print("🚀 CVUP RAW SYSTEM started")
    # نشغّل كل ساحب بيانات كمهمة مستقلة
    await asyncio.gather(
        run_telegram_scraper(),
        run_jadarat_scraper(),
    )

if __name__ == "__main__":
    asyncio.run(main())
