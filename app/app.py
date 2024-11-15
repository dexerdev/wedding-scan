from flask import Flask, request, jsonify, make_response, session
from flask.templating import render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask import Flask, send_from_directory
from datetime import datetime
from app.configs import *
import qrcode
import os


app = Flask(__name__)


@app.route("/static/assets/fonts/flaticon/font/<path:filename>")
def serve_fonts(filename):
    return send_from_directory(
        "static/assets/fonts/flaticon/font/", filename, mimetype="font/woff"
    )


app.config["JSON_SORT_KEYS"] = False
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = ConStr

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

from .con_sqlalchemy import *
from .ma_sqlalchemy import *


@app.route("/")
# @login_required
def index():
    return render_template("index.html")


@app.route("/scan_qr")
# @login_required
def scan_qr():
    return render_template("scan_qr.html")


@app.route("/api/register_reward", methods=["POST"])
def register_reward():
    try:
        name = request.json.get("name")
        phone = request.json.get("phone")
        table_no = request.json.get("table_no")
        register_date = datetime.now()
        status = "N"
        table_no = table_no.upper()
        
        vip_list = ["VIP1", "VIP2", "VIP3", "VIP4", "VIP5"]
        table_list = [
            "TABLE1",
            "TABLE2",
            "TABLE3",
            "TABLE4",
            "TABLE5",
            "TABLE6",
            "TABLE7",
            "TABLE8",
            "TABLE9",
            "TABLE10",
            "TABLE11",
            "TABLE12",
            "TABLE13",
            "TABLE14",
            "TABLE15",
            "TABLE16",
            "TABLE17",
            "TABLE18",
            "TABLE19",
            "TABLE20",
        ]
        if table_no not in vip_list:
            if table_no not in table_list:
                return jsonify(
                    {"data": "", "message": "เลขโต๊ะไม่ถูกต้อง", "success": False}
                )
        valid, msg = validate_data(phone, table_no)
        if valid == False:
                return jsonify({"data": "", "message": msg, "success": False})
        code = get_code()
        if code == "":
            return jsonify(
                {"data": "", "message": "ขอภัยของรางวัลหมดแล้ว", "success": False}
            )
        else:
            # generate qrcode
            path = generate_qrcode(code)
            register = TRegister(
                name=name,
                phone=phone,
                table_no=table_no.upper(),
                register_date=register_date,
                code=code,
                status=status,
            )
            db.session.add(register)
            db.session.commit()
            return jsonify(
                {
                    "data": {"qr_code_path": path},
                    "message": "ยินดีด้วยคุณได้รับของรางวัล",
                    "success": True,
                }
            )
    except Exception as e:
        print(str(e))
        raise e


def get_code():
    try:
        res = ""
        query = MCode.query.filter(MCode.useflag == False).first()
        if query != None:
            res = query.code
            query.useflag = True
            db.session.commit()
        return res
    except Exception as e:
        print(str(e))
        raise e


def generate_qrcode(code):
    try:
        qr_directory = "app/static/qr_codes"
        os.makedirs(qr_directory, exist_ok=True)

        # Generate the QR code image
        img = qrcode.make(code)

        # Define the file path with a unique name
        file_name = f"{code}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        file_path = os.path.join(qr_directory, file_name)

        # Save the image
        img.save(file_path)
        return file_path
    except Exception as e:
        print(str(e))


def validate_data(phone, table_no):
    try:
        table_no = table_no.upper()
        data = TRegister.query.filter(TRegister.table_no == table_no).first()
        if data != None:
            return False, "เลขโต๊ะของคุณได้รับรางวัลไปแล้ว"
        data2 = TRegister.query.filter(TRegister.phone == phone).first()
        if data2 != None:
            return False, "เบอร์โทรของคุณได้รับรางวัลไปแล้ว"
        return True, ""
    except Exception as e:
        print(str(e))


@app.route("/api/check_code", methods=["POST"])
def check_code():
    try:
        code = request.json.get("code")
        data = TRegister.query.filter(TRegister.code == code).first()
        if data != None:
            if data.status == "Y":
                return jsonify(
                    {
                        "data": "",
                        "message": "คุณรับรางวัลไปแล้ว",
                        "success": False,
                    }
                )
            data.receive_date = datetime.now()
            data.status = "Y"
            db.session.commit()
            reward = MCode.query.filter(MCode.code == code).first()
            return jsonify(
                {
                    "data": reward.reward,
                    "message": "ยินดีด้วยคุณได้รับของรางวัล",
                    "success": True,
                }
            )
        else:
            return jsonify(
                {
                    "data": "",
                    "message": "ไม่พบรางวัล",
                    "success": False,
                }
            )
    except Exception as e:
        print(str(e))
        db.session.rollback()
        raise e
