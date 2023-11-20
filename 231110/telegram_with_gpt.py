from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

load_dotenv()

async def call_gpt(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    prompt = update.message.text
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print(str(datetime.now()) + f' : {prompt}')
    await update.message.reply_text(completion.choices[0].message.content)



if __name__ == "__main__":
    application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, call_gpt))
    application.run_polling(allowed_updates=Update.ALL_TYPES)