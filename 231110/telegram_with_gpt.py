from openai import OpenAI
from dotenv import load_dotenv
import os
import telegram
import asyncio

load_dotenv()

bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))

def gpt(prompt):
    client = OpenAI(os.getenv('OPENAI_API_KEY'))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

async def main():
    openai = OpenAI(os.getenv('OPENAI_API_KEY'))
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    while True:
        message = await bot.get_updates()
        if message:
            prompt = message[0].message.text
            response = gpt(prompt)
            await bot.send_message(chat_id, response)

if __name__ == "__main__":
    asyncio.run(main())