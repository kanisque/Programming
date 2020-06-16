from book import *
from author import *
class Catalog:
    bookStore = []
    authorStore = []
    uniqueCategories = set()
    def addBookToCatalog(self,bookId,title,authorId,publisher,publishDate,category,price,soldCount):
        book = Book(bookId,title,authorId,publisher,publishDate,category,price,soldCount)
        self.bookStore.append(book)
        self.uniqueCategories.add(category)
    
    def addAnAuthor(self,authorId,name,phoneNumber,birthDate,deathDate):
        author = Author(authorId,name,phoneNumber,birthDate,deathDate)
        self.authorStore.append(author)
    
    def getListOfCategories(self):
        return self.uniqueCategories
    
    def getAllAuthorName(self):
        uniqueAuthor = set()
        for author in self.authorStore:
            uniqueAuthor.add(author.name)
        return uniqueAuthor
    
    def getMostSoldBooksByAuthor(self,authorName):
        currMax = -1
        foundBook = None
        authorID = self.getAuthorIdByName(authorName)
        for book in self.bookStore:
            if book.soldCount > currMax and book.authorId == authorID:
                currMax = book.soldCount
                foundBook = book
        return foundBook

    def getMostSoldBooksByCategory(self,category):
        currMax = -1
        foundBook = None
        for book in self.bookStore:
            if book.soldCount > currMax and book.category == category:
                currMax = book.soldCount
                foundBook = book
        return foundBook

    def searchBookByTitle(self, title):
        result = []
        for book in self.bookStore:
            if title in book.title:
                result.append(book)
        return result

    def searchBookByAuthor(self, authorName):
        authorID = self.getAllPartialAuthorIdByName(authorName)
        result = []
        for book in self.bookStore:
            if book.authorId in authorID:
                result.append(book)
        return result

# Helper functions
    def getAuthorIdByName(self,authorName):
        for author in self.authorStore:
            if author.name == authorName:
                return author.authorId
        return False

    def getAllPartialAuthorIdByName(self,authorName):
        result = []
        for author in self.authorStore:
            if authorName in author.name:
                result.append(author.authorId)
        return result

def main():
    print("Running Main")
    ctlg = Catalog()
    
    ctlg.addAnAuthor("author1","JK Rowling","123456789","birth123","death123")
    ctlg.addBookToCatalog("book1","Harry Potter XYZ","author1","abc pub","pub123","Fiction","100","5000")

    print(ctlg.getAllAuthorName())
    print(ctlg.getListOfCategories())
    print(ctlg.getMostSoldBooksByAuthor("JK Rowling").title)
    print([book.title for book in ctlg.searchBookByAuthor("JK")])
    print([book.title for book in ctlg.searchBookByTitle("Pot")])

if __name__ == "__main__":    
    main()