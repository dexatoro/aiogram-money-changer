from aiogram.filters import Command
from aiogram.types import Message,CallbackQuery
from aiogram import F, Router
from ratefile import send_currency_rate
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    phone_number = State()

@router.message(Command('register'))
async def registration(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')

@router.message(Register.name)
async def registration_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Register.phone_number)
    await message.answer('Введите ваш номер телефона', reply_markup=kb.get_number)
    
@router.message(Register.phone_number)
async def registration_phone_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data['name']}\nВаш номер телефона:{data['phone_number']}')
    await state.clear()
    
@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}!\nТвой ид: "{message.from_user.id}',
                        reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_start(message: Message):
    await message.answer('Это бот выдающий курс')

@router.message(F.text == "Курс валюты")
async def rate(message: Message):
    await message.answer('Выберите валюту',
                         reply_markup=kb.rates)
  
@router.callback_query(F.data == 'dollar')    
async def dollar_rate(callback: CallbackQuery):
    await send_currency_rate(callback, 'Доллара', 'USD')

@router.callback_query(F.data == 'euro')    
async def dollar_rate(callback: CallbackQuery):
    await send_currency_rate(callback, 'Евро', 'EUR')

@router.callback_query(F.data == 'yuan')    
async def dollar_rate(callback: CallbackQuery):
    await send_currency_rate(callback, 'Юаня', 'CNY')

@router.message()
async def echo_message(message: Message):
    await message.answer(message.text)
