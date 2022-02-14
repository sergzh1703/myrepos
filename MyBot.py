import random
import telebot

token = '...'
bot = telebot.TeleBot(token)
my_name = "Sergey"

HELP = """
/help - список доступных команд
/add - добавить задачу,
/show - показать все добавленные задачи,
/random - добавить случайную задачу на сегодня
"""
RANDOM_TASKS = [{'записаться на курсы':'учеба'},{'покормить кошку':'домашние дела'}, {'отпавить письмо':'работа'}]
tasks = {}
task = ''
date = ''
category = ''


def add_todo(date,task,category):
    if date in tasks:
        tasks[date].append({task: category})
    else:
        tasks[date] = []
        tasks[date].append({task: category})
    return f'задача {task} добавлена на дату {date} c категорией {category}!'

@bot.message_handler(commands=['help'])
# слушает команду указанную в commands. Команда вводится в строке Телеги вида: /команда
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['show','print'])
def show(message):
    commands = message.text.split()[1:]
    bot_text = ''
    for date in commands:
        bot_text = bot_text + date.upper()+'\n'
        if date.lower() in tasks:
            for task in tasks[date.lower()]:
                bot_text = bot_text + f'{list(task.keys())[0]} @{list(task.values())[0]}\n'
        else:
            bot_text = bot_text + f'Задач на дату {date.upper()} нет\n'
    bot.send_message(message.chat.id, bot_text)

@bot.message_handler(commands=['random'])
def random_add(message):
    date = 'сегодня'
    task = random.choice(RANDOM_TASKS)
    text = add_todo(date, list(task.keys())[0], list(task.values())[0])
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    global date, task
    date = command[1].lower()
    task = command[2]
    if len(task) < 3:
        text = f'Задание {task} слишком короткое.\nДолжно быть длиннее З-ех символов'
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, f'Хотите добавить категория для задания {task}')
        bot.register_next_step_handler(message, get_task_category);

@bot.message_handler(content_types=['text'])
def get_task_category(message):
    if message.text == 'да':
        bot.send_message(message.chat.id, "Введите категорию")
        bot.register_next_step_handler(message, set_task_category);
    else:
        category = 'Общая задача'
        bot_text = add_todo(date, task, category)
        bot.send_message(message.chat.id, bot_text)

@bot.message_handler(content_types=['text'])
def set_task_category(message):
    global date, task, metrik
    metrik = message.text
    bot_text = add_todo(date, task, metrik)
    bot.send_message(message.chat.id, bot_text)

bot.polling(none_stop = True)
