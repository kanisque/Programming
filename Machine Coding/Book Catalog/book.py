class Book:
    def __init__(self,bookId,title,authorId,publisher,publishDate,category,price,soldCount):
        self.bookId = bookId
        self.title = title
        self.authorId = authorId
        self.publisher = publisher
        self.publishDate = publishDate
        self.category = category
        self.price = price
        self.soldCount = int(soldCount)