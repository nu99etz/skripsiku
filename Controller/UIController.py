from flask import Flask, request, jsonify
from app import app, db

@app.route('/login-ui', methods=['GET'])
def LoginUI():
    form = []
    button = []
    form = [
        {
            "type" : "text",
            "id" : "username",
            "name" : "username",
            "placeholder" : "Username"
        },
        {
            "type": "password",
            "id": "password",
            "name": "password",
            "placeholder": "Password"
        }
    ]

    button = [
        {
            "color" : "primary",
            "name" : "login",
            "id" : "login",
            "placeholder" : "Login"
        }
    ]

    return {
        "Form" : form,
        "Button" : button,
        "Status" : 200
    }

@app.route('/regiser-ui', methods=['GET'])
def RegisterUI():
    form = []
    button = []
    form = [
        {
            "type": "text",
            "id": "username",
            "name": "username",
            "placeholder": "Username"
        },
        {
            "type": "password",
            "id": "password",
            "name": "password",
            "placeholder": "Password"
        }
    ]

    button = [
        {
            "color": "primary",
            "name": "register",
            "id": "register",
            "placeholder": "Register"
        }
    ]

    return {
        "Form": form,
        "Button": button,
        "Status": 200
    }

