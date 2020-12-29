from flask import Flask, jsonify
import dati


app = Flask(__name__)
app.config['JSON_AS_ASCII']=False#atgriež garumzīmes

@app.route('/')
def index():
  print(dati.vielas)
  return "Labrīt!"
  
@app.route('/api/v1/vielas')
def vielas():
  return jsonify(dati.vielas)#pārvērš par string

@app.route('/api/v1/viela/<vielasID>')
def viela1(vielasID):
  viela=f"Vielas ar doto id: {vielasID} nav atrasta" 
  for v in dati.vielas:
   if str(v['id'])==vielasID:# var būt arī  if v['id']==int(vielasID):
     viela=v
   return jsonify(viela)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
