from application import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=False)
    amount = db.Column(db.REAL)
    month = db.Column(db.String(128), index=True, unique=False)
    year = db.Column(db.Integer)		
    def __init__(self, name, amount, month,year):
        self.name = name
	self.amount = amount
	self.month = month
	self.year = year

    def __repr__(self):
        return '<Data %r%r%r%>' % self.name %self.amount %self.month %self.year
'''
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gameno = db.Column(db.String(128), index=True, unique=False)
    amount = db.Column(db.REAL)
    month = db.Column(db.String(128), index=True, unique=False)
    year = db.Column(db.Integer)		
    def __init__(self, name, amount, month,year):
        self.name = name
	self.amount = amount
	self.month = month
	self.year = year

    def __repr__(self):
        return '<Data %r%r%r%>' % self.name %self.amount %self.month %self.year

'''
