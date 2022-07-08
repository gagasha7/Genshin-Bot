from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types

api_token = "1877307812:AAGSAzJ--HDl6Vdf9Nx2HCNa_KTzOfOclsQ" # токен бота 

bot = Bot(token=api_token)
dp = Dispatcher(bot)


def follcheck():
 subLink1 = InlineKeyboardButton(text = "Подписаться на первый канал", url="https://t.me/+pTEW1TsnCx02NDIy")
 subLink2 = InlineKeyboardButton(text = "Подписаться на второй канал", url="https://t.me/+yaGVu1ZJxf9lZWQ6")
 subLink3 = InlineKeyboardButton(text = "Подписаться на третий канал", url="https://t.me/+b_L007v2NOk2MTAy")
 subLink4 = InlineKeyboardButton(text = "Подписаться на четвертый канал", url="https://t.me/+paI3vAmyx-c3OGZi")
 subLink5 = InlineKeyboardButton(text = "Подписаться на пятый канал", url="https://t.me/+w2L4xNWp_0MyYmYy")
 subCheck = InlineKeyboardButton(text="Продолжить", callback_data="subcheck")
 subMenu.add(subLink1, subLink2, subLink3, subLink4, subLink5, subCheck)

 subCheck = InlineKeyboardButton(text="Продолжить", callback_data="subcheck")
 subMenu.add(subLink,subCheck)
 return subMenu

promoMenu = InlineKeyboardMarkup(row_width=1)
btnPromo = InlineKeyboardButton(text="Получить промокоды", callback_data='getpromo')
promoMenu.add(btnPromo)

def checkuser(user_id):
  f = open('userlist.txt','r', encoding = "utf-8")
  userlist = f.read().split('\n')
  f.close()
  for user in userlist:
    if str(user) == str(user_id):
      return True
  return False

def newuser(user_id):
  f = open('userlist.txt','a', encoding = "utf-8")
  userlist = f.write(str(user_id) + '\n')
  f.close()



async def followcheck(uid):
 stts = await bot.get_chat_member(chat_id="-1001376477909", user_id=uid)
 if stts['status'] != "left":
  return True
 else:
  return False 

async def followmsg(uid):
 await bot.send_message(uid, 'Привет, друг! Этот бот собрал все рабочие промокоды Genshin Impact. Чтобы получить список промокодов подпишись на канал(ы) и нажми на кнопку снизу"', reply_markup=follcheck(), parse_mode="Markdown")


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
  if checkuser(message.from_user.id) == False:
    newuser(message.from_user.id)
  if await followcheck(message.from_user.id) == True:
    await bot.send_message(message.from_user.id, f'Здравствуй, {message.from_user.first_name}. Здесь ты можешь получить промокоды для *Genshin Impact*. Просто нажми на *Получить промокоды*', reply_markup=promoMenu, parse_mode="Markdown")
  else:
    await followmsg(message.from_user.id)



@dp.callback_query_handler(text="subcheck")
async def checksub(call: types.CallbackQuery):
 if await followcheck(call.from_user.id) is True:
  await bot.delete_message(call.from_user.id, call.message.message_id)
  await bot.send_message(call.from_user.id, 'Вы успешно подписались ,чтобы получить список промокодов напишите /start')
  #await bot.send_message(call.message.message_id, f'Здравствуй. Здесь ты можешь получить промокоды для *Genshin Impact*. Просто нажми на *Получить промокоды*', reply_markup=promoMenu, parse_mode="Markdown")
 else:
  await bot.answer_callback_query(callback_query_id=call.id, text="🚫 ОШИБКА! Ты не подписан на канал(ы)Чтобы получить ПРИМОГЕМЫ подпишись", show_alert=False)


@dp.callback_query_handler(text="getpromo")
async def checksub(call: types.CallbackQuery):
 if await followcheck(call.from_user.id) == True:
  await bot.send_message(call.from_user.id, '🔥НАЙДЕНО 8 100% РАБОЧИХ ПРОМОКОДА СУММАРНО НА 590 ПРИМОГЕМОВ. \n  \nDTNVKAWBWSF5 – 100 камней истока, 10 волшебной руды усиления. \n WANVJAFAXTER – 100 камней истока, 5 опыта героя.\n HA6C2AFBXSZV – 100 камней истока, 50000 моры.\n MS7C3SV8DMZH – 60 камней истока, 5 опыт героя.\n ZSPDKSC3V8V5 – 60 камней истока и 3 опыта героя.\n 9bpcjcqghawz – 60 камней истока, 5 опыт героя. \n MTNUJBXDD72R – 60 камней истока, 5 опыт героя. \n \n РЕГИСТРИРУЙСЯ И ПОЛУЧАЙ ПРИМОГЕМЫ - https://genshindrop.com/ref/2331 \n \n Вот список всех найденных промокодов: (https://telegra.ph/AKTUALNYE-PROMOKODY-2022-04-16 ')
 else:
  await followmsg(call.from_user.id)
  
@dp.message_handler(commands=['rassilka'])
async def command_send(message: types.Message):
  if message.from_user.id == 1660899869:
    msg = message.text[10:]
    await bot.send_message(message.from_user.id, f"*Рассылка началась *\nСообщение: {msg}", parse_mode='Markdown')
    receive_users = 0
    block_users = 0
    f = open("userlist.txt", "r", encoding='utf-8')
    userlist = f.read().split('\n')
    f.close()
    for user in userlist:
      try:
        await bot.send_message(user, msg)
        receive_users += 1
      except Exception as err:
        block_users += 1
        print(err)
    await bot.send_message(message.from_user.id, f"*Рассылка была завершена *\nОтправлено: {receive_users}\nЗаблокировали бота: {block_users}", parse_mode='Markdown') 

if __name__ == "__main__":
 executor.start_polling(dp,skip_updates= True)