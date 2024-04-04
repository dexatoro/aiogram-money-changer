import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
def get_currency_info(currency_code):
    return data['Valute'][currency_code]['Value']

async def send_currency_rate(callback, currency_name, currency_code):
    await callback.answer()
    await callback.message.answer(f'1 {currency_code} - {round(get_currency_info(currency_code),2)} рублей')
    
    