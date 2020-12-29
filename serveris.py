from flask import Flask


app = Flask(__name__)#ģenerē aplikāciju


@app.route('/')#ceļš uz adresēm
def index0():#funkcijas nosaukums
  return "Labrīt!*"

@app.route('/sveiki')
def index1():
  return "Nav vairs nekāds rīts!"
@app.route('/sveiki/<vards>')#ja nav statisks liek <> zīmēs
def index2(vards):#parametrs mainīgais

  return f"Sveiki {vards}"#"Sveiki{}".format(vards)

@app.route('/cik/<sk1>/<sk2>')#ja nav statisks liek <> zīmēs
def reizi(sk1,sk2):#parametrs mainīgais
  #var sk1=int(sk1)
  return str(int(sk1)*int(sk2))

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)#resartē web serveri šīs ir pēdējās rindiņas vienmēr
