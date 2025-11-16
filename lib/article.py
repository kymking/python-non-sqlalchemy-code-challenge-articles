from .author import Author
from .magazine import Magazine

class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self._title = None
        self._author = None
        self._magazine = None
        
        self.title = title
        self.author = author
        self.magazine = magazine
        
        author.articles().append(self)
        magazine.articles().append(self)
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("John Kimani")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Python Programming Basics")
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError("The Code King")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Titus Mwangi")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Mobile App Development")
        self._magazine = value