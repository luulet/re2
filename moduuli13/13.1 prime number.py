from flask import Flask, request, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        isPrime = "true"
        if int(luku) > 1:
            for i in range(2, int(luku)):
                if (int(luku) % i) == 0:
                    isPrime = "false"
        tilakoodi = 200
        vastaus = {
            "status" : tilakoodi,
            "luku" : luku,
            "isPrime" : isPrime
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status" : tilakoodi,
            "desc" : "Virheellinen luku"
        }

    jsonvastaus = json.dumps(vastaus)
    return Response(response=jsonvastaus, status=tilakoodi, mimetype="application/json")
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)