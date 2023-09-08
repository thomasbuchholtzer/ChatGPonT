import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from src.utils.ask_question_to_pdf import ask_question_to_pdf


curfilename = "pates.txt"


def change_chosen_course(newname):
    global curfilename
    curfilename = newname
    return 0


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
    message["answer"] = ask_question_to_pdf(question, curfilename)[0]
    # message["answer"] = question + "coubehhh {:D"
    return message


# Question
@app.route("/question", methods=["GET"])
def ask():
    Questioncours = {}
    # Questioncours["answer"] = "Bonjour"
    Questioncours["answer"] = ask_question_to_pdf(
        "Pose-moi une question sur le document suivant", curfilename
    )[0]
    return Questioncours


# Correction
@app.route("/answer", methods=["POST"])
def answer():
    donnereponse = {}
    reponse = request.form["prompt"]
    donnereponse["answer"] = ask_question_to_pdf(
        reponse + "ma réponse est-elle juste ? \
        Si non, quelle était la réponse ?", curfilename
    )[0]
    return donnereponse


# Formulaire
@app.route("/choose_course", methods=["GET"])
def choose_course():
    return render_template("choose_course.html")

# Code borrowed from :
# https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf'}
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/new_course", methods=["POST"])
def new_course():
    # Reload webpage if no file uploaded
    if 'file' not in request.files:
        return render_template("choose_course.html", title="Accueil")
    UPLOAD_FOLDER = 'src/utils/courses'
    file = request.files['file']
    if file.filename == '':
        return render_template("choose_course.html", title="Accueil")
    # Upload valid file
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER,
                               filename))
        change_chosen_course(filename)
        # URL redirect to index page
        return redirect("/")


if __name__ == "__main__":
    app.run()
