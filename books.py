from category import Category

class Book:
    def __init__(self, book_id: int, title: str, category: Category, user_id: str = None):
        self.book_id = book_id
        self.title = title
        self.category = category
        self.is_available = True
        self.issued_by = user_id

    def get_book_id(self):
        return self.book_id

    def get_title(self):
        return self.title

    def get_category(self):
        return self.category

    def is_book_available(self):
        return self.is_available == True

    def assign_user(self, user_id: str):
        self.issued_by = user_id
        self.is_available = False

    def unassign_user(self):
        self.issued_by = None
        self.is_available = True