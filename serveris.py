from flask import Flask


app = Flask(__name__)#ģenerē aplikāciju


@app.route('/')#ceļš uz adresēm
def index0():#funkcijas nosaukums
  return "Labrīt!*"

@app.route('/sveiki')
def index1():
  return "Nav vairs nekāds rīts!"
@app.route('/sveiki/<vards>')
def index2():
  return "Sveiki <vards"



if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)#resartē web serveri šīs ir pēdējās rindiņas vienmēr
