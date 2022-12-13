from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# si no especifiquem res al decorator, és el mètode GET
@app.route('/formulari')
def formulari_get():
    # mostrem el formulari
    return """
<form method='post'>
Introdueix el teu nom:
<input name='nom' type='text' />
<br>
<input type='submit'>
</form>
"""

# important importar la request per accedir a les dades adjuntes
from flask import request

@app.route('/formulari', methods=['POST'])
def formulari_post():
    # processem les dades del formulari
    nom = request.form["nom"]
    return "Salut, {}".format(nom)


