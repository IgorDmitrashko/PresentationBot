from Bot.Controller import base, disposable_mail
from Bot.Telegram import bot, button
from Bot.Model import config
from Bot.Parser import jsonParser, siteParser
import logging

bot = bot.Bot(config.BOT_TOKEN)
disposable_mail = disposable_mail.Disposable_mail()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler(
    "../tg_bot.log"), logging.StreamHandler()])

class MessageHandler:

    def __init__(self):
        self.tg_bot = bot
        self.base = base.Base()
        self.parser = jsonParser.JsonParser()
        self.button = button.Button()
        self.disposable_mail = disposable_mail
        self.site_parser = siteParser.SiteParser()
        self.commands_handler()

    def commands_handler(self):
        self.tg_bot.message_handler(commands=['start'])(self.welcome)
        self.tg_bot.message_handler(commands=['test1'])(self.test_command)
        self.tg_bot.message_handler(content_types=['text'])(self.handle_text)
        self.tg_bot.message_handler(content_types=['contact'])(self.handle_contact)
        self.tg_bot.callback_query_handler(func=lambda callback: True)(self.handle_callback)

    def handle_text(self, message):
        if message.text == 'Тест':
            disposable_mail.main()
        elif message.text == self.button.main_menu:
            self.send_main_menu(message)
        elif message.text == self.button.about_us:
            self.send_about_us(message)
        elif message.text == self.button.vending_machines:
            self.send_vending_menu(message)

    def handle_callback(self, callback):
        handlers = {
            'rate': self.send_exchange_rate,
            'image': self.send_nasa_image,
            'weather': self.send_weather_info,
            'vending': self.show_vending_menu,
            'back': self.show_main_menu,
            'bianchi': self.send_bianchi_link,
            'orki':self.send_orki,
            'iphone': self.send_price_iphone,
            'films': self.send_top_films,
        }
        handler = handlers.get(callback.data, self.handle_unknown_callback)
        handler(callback)

    def welcome(self, message):
        self.send_start_menu(message)

    def test_command(self, message):
        self.tg_bot.send_message(message.chat.id,text=self.site_parser.get_all_iphone_on_page("https://estore.ua/smartfony/manufacturer:apple/page=2")[0])
        if not self.initialize_database(message):
            return

    def send_top_films(self, callback):
        try:
            self.tg_bot.send_message(callback.message.chat.id, text=self.site_parser.get_top_films())
            self.tg_bot.delete_message(callback.message.chat.id, callback.message.message_id)
            logging.info("Top films sent to user %s", callback.message.chat.id)
        except Exception as ex:
            logging.error("Failed to send Top films: %s", ex)
            self.tg_bot.send_message(callback.message.chat.id, f"{self.site_parser.get_top_films()}")

    def handle_contact(self, message):
        if message.contact:
            self.tg_bot.send_message(message.chat.id, text=str(message.contact))
            logging.info("Contact processed")


    def initialize_database(self, message):
        try:
            self.base.set_datadb_()
            logging.info("Database initialized successfully.")
            return True
        except Exception as ex:
            logging.error("Database initialization failed: %s", ex)
            self.tg_bot.send_message(message.chat.id, text='База нот воркінг')
            return False

    def send_start_menu(self, message):
        try:
            self.tg_bot.send_message(message.chat.id, text='Стартове меню', reply_markup=self.button.get_buttons())
            self.tg_bot.delete_message(message.chat.id, message.message_id)
            logging.info("Start menu sent to user %s", message.chat.id)
        except Exception as ex:
            logging.info("Start menu sent to user %s", message.chat.id)
            self.tg_bot.send_message(message.chat.id, text='УПС!!\nЯкась помилка')

    def send_price_iphone(self, callback):
        try:
            self.tg_bot.send_message(callback.message.chat.id, text=self.site_parser.get_price_iphone15())
            self.tg_bot.delete_message(callback.message.chat.id, callback.message.message_id)
            logging.info("Price Iphone sent to user %s", callback.message.chat.id)
        except Exception as ex:
            logging.error("Failed to send Price Iphone: %s", ex)
            self.tg_bot.send_message(callback.message.chat.id, f"{self.site_parser.get_price_iphone15()}")

    def send_orki(self, callback):
        self.site_parser.get_top_films()
        try:
            self.tg_bot.send_message(callback.message.chat.id, text=self.site_parser.get_orki())
            self.tg_bot.delete_message(callback.message.chat.id, callback.message.message_id)

            logging.info("Orki sent to user %s", callback.message.chat.id)
        except Exception as ex:
            logging.error("Failed to send orki: %s", ex)
            self.tg_bot.send_message(callback.message.chat.id, f"{self.site_parser.get_orki()}")



    def send_main_menu(self, message):
        self.tg_bot.send_message(message.chat.id, "Головне меню", reply_markup=self.button.get_inline_buttons())
        self.tg_bot.delete_message(message.chat.id, message.message_id)
        logging.info("Main menu sent to user %s", message.chat.id)

    def send_about_us(self, message):

        try:
            self.tg_bot.send_message(message.chat.id, text=self.site_parser.get_videocards())
            self.tg_bot.delete_message(message.chat.id, message.message_id)
            logging.info("About us sent to user %s", message.chat.id)
        except Exception as ex:
            logging.error("Failed to send about us: %s", ex)
            self.tg_bot.send_message(message.chat.id, text=f"Помилка в бд {ex}")

    def send_vending_menu(self, message):
        self.tg_bot.send_message(message.chat.id, "Вендінг", reply_markup=self.button.get_inline_buttons_vending())
        self.tg_bot.delete_message(message.chat.id, message.message_id)
        logging.info("Vending menu sent to user %s", message.chat.id)

    def send_exchange_rate(self, callback):
        try:
            usd_rate = self.parser.get_rate()[1]["buy"]
            eur_rate = self.parser.get_rate()[0]["buy"]
            self.tg_bot.send_message(callback.message.chat.id, f"Курс долара США - {usd_rate}\nКурс Євро - {eur_rate}",
                                     reply_markup=self.button.get_inline_buttons())
            self.tg_bot.delete_message(callback.message.chat.id, callback.message.message_id)
            logging.info("Exchange rates sent to user %s", callback.message.chat.id)
        except Exception as ex:
            logging.error("Failed to send exchange rates: %s", ex)
            self.tg_bot.send_message(callback.message.chat.id, f"{self.parser.get_rate()}")

    def send_nasa_image(self, callback):
        try:
            image_url = self.parser.get_url_images_nasa()
            self.tg_bot.send_photo(callback.message.chat.id, photo=image_url, caption='Зображення фотографії NASA сьогоднішнього дня')
            logging.info("NASA image sent to user %s", callback.message.chat.id)
        except Exception as ex:
            logging.error("Failed to send NASA image: %s", ex)
            self.tg_bot.send_message(callback.message.chat.id, f"Помилка в запиті зображення: {ex}")

    def send_weather_info(self, callback):
        try:
            self.tg_bot.send_message(callback.message.chat.id, f"Погода в Києві - {self.parser.get_weather()}",
                                     reply_markup=self.button.get_inline_buttons())
            self.tg_bot.delete_message(callback.message.chat.id, callback.message.message_id)
            logging.info("Weather info sent to user %s", callback.message.chat.id)
        except Exception as ex:
            logging.error("Failed to send weather info: %s", ex)
            self.tg_bot.send_message(callback.message.chat.id, f"Помилка в запиті погоди {ex}")



    def show_vending_menu(self, callback):
        self.tg_bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                              reply_markup=self.button.get_inline_buttons_vending())
        logging.info("Vending menu shown to user %s", callback.message.chat.id)

    def show_main_menu(self, callback):
        self.tg_bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                              reply_markup=self.button.get_inline_buttons())
        logging.info("Main menu shown to user %s", callback.message.chat.id)

    def send_bianchi_link(self, callback):
        self.tg_bot.send_message(callback.message.chat.id, text='https://drive.google.com/file/d/1bFUNTc29dBpnj5uEnqtiPDMgpCoFZHTT/view?usp=sharing')
        logging.info("Bianchi link sent to user %s", callback.message.chat.id)

    def handle_unknown_callback(self, callback):
        self.tg_bot.send_message(callback.message.chat.id, "Невідома команда")
        logging.warning("Unknown command from user %s: %s", callback.message.chat.id, callback.data)

if __name__ == "__main__":
    MessageHandler()
    bot.polling(non_stop=True)
