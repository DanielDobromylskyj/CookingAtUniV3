from flask import Flask
import json

recipies = json.load(open("recipes.json"))

app = Flask(__name__)


def server_html(x):
    with open(f"html/{x}.html", encoding="utf-8") as f:
        return f.read()

@app.route("/")
def home():
    return server_html("home")


@app.route("/get_recipies")
def get_recipies():
    return recipies, 200



@app.route("/recipe")
def about():
    return server_html("recipe")

if __name__ == "__main__":
    app.run(host="192.168.1.120", port=8080)
