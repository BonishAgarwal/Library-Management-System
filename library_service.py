from typing import Dict, List
from books import Book
from users import User


class LibraryService:
    
    _instance = None
    
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.users: Dict[str, User] = {}
        if LibraryService._instance is not None:
            LibraryService._instance = self
        
        return LibraryService._instance

    def add_users(self, user: User):
        self.users[user.get_user_id()] = user
    
    def add_books(self, book: Book):
        self.books[book.get_book_id()] = book

    def remove_book(self, book_id: str):
        del self.books[book_id]
    
    def assign_book(self, book: Book, user: User):
        if book.is_book_available() and user.get_number_of_issued_books() < 5:
            book.assign_user(user.get_user_id())
            
            user.add_books(book)
        else:
            return "Book is either not available or you have issues more than 5 books"
    
    def unassign_book(self, book_id: int, user: User):
        if user.issued_books[book_id]:
            book = self.books[book_id]
            book.unassign_user()
            
            user.remove_from_issued_books(book_id)
    
    def get_books_assigned_to_user(self, user: User):
        return user.get_issues_by_books()