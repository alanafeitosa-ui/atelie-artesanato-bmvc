from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login")
def login():
    #rota provisória -sem lógica de autenticação ainda
    return "Página de login em construção"
if __name__ == "__main__":
    app.run(debug=True)