import telegram, asyncio, aioschedule
from datetime import datetime, timezone, timedelta

token = ""
public_chat_name = ""
chat_id = ""

bot = telegram.Bot(token=token)

async def job():
    stamp = datetime.now(timezone(timedelta(hours=9)))
    await bot.send_message(chat_id=chat_id, text=f"{stamp.year} / {stamp.month} / {stamp.day} {stamp.hour}:{stamp.minute}:{stamp.second}")
    print(stamp)

async def main():
    while True:
        now = datetime.now(timezone(timedelta(hours=9))).time()
        if now >= datetime.strptime("23:00", "%H:%M").time() or now <= datetime.strptime("06:00", "%H:%M").time():
                print(f"SLEEP TIME : {str(now)}")
                pass
        else:
                await job()
        await asyncio.sleep(60*30)

if __name__ == "__main__":
    asyncio.run(main())