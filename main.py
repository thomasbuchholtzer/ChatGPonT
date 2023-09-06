from flask import Flask, render_template, request
from src.utils.ask_question_to_pdf import ask_question_to_pdf

app = Flask(__name__)


# Route pour la page d'accueil
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Accueil")


# Réponse
@app.route("/prompt", methods=["POST"])
def prompt():
    message = {}
    question = request.form["prompt"]
    message["answer"] = ask_question_to_pdf(question)[0]
    # message["answer"] = question + "coubehhh {:D"
    return message


# Question
@app.route("/question", methods=["GET"])
def ask():
    Questioncours = {}
    # Questioncours["answer"] = "Bonjour"
    Questioncours["answer"] = ask_question_to_pdf(
        "Pose-moi une question \
    sur le document suivant"
    )[0]
    return Questioncours


# Correction
@app.route("/answer", methods=["POST"])
def answer():
    donnereponse = {}
    reponse = request.form["prompt"]
    donnereponse["answer"] = ask_question_to_pdf(
        reponse
        + "ma \
    réponse est-elle juste ? Si non, quelle était la réponse ?"
    )[0]
    return donnereponse


# Formulaire
@app.route("/choose_course", methods=["GET"])
def choose_course():
    return render_template("choose_course.html")


@app.route('/new_course', methods=['POST'])
def new_course():
    message = {}
    question = request.form["prompt"]
    message["answer"] = question + "NEIN !"
    print(message)
    return message


if __name__ == '__main__':
    app.run()
