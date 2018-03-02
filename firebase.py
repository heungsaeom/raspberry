import pyrebase
import RPi.GPIO as GPIO
from time import sleep
config ={
    "apiKey": "AIzaSyBjUucUFMKZPZ2iyES2iwYeb0AF6cx-3MU",
    "authDomain": "dieukhien-a83e2.firebaseapp.com",
    "databaseURL": "https://dieukhien-a83e2.firebaseio.com",
    "storageBucket": "dieukhien-a83e2.appspot.com",
    }
firebase = pyrebase.initialize_app(config)
db = firebase.database()
c = firebase.child('led')
data = {"led1": "0"}
db.child("").child().update(data)
