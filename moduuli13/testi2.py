from flask import Flask, request, Response
import json

app = Flask(__name__)
@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    try:
        summa = float(luku1)+float(luku2)
        tilakoodi = 200
        vastaus = {
            "status" : tilakoodi,
            "luku1" : luku1,
            "luku2" : luku2,
            "summa" : summa
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status" : tilakoodi,
            "desc" : "virheellinen yhteenlaskettava"
        }

    jsonvastaus = json.dumps(vastaus)
    return Response(response=jsonvastaus, status=tilakoodi, mimetype="application/json")
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)