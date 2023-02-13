from run import db


class Rooms(db.Model):
    number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(6), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    tenant_id = db.relationship('Tenant', backref='tenant')


class Tenants(db.Model):
    passport_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    age = db.Column(db.Integer(2), nullable=False)
    sex = db.Column(db.String(10), unique=True, nullable=False)
    # address(city, street) use nested
    # room_number = db.Column(db.Integer, db.ForegnKey('rooms.number'))


class Staff(db.Model):
    passportID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    position = db.Column(db.String(10), unique=True, nullable=False)
    salary = db.Column(db.Integer, nullable=False)



# Relationship between Room and tenants one-to-many (One tenant can book a few rooms, but one room can be booked by one tenant)
#
# Relationship between Staff and Room many-to-many (One staff can serve a few rooms, one room can be served by a few staff)


# app.app_context().push()
db.create_all()
db.session.commit()
