from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import hello_command, time_command, help_command, sum_command, yandex_command

app = ApplicationBuilder().token("5308391620:AAGjS2T84f7FeXgHiXAffP7XBzr8XU4O8xQ").build()


app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("time", time_command))


app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("yandex", yandex_command))
# app.add_handler(CommandHandler("candy", candy_command))

app.run_polling()

# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext

# def log(update: Update, context: CallbackContext):
#     file = open('db.csv', 'a')
#     file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
#     file.close()











# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# # Python is 👍
# print(emoji.emojize('Python is :red_heart:'))
# print(emoji.emojize('Python is :thumbs_up:'))

# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=5)
# for i in range(5):
#     time.sleep(1)   #Задержка таймера на 1 сек
#     bar.next()
# bar.finish()


# from isOdd import isOdd

# print(isOdd(1)) #=> true
# print(isOdd(5)) #=> true

# print(isOdd(0)) #=> false
# print(isOdd(4)) #=> false