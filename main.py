import config
import heroes
import images
import requests
import logging
import asyncio
import sqlite3
import os

from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
from bs4 import BeautifulSoup as BS
from sqlighter import SQLighter

print("[Log]: "+"All API loaded")
print("[Log]: "+"All files loaded")
print("[Log]: "+"All lib's loaded")

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.TOKEN)

dp = Dispatcher(bot)
#Пдключние к БД
db = SQLighter('heroes.db')

@dp.message_handler(commands = ['start'])
async def welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    item1 = types.KeyboardButton("Список героев")
    item2 = types.KeyboardButton("Полезная информация")
    item3 = types.KeyboardButton("Связки героев")
    markup.add(item1, item2, item3)

    await bot.send_message(message.chat.id, "Привет, я бот по игре AFK Arena", parse_mode = 'html', reply_markup = markup)

@dp.message_handler(commands = ['menu'])
async def menu(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    item1 = types.KeyboardButton("Список героев")
    item2 = types.KeyboardButton("Полезная информация")
    item3 = types.KeyboardButton("Связки героев")
    markup.add(item1, item2, item3)

    await bot.send_message(message.chat.id, "Меню", parse_mode = 'html', reply_markup = markup)
#           Небожители
@dp.message_handler(commands = ['celestials'])
async def celestials(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 3)
    item1 = types.KeyboardButton("Аталия")
    item2 = types.KeyboardButton("Илия и Лейла")
    item3 = types.KeyboardButton("Ортус")
    item4 = types.KeyboardButton("Талена")
    item5 = types.KeyboardButton("У-Кун")
    item6 = types.KeyboardButton("Флора")
    back = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3, item4, item5, item6, back)

    await bot.send_message(message.chat.id, "Герои фракции Небожители", parse_mode = 'html', reply_markup = markup)
#           Подземные жители
@dp.message_handler(commands = ['underground'])
async def underground(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 3)
    item1 = types.KeyboardButton("Эзиж")
    item2 = types.KeyboardButton("Мегира")
    item3 = types.KeyboardButton("Золрат")
    item4 = types.KeyboardButton("Хазард")
    item5 = types.KeyboardButton("Мезот")
    back = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3, item4, item5, back)

    await bot.send_message(message.chat.id, "Герои фракции Небожители", parse_mode = 'html', reply_markup = markup)
#           Герои из других измерений
@dp.message_handler(commands = ['other_dimensions'])
async def other_dimensions(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 2)
    item1 = types.KeyboardButton("Артур")
    item2 = types.KeyboardButton("Укио")
    item3 = types.KeyboardButton("Накоруру")
    back = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3, back)

    await bot.send_message(message.chat.id, "Герои фракции Небожители", parse_mode = 'html', reply_markup = markup)
#           Носители света
@dp.message_handler(commands = ['light'])
async def lightbringers(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 5)
    item1 = types.KeyboardButton("Люций")
    item2 = types.KeyboardButton("Белинда")
    item3 = types.KeyboardButton("Рован")
    item4 = types.KeyboardButton("Эстрильда")
    item5 = types.KeyboardButton("Райна")
    item6 = types.KeyboardButton("Фокс")
    item7 = types.KeyboardButton("Тэйн")
    item8 = types.KeyboardButton("Хендрик")
    item9 = types.KeyboardButton("Гвинет")
    item10 = types.KeyboardButton("Розалина")
    item11 = types.KeyboardButton("Сесилия",)
    item12 = types.KeyboardButton("Ригби")
    item13 = types.KeyboardButton("Оскар")
    back = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, back)

    await bot.send_message(message.chat.id, "Герои фракции Носители света", parse_mode = 'html', reply_markup = markup)
#           Громилы
@dp.message_handler(commands = ['thugs'])
async def thugs(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 5)
    item1 = types.KeyboardButton("Брутус")
    item2 = types.KeyboardButton("Хасос")
    item3 = types.KeyboardButton("Вурк")
    item4 = types.KeyboardButton("Нумису")
    item5 = types.KeyboardButton("Скрег")
    item6 = types.KeyboardButton("Варек")
    item7 = types.KeyboardButton("Антандра")
    item8 = types.KeyboardButton("Сафия")
    item9 = types.KeyboardButton("Сатрана")
    item10 = types.KeyboardButton("Тайдус")
    item11 = types.KeyboardButton("Скриат",)
    item12 = types.KeyboardButton("Аноки")
    item13 = types.KeyboardButton("Дрез")
    back = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, back)

    await bot.send_message(message.chat.id, "Герои фракции Громилы", parse_mode = 'html', reply_markup = markup)
