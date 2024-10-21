
import telebot
from telebot import types

bot = telebot.TeleBot('7751544858:AAH-kVNYBHGCVRjvhqCFRSVZxH647rcuGGI')

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Функционал')
    markup.add(btn1)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Функционал':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перевод частоты излучения или энергии фотона в длину волны света', callback_data='функция_1'))
        markup.add(types.InlineKeyboardButton('Перевод длины волны света в частоты излучения или энергии фотона',callback_data='функция_2'))
        markup.add(types.InlineKeyboardButton('Вычисление флюенса лазерной системы по средней мощности',callback_data='функция_3'))
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю')
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):

    if callback.data == 'функция_1':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Частоты излучения',callback_data='функция_излучение_длина'))
        markup.add(types.InlineKeyboardButton('Энергии фотона',callback_data='функция_энергия_длина'))
        bot.send_message(callback.message.chat.id, "Из каких данных надо переводить", reply_markup=markup)
    elif callback.data == 'функция_2':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Частоту излучения', callback_data='функция_длина_излучения'))
        markup.add(types.InlineKeyboardButton('Энергию фотона', callback_data='функция_длина_энергию'))
        bot.send_message(callback.message.chat.id, "В какие данные надо перевести", reply_markup=markup)

    elif callback.data == 'функция_излучение_длина':
        bot.send_message(callback.message.chat.id, 'Введите частоту (Гц):')
        bot.register_next_step_handler(callback.message, handle_frequency_length_input)
    elif callback.data == 'функция_энергия_длина':
        bot.send_message(callback.message.chat.id, 'Введите энергию фотона (эВ):')
        bot.register_next_step_handler(callback.message, handle_energy_length_input)
    elif  callback.data  == 'функция_длина_излучения':
        bot.send_message(callback.message.chat.id, 'Введите длину(м):')
        bot.register_next_step_handler(callback.message, handle_length_frequency_input)
    elif  callback.data  == 'функция_длина_энергию':
        bot.send_message(callback.message.chat.id, 'Введите длину(мкм):')
        bot.register_next_step_handler(callback.message, handle_length_energy_input)

    elif callback.data == 'функция_3':
        bot.send_message(callback.message.chat.id, f'3' )

    elif callback.data == 'вернуться_к_функциям':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перевод частоты излучения или энергии фотона в длину волны света',callback_data='функция_1'))
        markup.add(types.InlineKeyboardButton('Перевод длины волны света в частоты излучения или энергии фотона',callback_data='функция_2'))
        markup.add(types.InlineKeyboardButton('Вычисление флюенса лазерной системы по средней мощности', callback_data='функция_3'))
        bot.send_message(callback.message.chat.id, "Что вас интересует?", reply_markup=markup)

def handle_frequency_length_input(message):
    try:
        frequency = float(message.text)
        frequency1 = frequency
        length = 299792458 / frequency1
        if 10000 < length < 100000 :
            bot.send_message(message.chat.id, f"Длина составляет: {length} метров \nДиапазон длины волны: мириаметровые")
        elif 1000 < length <= 10000:
            bot.send_message(message.chat.id, f"Длина составляет: {length} метров \nДиапазон длины волны: километровые")
        elif 100 < length <= 1000:
            bot.send_message(message.chat.id, f"Длина составляет: {length} метров \nДиапазон длины волны: гектометровые")
        elif 10 < length <= 100:
            bot.send_message(message.chat.id, f"Длина составляет: {length} метров \nДиапазон длины волны: декаметровы")
        elif 1 < length <= 10:
            bot.send_message(message.chat.id, f"Длина составляет: {length} метров \nДиапазон длины волны: метровые")
        elif 0.1 < length <= 1:
            bot.send_message(message.chat.id, f"Длина составляет: {length} метров \nДиапазон длины волны: дециметровые")
        elif 0.01 < length <= 0.1:
            bot.send_message(message.chat.id, f"Длина составляет: {length} метров \nДиапазон длины волны: сантиметровые ")
        elif 0.001 < length <= 0.01:
            bot.send_message(message.chat.id,f"Длина составляет: {length} метров \nДиапазон длины волны: миллиметровые ")
        elif 0.0001 < length <= 0.001:
            bot.send_message(message.chat.id,f"Длина составляет: {length} метров \nДиапазон длины волны: децимиллиметровые ")
        else:
            bot.send_message(message.chat.id, f"Длина составляет: {length} \nДиапазон длины волны: недопустимая.")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Частоты излучения', callback_data='функция_излучение_длина'))
        markup.add(types.InlineKeyboardButton('Энергии фотона', callback_data='функция_энергия_длина'))
        markup.add(types.InlineKeyboardButton('Вернуться к функциям', callback_data='вернуться_к_функциям'))
        bot.send_message(message.chat.id, "Из каких данных надо переводить", reply_markup=markup)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

