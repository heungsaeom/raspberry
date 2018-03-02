import pyrebase
import RPi.GPIO as GPIO
from time import sleep
config ={
    "apiKey": "AIzaSyBF0yWiL9gb1wi-HAl1gJ4fwkhL4Awh7Vk",
    "authDomain": "test-ba51b.firebaseapp.com",
    "databaseURL": "https://test-ba51b.firebaseio.com",
    "storageBucket": "test-ba51b.appspot.com",
    }
firebase = pyrebase.initialize_app(config)
db = firebase.database()
data = {"led1": "0"}
db.child("").child().update(data)
