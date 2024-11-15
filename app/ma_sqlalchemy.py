from app.app import ma
from marshmallow import Schema, fields


class MCodeSchema(ma.Schema):
    id = fields.Integer()
    code = fields.String()
    reward = fields.String()
    useflag = fields.Boolean()

class TRegisterSchema(ma.Schema):
    register_id = fields.Integer()
    name = fields.String()
    phone = fields.String()
    code = fields.String()
    table_no = fields.String()
    register_date = fields.DateTime()
    receive_date = fields.DateTime()
    status = fields.String()
