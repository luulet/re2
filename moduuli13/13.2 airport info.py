from flask import Flask, request, Response
import json

app = Flask(__name__)
@app.route('/kentta/<ICAO>')
def summa(luku):
    try:

        tilakoodi = 200
        vastaus = {
            "status" : tilakoodi,
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status" : tilakoodi,
            "desc" : "virheellinen ICAO koodi"
        }

    jsonvastaus = json.dumps(vastaus)
    return Response(response=jsonvastaus, status=tilakoodi, mimetype="application/json")
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)