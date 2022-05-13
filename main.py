# Импортируем json и flask

import json

from flask import Flask

# открываем json файл для чтения
with open("candidates.json", "r") as file:
    candidates = json.load(file)

app = Flask(__name__)


# создаём роут "/" - это главная страница
@app.route("/")
def page_index():
    person = ""
    for i in candidates:
        name = "Имя кандидата - " + i["name"] + "\n"
        position = "Позиция кандидата: " + i["position"] + "\n"
        skills = "Навыки: " + i["skills"] + "\n"
        person += name + position + skills + "\n"
    return "<pre>" + person + "<pre>"


# создаём роут "candidates/" для поиска по id
@app.route("/candidates/<int:id>")
def user_profile(id):
    person = ""
    for i in candidates:
        if id == i["id"]:
            picture = i["picture"]
            name = "Имя кандидата - " + i["name"] + "<br />"
            position = "Позиция кандидата: " + i["position"] + "<br />"
            skills = "Навыки: " + i["skills"] + "<br />"
            person += name + position + skills + "<br />"

            return f"<img src= {picture}> <br /> </pre>{person}</pre>"


# создаём роут "candidates/" для поиска по навыкам
@app.route("/skills/<skill>")
def user_skill(skill):
    person = ""
    for i in candidates:
        for s in i["skills"].split(", "):
            if s.lower() == skill:
                name = "Имя кандидата - " + i["name"] + "\n"
                position = "Позиция кандидата: " + i["position"] + "\n"
                skills = "Навыки: " + i["skills"] + "\n"
                person += name + position + skills + "\n"
    return "<pre>" + person + "<pre>"


app.run()
