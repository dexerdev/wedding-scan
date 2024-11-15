from app.app import db,datetime

class MCode(db.Model):
    __tablename__ = "m_code"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50))
    useflag = db.Column(db.Boolean)
    reward = db.Column(db.String(100))

class TRegister(db.Model):
    __tablename__ = "t_register"
    register_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(100))
    table_no = db.Column(db.String(50))
    register_date = db.Column(db.DateTime)
    code = db.Column(db.String(50))
    receive_date = db.Column(db.DateTime)
    status = db.Column(db.String(10))
