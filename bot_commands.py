from telegram import Update
from telegram.ext import CallbackContext, MessageHandler
import datetime
from ntpath import join
import random

async def hello_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"I'll kill you {update.effective_user.first_name}!!")

async def time_command(update: Update, context: CallbackContext)-> None:
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: CallbackContext):
   await update.message.reply_text(f'/hello\n/time\n/help\n/yandex\n/candy\n')

async def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def yandex_command(update: Update, context: CallbackContext)-> None:
    await update.message.reply_html(f'https://yandex.ru/')


# async def candy_command(update: Update, context: CallbackContext):
#     All = 2021 #Количество конфет
#     Move = 28 #Максимальное количество конфет, которое можно взять 1 игроку за 1 ход

#     @bot.message_handler(content_types=['text'])
#     text = message.text.lower()
#     chat_id = message.chat.id


#     await update.message.reply_text(f'На столе лежит {All} конфета')
#     Player = ['Пользователь','Бот Василий Иванович']
#     Lottery = random.choice (Player)
#     await update.message.reply_text(f'Первым ходит: {Lottery}\n')
#     Player_2 = []
#     for i in Player:
#             if Lottery not in (i):
#                 Player_2.append (i)
#     Player_2 = ''.join(Player_2)   
#     for i in reversed (range (1, All+1)):
#         First = int()
#         if Lottery == Player[0]:
#             msg = update.message.text
#             First = int (msg)
#         else:
#             First = All % (Move+1)
#         if First == 0:
#             First = random.randint (1,28)  
#         await update.message.reply_text (f'{Lottery}: {First}')
#         while First not in range (1,Move+1):
#             await update.message.reply_text ('Введено неверное значение, введите число от 1 до 28')
#             First = int (input(f'{Lottery}: '))
#         else:
#             await update.message.reply_text ('\n',f'На столе осталось {All-First}', '\n') 
#         All = All - First
#         if All <= Move:
#             await update.message.reply_text (f'Выиграл {Player_2}, ему осталось взять {All} конфет/конфеты')
#             break
#         Second = int ()
#         if Player_2 == Player[0]:
#                 Second = int(input(f'{Player_2}: '))
#         else:
#             Second = All % (Move+1)
#         if Second == 0:
#             Second = random.randint (1,28)
#         await update.message.reply_text (f'{Player_2}: {Second}')
#         while Second not in range (1,Move+1):
#             await update.message.reply_text ('Введено неверное значение, введите число от 1 до 28')
#             Second = int (input(f'{Player_2}: '))
#         else:
#             await update.message.reply_text ('\n', f'На столе осталось {All-Second}', '\n') 
#         All = All - Second
#         if All <= Move:
#             await update.message.reply_text (f'Выиграл {Lottery}, ему осталось взять {All} конфет/конфеты')
#             break
#     await update.message.reply_text(f'gdhh')