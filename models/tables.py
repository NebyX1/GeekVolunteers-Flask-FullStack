from database.db import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    profile_image = db.Column(db.String(300), nullable=True)
    linkedin_url = db.Column(db.String(300), nullable=True)
    github_url = db.Column(db.String(300), nullable=True)
    skills = db.Column(db.String(500), nullable=True)
    # user_role = db.Column(db.String(20), nullable=False, default="developer")

    # def check_password(self, password_attempt):
    #     return self.password == password_attempt

    def __repr__(self):
        return '<Users %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "location": self.location,
            "bio": self.bio,
            "profile_image": self.profile_image,
            "linkedin_url": self.linkedin_url,
            "github_url": self.github_url,
            "skills": self.skills,
            "user_role": self.user_role
        }