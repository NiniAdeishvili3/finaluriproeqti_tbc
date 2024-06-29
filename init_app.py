from app import db, User, Book


db.create_all()


book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", price="$3.00")
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", price="$1.50")
book3 = Book(title="1984", author="George Orwell", price="$3.00")
book4 = Book(title="Moby Dick", author="Herman Melville", price="$1.50")
book5 = Book(title="War and Peace", author="Leo Tolstoy", price="$2.00")
book6 = Book(title="Jane Eyre", author="Charlotte Bronte", price="$3.00")

db.session.add(book1)
db.session.add(book2)
db.session.add(book3)
db.session.add(book4)
db.session.add(book5)
db.session.add(book6)
db.session.commit()

print("Database initialized and initial data added.")
