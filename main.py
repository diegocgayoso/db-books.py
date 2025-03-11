from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# Criar banco de dados

db = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# Criar tabelas
class User(Base):
    #criar nome da table
    __tablename__ = "users"
    #criar colunas da table
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(50))
    email = Column("email", String(50))
    password = Column("password", String(50))
    active = Column("active", Boolean)

    def __init__(self, name, email, password, active=True):
        self.name = name
        self.email = email
        self.password = password
        self.active = active

class Book(Base):
    __tablename__ = "books"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("ttile", String(50))
    author = Column("author", String(50))
    year = Column("year", Integer)
    user_id = Column("user_id",Integer, ForeignKey("users.id"))
    # user = relationship("User", backref="books")
    
    def __init__(self, title, author, year, user_id):
        self.title = title
        self.author = author
        self.year = year
        self.user_id = user_id


Base.metadata.create_all(bind=db)

#Add user 
user = User("Carlos", "carlos@gmail.com", "123456")
session.add(user)
session.commit()

#Read users
list_users = session.query(User).all()
print(list_users)


#Add book
# book = Book("O Senhor dos Anéis", "JRR Tolkien", 1954, 1)
# session.add(book)
# session.commit()    