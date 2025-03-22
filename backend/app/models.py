from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullName  = db.Column(db.String(50), unique=True, nullable=True)
    userName = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=True)
    
    # contact infos
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(100), unique=True, nullable=True)
    password = db.Column(db.String(250), nullable=False)
    adresse = db.Column(db.String(250), nullable=True)
    
    # 0 => is not confirmed yet and 1 if the user has confirmed
    isConfirmed = db.Column(db.Integer, unique=False, nullable=False, default=0)
    confirmationCode = db.Column(db.String(6), unique=True, nullable=True)

    profile_image = db.Column(db.String(255), nullable=False, default='default_profile.png')
    
    
    def to_dict(self):
        return {"id": self.id, "email": self.email}
