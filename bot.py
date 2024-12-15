import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from django.conf import settings
from users.models import *
from projectapp.models import *
import dotenv
dotenv.load_dotenv()


# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Command to start the bot
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    chat_id = str(update.message.chat_id)

    # Foydalanuvchi ma'lumotlarini saqlash
    TelegramUser.objects.get_or_create(chat_id=chat_id, defaults={'username': user.username, 'full_name': user.full_name})

    # Categorylar ro'yxatini olish va tugmalarni yaratish
    categories = Category.objects.all()
    keyboard = [[InlineKeyboardButton(category.name, callback_data=f"category_{category.id}") for category in categories]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Assalomu alaykum! Kategoriya tanlang:', reply_markup=reply_markup)


# Categoryni tanlash va uylarni yuborish
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    category_id = int(query.data.split("_")[1])
    category = Category.objects.get(id=category_id)

    apartments = Apartment.objects.filter(category=category)[:5]  # Dastlabki 5 ta uy

    # Uylarni yuborish
    apartment_info = "\n\n".join([f"{apartment.short_name} - {apartment.price} so'm" for apartment in apartments])
    query.edit_message_text(f"{category.name} kategoriyasidagi uylar:\n{apartment_info}")

    # Agar 5 tadan ko'proq bo'lsa, qo'shimcha yuborish kerakligini so'rash
    if apartments.count() > 5:
        query.message.reply_text("Yana ko'proq uylarni yuborish kerakmi?", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Ha", callback_data=f"more_{category.id}"), InlineKeyboardButton("Yo'q", callback_data="no_more")]
        ]))


# Qo'shimcha uylarni yuborish
def more_apartments(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    category_id = int(query.data.split("_")[1])
    category = Category.objects.get(id=category_id)

    apartments = Apartment.objects.filter(category=category)[5:]  # 6+ uylarni yuborish
    apartment_info = "\n\n".join([f"{apartment.short_name} - {apartment.price} so'm" for apartment in apartments])

    query.edit_message_text(f"{category.name} kategoriyasidagi qo'shimcha uylar:\n{apartment_info}")


# Botni ishga tushirish
def main():
    updater = Updater(os.getenv("TELEGRAM_BOT_TOKEN"))
    dp = updater.dispatcher

    # Start komandasini qo'shish
    dp.add_handler(CommandHandler("start", start))

    # Tugmalarga qaytish
    dp.add_handler(CallbackQueryHandler(button))

    # Qo'shimcha uylarni yuborish
    dp.add_handler(CallbackQueryHandler(more_apartments, pattern=r"more_"))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
