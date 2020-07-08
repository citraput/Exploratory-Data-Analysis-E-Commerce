from flask import Flask, render_template, redirect, \
    jsonify, request, send_from_directory, Flask 
import requests
import mysql.connector as mc

app = Flask(__name__)

@app.route('/')
def beranda():
    return render_template('home.html')

# @app.route('/')
# def beranda():
#     return render_template('home.html')
    
if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)