#           Лесные жители
@dp.message_handler(commands = ['forest'])
async def forest(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 4)
    item1 = types.KeyboardButton("Немора")
    item2 = types.KeyboardButton("Каз")
    item3 = types.KeyboardButton("Ника")
    item4 = types.KeyboardButton("Тази")
    item5 = types.KeyboardButton("Ульмус")
    item6 = types.KeyboardButton("Сейрус")
    item7 = types.KeyboardButton("Эйрон")
    item8 = types.KeyboardButton("Горво")
    item9 = types.KeyboardButton("Лорсан")
    item10 = types.KeyboardButton("Саурус")
    item11 = types.KeyboardButton("Солиса")
    back = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, back)

    await bot.send_message(message.chat.id, "Герои фракции Лесные жители", parse_mode = 'html', reply_markup = markup)
#           Могилорождённые
@dp.message_handler(commands = ['grave'])
async def grave(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 5)
    item1 = types.KeyboardButton("Грежул")
    item2 = types.KeyboardButton("Шемира")
    item3 = types.KeyboardButton("Торан")
    item4 = types.KeyboardButton("Изабелла")
    item5 = types.KeyboardButton("Нара")
    item6 = types.KeyboardButton("Фераэль")
    item7 = types.KeyboardButton("Баден")
    item8 = types.KeyboardButton("Кельтур")
    item9 = types.KeyboardButton("Оден")
    item10 = types.KeyboardButton("Изольд")
    item11 = types.KeyboardButton("Торн")
    item12 = types.KeyboardButton("Дэймон")
    back = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

    await bot.send_message(message.chat.id, "Герои фракции Могилорождённые", parse_mode = 'html', reply_markup = markup)

