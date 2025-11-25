
المتغيرات المطلوبة في السيرفر (Railway أو غيره):

1) GOOGLE_CREDS_JSON
   • الصق فيه محتوى ملف Google Service Account JSON كامل.

2) SPREADSHEET_ID
   • حط فيه ID ملف Google Sheet اللي فيه التابات:
     - jobs_telegram_raw
     - jobs_jadarat_raw
     - jobs_twitter_raw (مستقبلاً)

3) TG_API_ID
   • رقم API ID من Telegram.

4) TG_API_HASH
   • قيمة API Hash من Telegram.

ملاحظة:
- لا ترفع ملف JSON إلى GitHub.
- فقط الصقه كنص في متغير GOOGLE_CREDS_JSON في إعدادات السيرفر.
