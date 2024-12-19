from telebot import types


class Button:

    def __init__(self):
        self.button_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        self.main_menu = "Головне меню"
        self.about_us = "Про нас"
        self.rate = "Курс"
        self.vending_machines = "Вендінг"
        self.back = "Назад"
        self.weather = "Погода"
        self.images_nasa = "Зображення"
        self.orki = "Орки"
        self.iphone = "Iphone"
        self.films = "Films"
        self.AI = "AI"

    def get_inline_buttons(self) -> types.InlineKeyboardMarkup:
        buttons = [
            types.InlineKeyboardButton(self.rate, callback_data='rate'),
            types.InlineKeyboardButton(self.weather, callback_data='weather'),
            types.InlineKeyboardButton(self.vending_machines, callback_data='vending'),
            types.InlineKeyboardButton(self.images_nasa, callback_data='image'),
            types.InlineKeyboardButton(self.orki, callback_data='orki'),
            types.InlineKeyboardButton(self.iphone, callback_data='iphone'),
            types.InlineKeyboardButton(self.films, callback_data='films'),
            types.InlineKeyboardButton(self.AI, callback_data='AI'),
        ]
        return types.InlineKeyboardMarkup(row_width=2).add(*buttons)

    def get_inline_buttons_vending(self) -> types.InlineKeyboardMarkup:
        buttons = [
            types.InlineKeyboardButton("Saeco", callback_data='saeco'),
            types.InlineKeyboardButton("Bianchi", callback_data='bianchi'),
            types.InlineKeyboardButton(self.back, callback_data='back'),
        ]
        return types.InlineKeyboardMarkup(row_width=2).add(*buttons)

    def get_buttons(self) -> types.ReplyKeyboardMarkup:
        self.button_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [
            types.KeyboardButton(self.main_menu),
            types.KeyboardButton(self.about_us),
            types.KeyboardButton("Потрібен номер телефону", request_contact=True),
        ]
        return self.button_markup.add(*buttons)
