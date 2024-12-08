class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        
        if hasattr(self, 'title'):
            raise AttributeError("Title is immutable.")
        
        self.title = title

        Article.all.append(self)
class Author:
    def __init__(self, name):
        self._name = name

    def __setattr__(self, name, value):
        if hasattr(self,'_name'):
            raise AttributeError("Name is immutable.")
        super().__setattr__(name, value)

    @property
    def name(self):
        return self._name
    
    def articles(self):
        return[artic for artic in Article.all if artic.author == self]  
    def magazines(self):
        return list(set(art.magazine for art in self.articles()))

    def add_article(self, magazine, title): 
        return Article(self,magazine,title)

    def topic_areas(self):
        if not self.articles():
            return None
        
        return list(set(article.magazine.category for article in self.articles()))

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Magazine name must be a string.")
        if not isinstance(category, str):
            raise ValueError("Magazine category must be a string.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            print(f"Invalid name assignment.=")
            return

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            print(f"Invalid category assignment.")
            return

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        articles = self.articles()
        if articles:
            return [article.title for article in articles]
        return None

    def contributing_authors(self):
        authors_count = {}
        
        for article in self.articles():
            if article.author in authors_count:
                authors_count[article.author] += 1
            else:
                authors_count[article.author] = 1
        
        contributing_authors = [author for author, count in authors_count.items() if count > 2]
        
        return contributing_authors if contributing_authors else None
