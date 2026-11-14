"""Goal model: a personal goal a user sets for themselves.

Stores the title, an optional description, a due date, and whether the
goal is completed, linked to the user who set it.
"""
from db import db
from datetime import datetime

class Goal(db.Model):
    __tablename__ = 'goals'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    def __init__(self, user_id, title, due_date, description=None):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False