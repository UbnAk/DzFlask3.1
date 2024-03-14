from flask_sqlalchemy import SQLAlchemy

# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.

# Необходимо создать связь между таблицами "Книги" и "Авторы".
db = SQLAlchemy()

# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
class Authors(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name_author = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    book_ = db.relationship('Books', backref=db.backref('authors'), lazy=True)
  
    def __repr__(self):
        return f'Authors({self.name_author}, {self.last_name})'


class Books(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name_b = db.Column(db.String(50), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    copiens = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('authors.id_'))


    def __repr__(self):
        return f'Books({self.name_b}, {self.year})'
    

    