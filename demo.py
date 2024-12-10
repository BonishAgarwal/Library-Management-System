from books import Book
from category import Category
from library_service import LibraryService
from users import User


def main():

    library_service = LibraryService()
    library_service1 = LibraryService()
    
    print(library_service)
    print(library_service1)
    
    
    user1 = User("1", "bonish", "123456")
    user2 = User("2", "tanuja", "123456")
    user3 = User("3", "pravin", "123456")
    
    library_service.add_users(user1)
    library_service.add_users(user2)
    library_service.add_users(user3)
    
    book1 = Book("1", "Book1", Category.FICTION)
    book2 = Book("2", "Book2", Category.SCIENCE)
    book3 = Book("3", "Book3", Category.GENERAL_KNOWLEDGE)
    
    library_service.add_books(book1)
    library_service.add_books(book2)
    library_service.add_books(book3)
    
    library_service.assign_book(book1, user1)
    library_service.assign_book(book2, user2)
    library_service.assign_book(book3, user1)
    
    books_assigened_to_user = library_service.get_books_assigned_to_user(user1)
    print(books_assigened_to_user)
    
    library_service.unassign_book(book1.get_book_id(), user1)
    
    books_assigened_to_user = library_service.get_books_assigned_to_user(user1)
    print(books_assigened_to_user)
    

if __name__ == "__main__":
    main()