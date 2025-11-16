class Author:
    all_authors = []

    def __init__(self, name):
        self._name = None
        self.name = name
        self._articles = []
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("John Kimani")
        if len(value) == 0:
            raise ValueError("The Code King")
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Kimani is the best coder")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        from .article import Article
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))