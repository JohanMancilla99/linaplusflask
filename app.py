
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def landing():
    return render_template("landing.html")

# ruta de administrador
@app.route('/admin')
def adminRoute():
    return render_template('admin/menuAdministrador.html')


if (__name__ == "__main__"):
    app.run(debug = True)