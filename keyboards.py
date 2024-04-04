from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Курс валюты')]
],
                           resize_keyboard=True,
                           input_field_placeholder="Что вы хотите?"
)

rates = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Доллар',callback_data='dollar')],
    [InlineKeyboardButton(text='Евро',callback_data='euro')],
    [InlineKeyboardButton(text='Юань',callback_data='yuan')],
])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',request_contact=True)]],resize_keyboard=True)