def handle_energy_length_input(message):
    try:
        energy = float(message.text)
        result=pow(10,-1)
        length=(((6.6* (3 * result))/1.6)/energy)
        if 0.01 < length < 0.1 :
            bot.send_message(message.chat.id, f"Длина составляет: {length} мкм \nДиапазон длины волны: мириаметровые")
        elif 0.001 < length <= 0.01:
            bot.send_message(message.chat.id, f"Длина составляет: {length} мкм \nДиапазон длины волны: километровые")
        elif 0.0001 < length <= 0.001:
            bot.send_message(message.chat.id, f"Длина составляет: {length} мкм \nДиапазон длины волны: гектометровые")
        elif 0.00001 < length <= 0.0001:
            bot.send_message(message.chat.id, f"Длина составляет: {length} мкм \nДиапазон длины волны: декаметровы")
        elif 0.000001 < length  <= 0.00001 :
            bot.send_message(message.chat.id, f"Длина составляет: {length} мкм \nДиапазон длины волны: метровые")
        elif 0.0000001 < length <= 0.000001:
            bot.send_message(message.chat.id, f"Длина составляет: {length} мкм \nДиапазон длины волны: дециметровые")
        elif 0.00000001 < length <= 0.0000001:
            bot.send_message(message.chat.id, f"Длина составляет: {length} мкм \nДиапазон длины волны: сантиметровые ")
        elif 0.000000001 < length <= 0.00000001:
            bot.send_message(message.chat.id,f"Длина составляет: {length} мкм \nДиапазон длины волны: миллиметровые ")
        elif 0.0000000001  < length  <= 0.000000001 :
            bot.send_message(message.chat.id,f"Длина составляет: {length} мкм \nДиапазон длины волны: децимиллиметровые ")
        else:
            bot.send_message(message.chat.id, f"Длина составляет: {length} \nДиапазон длины волны: недопустимая.")

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Частоты излучения', callback_data='функция_излучение_длина'))
        markup.add(types.InlineKeyboardButton('Энергии фотона', callback_data='функция_энергия_длина'))
        markup.add(types.InlineKeyboardButton('Вернуться к функциям', callback_data='вернуться_к_функциям'))
        bot.send_message(message.chat.id, "Из каких данных надо переводить", reply_markup=markup)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

def handle_length_frequency_input(message):
    try:
        frequency = float(message.text)
        frequency_1 = 299792458 / frequency
        bot.send_message(message.chat.id, f"Частота излучения состовляет: {frequency_1} Гц")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Частоту излучения', callback_data='функция_длина_излучения'))
        markup.add(types.InlineKeyboardButton('Энергию фотона', callback_data='функция_длина_энергию'))
        markup.add(types.InlineKeyboardButton('Вернуться к функциям', callback_data='вернуться_к_функциям'))
        bot.send_message(message.chat.id, "В какие данные надо перевести", reply_markup=markup)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

def handle_length_energy_input(message):
    try:
        energy = float(message.text)
        result = pow(10,-1)
        energy_1 = (6.6 * (3* result))/(energy * 1.6 )
        bot.send_message(message.chat.id, f"Энергия фотона составляет: {energy_1} эВ")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Частоту излучения', callback_data='функция_длина_излучения'))
        markup.add(types.InlineKeyboardButton('Энергию фотона', callback_data='функция_длина_энергию'))
        markup.add(types.InlineKeyboardButton('Вернуться к функциям', callback_data='вернуться_к_функциям'))
        bot.send_message(message.chat.id, "В какие данные надо перевести", reply_markup=markup)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

bot.polling(none_stop=True)












