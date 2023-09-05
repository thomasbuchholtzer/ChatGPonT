from flask import Flask, render_template, request
from src.utils.ask_question_to_pdf import ask_question_to_pdf

app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Accueil')

# Réponse
@app.route('/prompt', methods=['POST'])
def prompt():
    message = {}
    question = request.form['prompt'] 
    message['answer'] = ask_question_to_pdf(question)[0]
    # message['answer'] = question + "coubehhh {:D"
    return message

<<<<<<< HEAD
@app.route('/question', methods=['GET'])
def ask():
    Questioncours = {}
    Questioncours['answer'] = "Bonjour"
    return Questioncours
=======
# Question
>>>>>>> 2cf716b8f6630e1b6660134e8410b8be138f57a0

if __name__ == '__main__':
    app.run()
