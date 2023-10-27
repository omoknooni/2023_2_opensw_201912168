import telegram, asyncio, aioschedule
from datetime import datetime

token = ""
public_chat_name = ""
chat_id = ""

bot = telegram.Bot(token=token)
stamp = datetime.now()

# asyncio.run(bot.send_message(chat_id=chat_id, text=f"{stamp.year} / {stamp.month} / {stamp.day} {stamp.hour}:{stamp.minute}:{stamp.second}"))
async def job():
    stamp = datetime.now()
    await bot.send_message(chat_id=chat_id, text=f"{stamp.year} / {stamp.month} / {stamp.day} {stamp.hour}:{stamp.minute}:{stamp.second}")
    print(stamp)

aioschedule.every(30).seconds.do(job)

loop = asyncio.get_event_loop()
while True:
    loop.run_until_complete(aioschedule.run_pending())
    asyncio.sleep(1)