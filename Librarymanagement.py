class library:
    def __init__(self, list, Name):
        self.booklist = list
        self.name = Name
        self.lendDict = {}

    def displaybooks(self):
        print(f"We Have Following Books In our Library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Database has been Updated:\n You can take the book now")
            
        else:
            print(f"Book is already taken by {self.lendDict[book]}")

    def addbook(self, book):
        self.booklist.append(book)
        print("Book Has Been added to the Booklist")

    def returnbook(self, book):
        self.lendDict.pop(book)
        


if __name__ == "__main__":
    Abhishek = library(['1.Harry Potter and the Deathly Hallows','2.Rich Dad, Poor Dad','3.The Alchemist','4.Lord of the Rings'],"Abhishek_Library")
    
    while(True):
        print(f"Welcome To the {Abhishek.name} . Enter your choice to continue:")
        print("1.Display the Books")
        print("2.Lend a Book")
        print("3.Add a Book")
        print("4.Return the Book")
        
        user_choice = input()
        
        if user_choice not in ['1','2','3','4']:
            print("Please Enter a Valid Option !!")
            continue
        
        else:
            user_choice = int(user_choice)
        
        if user_choice==1:
            Abhishek.displaybooks()
            
        elif user_choice==2:
            book = input("Enter the Book you want to Lend: ")
            user = input("Enter your Name: ")
            Abhishek.lendbook(user,book)
        
        elif user_choice==3:
            book = input("Enter the name of the book you want to Add:")
            Abhishek.addbook(book)
        
        elif user_choice==4:
             book = input("Enter the name of the book you want to Return:")
             Abhishek.returnbook(book)
        
        else:
            print("Not a Valid Option") 
        
        print("Press c to Continue and q to Quit ")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2=='q':
                exit()
            
            elif user_choice2=='c':
                continue
            
        
        