from gtts import gTTS
import markovify
import gender

from telegram.ext import (Updater, Filters, ConversationHandler, CommandHandler, MessageHandler)
import logging

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

logger = logging.getLogger(__name__)

def generate(text, out_file):
    tts = gTTS(text, lang="ru")
    tts.save(out_file)

def get_model(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()

    return markovify.Text(text)

def start(update, context):
    update.message.reply_text("Привет")

def error(update, context):
    logger.warning('update "%s" caused error "%s"', update, context.error)

def photo(update, context):
    largest_photo = update.message.photo[-1].get_file()
    print('photo caught')
    largest_photo.download("./user_data/test.jpg")
    return ConversationHandler.END

def cancel(update, context):
    return

def main():
    updater = Updater("847405208:AAG4ywLly9QausdtqJy3RIcfkk_mqD1PDFs", use_context=True)
    dp = updater.dispatcher

    handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    photo_handler = MessageHandler(Filters.photo, photo)

    dp.add_handler(photo_handler)
    dp.add_handler(handler)
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()