from flask import Flask, request, jsonify, make_response, session
from flask.templating import render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask import Flask, send_from_directory
from datetime import datetime

app = Flask(__name__)

@app.route('/static/assets/fonts/flaticon/font/<path:filename>')
def serve_fonts(filename):
    return send_from_directory('static/assets/fonts/flaticon/font/', filename, mimetype='font/woff')

if __name__ == "__main__":
    app.run(debug=True)
app = Flask(__name__)
CORS(app)


@app.route("/")
# @login_required
def index():
    return render_template("index.html")

@app.route("/scan_qr")
# @login_required
def scan_qr():
    return render_template("scan_qr.html")
