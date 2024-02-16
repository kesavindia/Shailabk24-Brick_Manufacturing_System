'''Write a class Book with a constructor
 that can be initialized with either the book's
  title and author or just the title
  (author defaults to "Unknown").'''
class Book:
    def __init__(self,title,author="unknown"):
        self.title = title
        self.author = author
life = Book('Success')
hero = Book('Everyday Hero','Robin sharma')
print(f"Book1 is '{life.title}' and it's author is {life.author}.")
print(f"Book2 is '{hero.title}' and it's author is {hero.author}.")