@dp.message_handler(content_types=['text'])
async def buttons(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Список героев':

            await bot.send_message(message.chat.id, "Выбирете Фракцию:" + '\n' +  "/light - Носители света"+ '\n' + "/thugs - Громилы" + '\n' + "/forest - Лесные жители" + '\n' +"/grave - Могилорождённые"+ '\n' +"/celestials - Небожители"+ '\n' +"/underground - Подземные жители"+ '\n' +"/other_dimensions - Герои из других измерений")
        #Фракция носители света
        elif message.text =='Люций':
            await bot.send_photo(message.chat.id, images.lucius)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[0]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[0]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[0]['Фракция'] + '\n' + heroes.heroesFullInfo[0]['Роль'])
        elif message.text =='Белинда':
            await bot.send_photo(message.chat.id, images.belinda)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[1]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[1]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[1]['Фракция'] + '\n' + heroes.heroesFullInfo[1]['Роль'])
        elif message.text =='Рован':
            await bot.send_photo(message.chat.id, images.rowan)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[2]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[2]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[2]['Фракция'] + '\n' + heroes.heroesFullInfo[2]['Роль'])
        elif message.text =='Эстрильда':
            await bot.send_photo(message.chat.id, images.estrilda)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[3]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[3]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[3]['Фракция'] + '\n' + heroes.heroesFullInfo[3]['Роль'])
        elif message.text =='Райна':
            await bot.send_photo(message.chat.id, images.raina)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[4]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[4]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[4]['Фракция'] + '\n' + heroes.heroesFullInfo[4]['Роль'])
        elif message.text =='Фокс':
            await bot.send_photo(message.chat.id, images.foks)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[5]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[5]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[5]['Фракция'] + '\n' + heroes.heroesFullInfo[5]['Роль'])
        elif message.text =='Тэйн':
            await bot.send_photo(message.chat.id, images.tein)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[6]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[6]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[6]['Фракция'] + '\n' + heroes.heroesFullInfo[6]['Роль'])
        elif message.text =='Хендрик':
            await bot.send_photo(message.chat.id, images.hendrik)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[7]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[7]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[7]['Фракция'] + '\n' + heroes.heroesFullInfo[7]['Роль'])
        elif message.text =='Гвинет':
            await bot.send_photo(message.chat.id, images.gvinet)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[8]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[8]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[8]['Фракция'] + '\n' + heroes.heroesFullInfo[8]['Роль'])
        elif message.text =='Розалина':
            await bot.send_photo(message.chat.id, images.rozalina)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[9]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[9]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[9]['Фракция'] + '\n' + heroes.heroesFullInfo[9]['Роль'])
        elif message.text =='Сесилия':
            await bot.send_photo(message.chat.id, images.sesilia)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[10]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[10]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[10]['Фракция'] + '\n' + heroes.heroesFullInfo[10]['Роль'])
        elif message.text =='Ригби':
            await bot.send_photo(message.chat.id, images.rigbi)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[11]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[11]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[11]['Фракция'] + '\n' + heroes.heroesFullInfo[11]['Роль'])
        elif message.text =='Оскар':
            await bot.send_photo(message.chat.id, images.oskar)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[12]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[12]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[12]['Фракция'] + '\n' + heroes.heroesFullInfo[12]['Роль'])

        #Фракция Громилы

        elif message.text =='Брутус':
            await bot.send_photo(message.chat.id, images.brutus)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[13]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[13]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[13]['Фракция'] + '\n' + heroes.heroesFullInfo[13]['Роль'])
        elif message.text =='Хасос':
            await bot.send_photo(message.chat.id, images.hasos)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[14]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[14]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[14]['Фракция'] + '\n' + heroes.heroesFullInfo[14]['Роль'])
        elif message.text =='Вурк':
            await bot.send_photo(message.chat.id, images.wurk)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[15]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[15]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[15]['Фракция'] + '\n' + heroes.heroesFullInfo[15]['Роль'])
        elif message.text =='Нумису':
            await bot.send_photo(message.chat.id, images.numisu)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[16]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[16]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[16]['Фракция'] + '\n' + heroes.heroesFullInfo[16]['Роль'])
        elif message.text =='Скрег':
            await bot.send_photo(message.chat.id, images.skreg)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[17]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[17]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[17]['Фракция'] + '\n' + heroes.heroesFullInfo[17]['Роль'])
        elif message.text =='Варек':
            await bot.send_photo(message.chat.id, images.warek)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[18]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[18]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[18]['Фракция'] + '\n' + heroes.heroesFullInfo[18]['Роль'])
        elif message.text =='Антандра':
            await bot.send_photo(message.chat.id, images.antandra)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[19]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[19]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[19]['Фракция'] + '\n' + heroes.heroesFullInfo[19]['Роль'])
        elif message.text =='Сафия':
            await bot.send_photo(message.chat.id, images.safia)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[20]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[20]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[20]['Фракция'] + '\n' + heroes.heroesFullInfo[20]['Роль'])
        elif message.text =='Сатрана':
            await bot.send_photo(message.chat.id, images.satrana)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[21]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[21]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[21]['Фракция'] + '\n' + heroes.heroesFullInfo[21]['Роль'])
        elif message.text =='Тайдус':
            await bot.send_photo(message.chat.id, images.taidus)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[22]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[22]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[22]['Фракция'] + '\n' + heroes.heroesFullInfo[22]['Роль'])
        elif message.text =='Скриат':
            await bot.send_photo(message.chat.id, images.skriat)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[23]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[23]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[23]['Фракция'] + '\n' + heroes.heroesFullInfo[23]['Роль'])
        elif message.text =='Аноки':
            await bot.send_photo(message.chat.id, images.anoki)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[24]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[24]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[24]['Фракция'] + '\n' + heroes.heroesFullInfo[24]['Роль'])
        elif message.text =='Дрез':
            await bot.send_photo(message.chat.id, images.drez)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[62]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[62]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[62]['Фракция'] + '\n' + heroes.heroesFullInfo[62]['Роль'])

        #Фракция Лесные жители

        elif message.text =='Немора':
            await bot.send_photo(message.chat.id, images.nemora)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[25]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[25]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[25]['Фракция'] + '\n' + heroes.heroesFullInfo[25]['Роль'])
        elif message.text =='Каз':
            await bot.send_photo(message.chat.id, images.kaz)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[26]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[26]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[26]['Фракция'] + '\n' + heroes.heroesFullInfo[26]['Роль'])
        elif message.text =='Лика':
            await bot.send_photo(message.chat.id, images.lika)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[27]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[27]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[27]['Фракция'] + '\n' + heroes.heroesFullInfo[27]['Роль'])
        elif message.text =='Тази':
            await bot.send_photo(message.chat.id, images.tazi)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[28]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[28]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[28]['Фракция'] + '\n' + heroes.heroesFullInfo[28]['Роль'])
        elif message.text =='Ульмус':
            await bot.send_photo(message.chat.id, images.ulmus)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[29]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[29]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[29]['Фракция'] + '\n' + heroes.heroesFullInfo[29]['Роль'])
        elif message.text =='Сейрус':
            await bot.send_photo(message.chat.id, images.seirus)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[30]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[30]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[30]['Фракция'] + '\n' + heroes.heroesFullInfo[30]['Роль'])
        elif message.text =='Эйрон':
            await bot.send_photo(message.chat.id, images.eiron)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[31]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[31]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[31]['Фракция'] + '\n' + heroes.heroesFullInfo[31]['Роль'])
        elif message.text =='Горво':
            await bot.send_photo(message.chat.id, images.gorvo)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[32]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[32]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[32]['Фракция'] + '\n' + heroes.heroesFullInfo[32]['Роль'])
        elif message.text =='Лорсан':
            await bot.send_photo(message.chat.id, images.lorsan)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[33]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[33]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[33]['Фракция'] + '\n' + heroes.heroesFullInfo[33]['Роль'])
        elif message.text =='Саурус':
            await bot.send_photo(message.chat.id, images.saurus)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[34]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[34]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[34]['Фракция'] + '\n' + heroes.heroesFullInfo[34]['Роль'])
        elif message.text =='Солиса':
            await bot.send_photo(message.chat.id, images.solisa)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[35]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[35]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[35]['Фракция'] + '\n' + heroes.heroesFullInfo[35]['Роль'])

        #Фракция Могилорождённые

        elif message.text =='Грежул':
            await bot.send_photo(message.chat.id, images.grejul)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[36]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[36]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[36]['Фракция'] + '\n' + heroes.heroesFullInfo[36]['Роль'])
        elif message.text =='Шемира':
            await bot.send_photo(message.chat.id, images.shemira)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[37]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[37]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[37]['Фракция'] + '\n' + heroes.heroesFullInfo[37]['Роль'])
        elif message.text =='Торан':
            await bot.send_photo(message.chat.id, images.toran)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[38]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[38]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[38]['Фракция'] + '\n' + heroes.heroesFullInfo[38]['Роль'])
        elif message.text =='Изабелла':
            await bot.send_photo(message.chat.id, images.izabella)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[39]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[39]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[39]['Фракция'] + '\n' + heroes.heroesFullInfo[39]['Роль'])
        elif message.text =='Нара':
            await bot.send_photo(message.chat.id, images.nara)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[40]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[40]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[40]['Фракция'] + '\n' + heroes.heroesFullInfo[40]['Роль'])
        elif message.text =='Фераэль':
            await bot.send_photo(message.chat.id, images.ferael)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[41]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[41]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[41]['Фракция'] + '\n' + heroes.heroesFullInfo[41]['Роль'])
        elif message.text =='Баден':
            await bot.send_photo(message.chat.id, images.baden)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[42]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[42]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[42]['Фракция'] + '\n' + heroes.heroesFullInfo[42]['Роль'])
        elif message.text =='Кельтур':
            await bot.send_photo(message.chat.id, images.keltur)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[43]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[43]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[43]['Фракция'] + '\n' + heroes.heroesFullInfo[43]['Роль'])
        elif message.text =='Оден':
            await bot.send_photo(message.chat.id, images.oden)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[44]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[44]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[44]['Фракция'] + '\n' + heroes.heroesFullInfo[44]['Роль'])
        elif message.text =='Изольд':
            await bot.send_photo(message.chat.id, images.izold)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[45]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[45]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[45]['Фракция'] + '\n' + heroes.heroesFullInfo[45]['Роль'])
        elif message.text =='Торн':
            await bot.send_photo(message.chat.id, images.torn)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[46]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[46]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[46]['Фракция'] + '\n' + heroes.heroesFullInfo[46]['Роль'])
        elif message.text =='Дэймон':
            await bot.send_photo(message.chat.id, images.deimon)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[47]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[47]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[47]['Фракция'] + '\n' + heroes.heroesFullInfo[47]['Роль'])

        #Фракция Небожители

        elif message.text =='Аталия':
            await bot.send_photo(message.chat.id, images.atalia)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[48]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[48]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[48]['Фракция'] + '\n' + heroes.heroesFullInfo[48]['Роль'])
        elif message.text =='Илия и Лейла':
            await bot.send_photo(message.chat.id, images.ilia)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[49]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[49]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[49]['Фракция'] + '\n' + heroes.heroesFullInfo[49]['Роль'])
        elif message.text =='Ортус':
            await bot.send_photo(message.chat.id, images.ortus)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[50]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[50]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[50]['Фракция'] + '\n' + heroes.heroesFullInfo[50]['Роль'])
        elif message.text =='Талена':
            await bot.send_photo(message.chat.id, images.talena)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[51]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[51]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[51]['Фракция'] + '\n' + heroes.heroesFullInfo[51]['Роль'])
        elif message.text =='У-Кун':
            await bot.send_photo(message.chat.id, images.kong)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[52]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[52]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[52]['Фракция'] + '\n' + heroes.heroesFullInfo[52]['Роль'])
        elif message.text =='Флора':
            await bot.send_photo(message.chat.id, images.flora)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[53]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[53]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[53]['Фракция'] + '\n' + heroes.heroesFullInfo[53]['Роль'])

        #Фракция Подземные жители

        elif message.text =='Эзиж':
            await bot.send_photo(message.chat.id, images.ezij)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[54]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[54]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[54]['Фракция'] + '\n' + heroes.heroesFullInfo[54]['Роль'])
        elif message.text =='Мегира':
            await bot.send_photo(message.chat.id, images.megira)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[55]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[55]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[55]['Фракция'] + '\n' + heroes.heroesFullInfo[55]['Роль'])
        elif message.text =='Золрат':
            await bot.send_photo(message.chat.id, images.zolrat)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[56]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[56]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[56]['Фракция'] + '\n' + heroes.heroesFullInfo[56]['Роль'])
        elif message.text =='Хазард':
            await bot.send_photo(message.chat.id, images.hazard)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[57]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[57]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[57]['Фракция'] + '\n' + heroes.heroesFullInfo[57]['Роль'])
        elif message.text =='Мезот':
            await bot.send_photo(message.chat.id, images.mezot)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[58]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[58]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[58]['Фракция'] + '\n' + heroes.heroesFullInfo[58]['Роль'])

        #Фракция Герои из других измерений

        elif message.text =='Артур':
            await bot.send_photo(message.chat.id, images.artur)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[59]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[59]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[59]['Фракция'] + '\n' + heroes.heroesFullInfo[59]['Роль'])
        elif message.text =='Укио':
            await bot.send_photo(message.chat.id, images.ukio)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[60]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[60]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[60]['Фракция'] + '\n' + heroes.heroesFullInfo[60]['Роль'])
        elif message.text =='Накоруру':
            await bot.send_photo(message.chat.id, images.nakoruru)
            await bot.send_message(message.chat.id, "Имя: " + heroes.heroesFullInfo[61]['Имя'] + '\n' + "Роль в команде: " + heroes.heroesFullInfo[61]['РвК'] + '\n' + "Фракция: " + heroes.heroesFullInfo[61]['Фракция'] + '\n' + heroes.heroesFullInfo[61]['Роль'])

        #Полезная информация

        elif message.text == 'Полезная информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
            item1 = types.KeyboardButton("Начало игры")
            item2 = types.KeyboardButton("Тир лист героев")
            item3 = types.KeyboardButton("Коды возмещения")
            markup.add(item1, item2, item3)
            await bot.send_message(message.chat.id, "Полезная информация", parse_mode = 'html', reply_markup = markup)

        elif message.text == 'Начало игры':
            await bot.send_message(message.chat.id, "Что нужно делать в начале игры?")
        elif message.text == 'Тир лист героев':
            await bot.send_message(message.chat.id, "Тир лист героев")
        elif message.text == 'Коды возмещения':
            await bot.send_message(message.chat.id, "Последний код возмещения")

        #Связки героев

        elif message.text == 'Связки героев':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
            item1 = types.KeyboardButton("Классика v.2")
            item2 = types.KeyboardButton("Светлая сторона")
            item3 = types.KeyboardButton("Грубая сила и Изящность")
            item4 = types.KeyboardButton("Торговец в лесу")
            item5 = types.KeyboardButton("На хрупких плечах")
            back = types.KeyboardButton("Назад")
            markup.add(item1, item2, item3, item4, item5, back)
            await bot.send_message(message.chat.id, "Список связок", parse_mode = 'html', reply_markup = markup)

        elif message.text == 'Классика v.2':
            await bot.send_message(message.chat.id, "Брутус, Лика, Тази, Фераэль, Немора")
        elif message.text == 'Светлая сторона':
            await bot.send_message(message.chat.id, "Люций, Эстрильда, Белинда, Рован, Розалина")
        elif message.text == 'Грубая сила и Изящность':
            await bot.send_message(message.chat.id, "Брутус, Лика, Сафия, Эйрон, Тази")
        elif message.text == 'Торговец в лесу':
            await bot.send_message(message.chat.id, "Тази, Рован, Лика, Эйрон, Немора")
        elif message.text == 'На хрупких плечах':
            await bot.send_message(message.chat.id, "Артур, Рован, Розалина, Гвинет, Фокс")

        elif message.text =='Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
            item1 = types.KeyboardButton("Список героев")
            item2 = types.KeyboardButton("Полезная информация")
            item3 = types.KeyboardButton("Связки героев")
            markup.add(item1, item2, item3)
            await bot.send_message(message.chat.id, "Меню", parse_mode = 'html', reply_markup = markup)

        else:
            await bot.send_message(message.chat.id, 'Я не знаю как на это ответить(')

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
