import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import InlineQuery, InlineQueryResultCachedVoice, Message

# Токен в кавычках
BOT_TOKEN = "9160886203:AAF8n-3WBWt0ftBOWPIEowmIxlMfULEgJdE"

SOUNDS = {
    "голубцы, давай": "AwACAgQAAxkBAAMDauyEjd6Jem2sbbEqvrPpCCnYIHQAAhY1AAKfv7lTAAFvTZ4fc1-vPQQ",
    "быстрее(мэл)": "AwACAgQAAxkBAAMHauyVi-kDUga9cAIjGfke85aYjT0AAu80AAKfv7lT6wf5CCmFyDk9BA",
    "мама, вызывай такси": "AwACAgQAAxkBAAMJau7uRlnW1vs3m9hItUgtL8Meh6cAApMdAALIB9lTrQf_KYQtulE9BA",
    "дядь, не в маст тебе такие котлы": "AwACAgQAAxkBAAMLau7ubArQk05ChiOJVX576YART5kAAn8dAALIB9lTc61N_z8XPCk9BA",
    "червячки": "AwACAgQAAxkBAAMNau7ujz6BZd5Y6AnV6zJ1sSd6XBwAAlpCAAKT0ehSPBYsDpZvJ2M9BA",
    "bombardilo crocodilo": "AwACAgQAAxkBAAMPau7ut5Ab0nKwTn3BUYmd0CirWZIAAkBCAAKT0ehSW_CeCP8PNkM9BA",
    "минетики": "AwACAgQAAxkBAAMRau7u6NyrnfU3VJWaYDE91d7ZS84AArEfAAKRrcFSghU-ymBsmd09BA",
}

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.inline_query()
async def inline_sound_handler(inline_query: InlineQuery):
    query_text = inline_query.query.lower().strip()
    results = []
    
    for idx, (name, file_id) in enumerate(SOUNDS.items()):
      
        if query_text in name.lower():
            results.append(
                InlineQueryResultCachedVoice(
                    id=str(idx),
                    voice_file_id=file_id,
                    title=name
                )
            )
            
    
    await inline_query.answer(results[:50], cache_time=1, is_personal=True)

@dp.message(F.voice | F.audio | F.document)
async def get_file_id(message: Message):
    if message.voice:
        file_id = message.voice.file_id
        file_type = "Голосовое сообщение"
    elif message.audio:
        file_id = message.audio.file_id
        file_type = "Аудиофайл"
    elif message.document:
        file_id = message.document.file_id
        file_type = "Документ"
    else:
        return
    
    # HTML-тег <code> делает текст копируемым в один клик и не ломается от символов "_"
    await message.answer(f"<b>{file_type} file_id:</b>\n<code>{file_id}</code>", parse_mode="HTML")

async def main():
    print("Бот запущен. Нажми Ctrl+C для остановки.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())