import datetime
import flask

all_messages = []  # Список всех сообщений.


def add_message(sender, text):  # Добавить новое сообщение.
    date_time = datetime.datetime.now().strftime('%H:%M - %m.%d.%Y')
    new_message = {
        'sender': sender,
        'text': text,
        'time': date_time
    }
    all_messages.append(new_message)


def print_all_messages():  # Печатает на экран все сообщения.
    for message in all_messages:
        sender = message['sender']
        text = message['text']
        time = message['time']
        print(f'{time}\n{[sender]}: {text}')


add_message('Дима', 'Всем привет!')

print_all_messages()

