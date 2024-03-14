# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.



from flask import Flask,render_template
from models import db,Authors,Books
from faker import Faker
from random import randint,choice


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_test.db'
db.init_app(app)#Инициализируем бд
fake = Faker()


@app.route('/')
def index():
    books = Books.query.all()
    # context = {'books':books}
    return render_template('index.html',books=books)


@app.cli.command('init-db') 
def init_db():
    db.create_all() # создаем все таблицы по имеющим моделям
    print('OK')


@app.cli.command('add-authors')
def add_authors():
    for i in range(1,6):
        author_name = fake.first_name()
        author_last_name = fake.last_name()
        autr = Authors(name_author=author_name, last_name=author_last_name)
        db.session.add(autr)
    db.session.commit()

    author_ids = [1, 2, 3, 4, 5]
    for i in range(1, 6):
        book_name = fake.sentence(nb_words=choice([2,3]))
        publication_year = randint(1900, 2021)
        author_id = choice(author_ids)
        author_ids.remove(author_id)
        bk = Books(name_b=f'{book_name}', year =f'{publication_year}', 
                           copiens = i, 
                           author_id = author_id)
        db.session.add(bk)#транзакция
    db.session.commit()#Подтверждение добавления
    print('Authors add in DB!')

if __name__ == '__main__':
    app.run(debug=True)