from db import db

room_staff = db.Table('room_staff',
                      db.Column('staff_id', db.Integer, db.ForeignKey('table_staff.passport_id')),
                      db.Column('room_id', db.Integer, db.ForeignKey('table_room.number'))
                      )


class RoomModel(db.Model):
    __tablename__ = 'table_room'

    number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('table_tenant.passport_id'))
    staff = db.relationship('StaffModel', secondary=room_staff, backref=db.backref('rooms'))



class TenantModel(db.Model):
    __tablename__ = 'table_tenant'

    passport_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    rooms = db.relationship('RoomModel', backref='tenant', lazy=True)

class StaffModel(db.Model):
    __tablename__ = 'table_staff'

    passport_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    position = db.Column(db.String(10), nullable=False)
    salary = db.Column(db.Integer, nullable=False)





# Relationship between Staff and Room many-to-many (One staff can serve a few rooms, one rooms can be served by a few staff)



