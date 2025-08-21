from flask import Flask, redirect, url_for, render_template, request
#import requests
from flask_restful import Resource, Api
import weather_utils

app = Flask(__name__)
api = Api(app)

@app.route("/", methods=["POST", "GET"])
def home():
    try:
        if request.method == "POST":
            user = request.form.get("nm")
            if user == "":
                return render_template("home.html")
            data = weather_utils.weather(str(user))
            return render_template("home.html", **data)
        else:
            return render_template("home.html")
    except TypeError:
        return render_template("home.html", message="cette ville n'existe pas ou elle est mal ortographié")
    except KeyError:
        print("cette ville n'existe pas ou elle est mal ortographié")

class Temperature(Resource):
    def get(self):
        try:
            city = request.args.get('city')
            data = weather_utils.weather(city)
            return data
        except:
            return "error"

api.add_resource(Temperature, '/city')

if __name__ == '__main__':
    app.run(debug=True)
