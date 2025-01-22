from config import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(50), primary_key=True)
    pseudo = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "username": self.username,
            "lastName": self.last_name,
            "firstName": self.first_name,
            "email": self.email,
            "pseudo": self.pseudo
        }
    
    def to_dict_min(self):
        return {
            "username": self.username,
            "pseudo": self.pseudo
        }
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
