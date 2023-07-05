import json
import requests
import socket
from flask import Flask

app = Flask(__name__)


class LocationInfo:
    def __init__(self, backend):
        self.backend = backend

    def get_location(self, ip_address):
        response = requests.get("https://freeipapi.com/api/json")
        data = response.json()
        return data

    def get_ip():
        response = requests.get("https://freeipapi.com/api/json").json()
        return response["ipAddress"]

    def get_ip_from_socket():
        response = requests.get("https://vg.no", stream=True)
        return response.raw._connection.sock.getsockname()


@app.route("/")
def index():
    return "API Works!"


@app.route("/ip-api")
def show_ip():
    return LocationInfo.get_ip()


@app.route("/ip-socket")
def show_socket_ip():
    return LocationInfo.get_ip_from_socket()


if __name__ == "__main__":
    app.run(debug=True, port=4200)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        print("The " + self.color + " car har " + self.mileage + " miles.")


red = Car("red", 2000)
blue = Car("blue", 3000)
