#importation des bibleotheque

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
################################################################################################
cred = credentials.Certificate("C:\\Users\\hp\\Desktop\\application de pfe\\j.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://rfga-edea2-default-rtdb.firebaseio.com/"
})


#Création d'une référence à la base de données
ref = db.reference('Students')

data = {
    "20023991":
        {
            "name": "samiha Skhoun ",
            "major": " info",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
         "19003973":
        {
            "name": "Maryam El Hafdi",
            "major": "info",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
         "19028555":
        {
            "name": "Ikram tabek",
            "major": " info ",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)