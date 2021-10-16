
from webcalc import db

class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    oper = db.Column(db.String(3), unique=True, nullable=False)
    description = db.Column(db.String(15), nullable=False)  

    def __repr__(self) -> str:
        return f'<{self.description}>' 