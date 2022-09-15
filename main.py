from email.mime import message
from flask import Flask, request, render_template
import json
import datetime

app = Flask(__name__)  # Создаем новое приложение.

def load_chat():  # Загружаем данные чата из файла.
    with open('chat.json', 'r') as json_file:
        data = json.load(json_file)
        return data['messages']

all_messages = load_chat()  # Список всех сообщений.

def save_chat():  # Запись данных чата в файл.
    data = {'messages': all_messages}
    with open('chat.json', 'w') as json_file:
        json.dump(data, json_file)

@app.route('/chat')
def display_chat():
    return render_template('index.html')

@app.route('/')
def index_page():
    return 'Добро пожаловать \'Месенджер\'!'

@app.route('/get_messages')
def get_messages():
    return {'messages': all_messages}

@app.route('/send_message')
def send_message():
    sender = request.args['sender']
    text = request.args['text']
    add_message(sender, text)
    save_chat()
    return 'OK'

def add_message(sender, text):  # Добавить новое сообщение.
    date_time = datetime.datetime.now().strftime('%H:%M - %m.%d.%Y')
    new_message = {
        'time': date_time,
        'sender': sender,
        'text': text
    }
    all_messages.append(new_message)

app.run()  # Запускает приложение.
