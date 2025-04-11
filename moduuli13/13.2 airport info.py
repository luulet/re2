from flask import Flask, request, Response
import json
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='sampo',
         password='luulee',
        autocommit=True,
        collation='utf8mb3_general_ci'
         )

app = Flask(__name__)
@app.route('/kentta/<ICAO>')
def search(ICAO):
    try:
        sql = f"SELECT ident, name, municipality FROM airport where ident='{ICAO}'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        tilakoodi = 200
        for rivi in tulos:
            vastaus = {
                "ICAO" : rivi[0],
                "Name" : rivi[1],
                "Municipality" : rivi[2]
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
