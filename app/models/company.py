from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True) #this field is auto incremented by default
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Company('{self.name}', '{self.email}', '{self.location}')"