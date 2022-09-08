class librarian:
    print("====================Welcome to Hafsa's Reading Hub========================")
    def display_books(self): #This function is used to display all the books to the user
        #print("====================Welcome to Hafsa's Reading Hub========================")
        print("===========================List of Books==================================")
        with open("List_of_Books.txt","r+") as db:
            db.seek(0)
            content=db.readlines()
        for i in content:
            print(i)


            
    def add_books(self): #This function can add as many books we want
        with open("List_of_Books.txt","a+") as ab:
            ab.seek(0)
            c=ab.readlines()
            Name_of_the_book=input("Enter the name of the book to add: ")
            key=len(c)+1
            key=str(key)
            string=key+":"+Name_of_the_book
            ab.write("\n"+string)
        print("The book has been added successfully")



        
    def remove_books(self): #This function can remove books from the list of books
        with open("List_of_Books.txt","r+") as r:
            r.seek(0)
            f=r.readlines()
        for j in f:
            print(j)
        Name_of_the_book_to_remove=input("Enter the name of the book to remove: ")
        new_lst=[]
        for book in f:
            if Name_of_the_book_to_remove in book:
                continue
            else:
                new_lst.append(book)
        with open("List_of_Books.txt","w+") as rb:
            for item in new_lst:
                rb.write(item)
        print("Book removed successfully")


                
    def register(self): #This function register the user and also can cancel the membership of any user
        print("Register the user first!")
        users=open("users.txt","a+")
        name=input("Enter the name: ")
        email=input("Enter the email: ")
        users.write("Name: "+name+" \n")
        users.write("Email: "+email+" \n")
        print()
        print("The user have been registered successfully! :)")
        print()
        with open("users.txt","r+") as r:
            r.seek(0)
            r=r.readlines()
        #for j in r:
            #print(j)
        Name_of_the_user_to_remove=input("Enter the name of the user to cancel the membership of: ")
        new_lst=[]
        for b in r:
            if Name_of_the_user_to_remove in b:
                continue
            else:
                new_lst.append(b)
        with open("users.txt","w+") as rb:
            for item in new_lst:
                rb.write(item)
        print("The membership of",Name_of_the_user_to_remove,"has been cancelled") 

                
    def reserve_book(self): #This function reserves an unavailable book for the user beforehand
        print("If you want to reserve a book which is not currently available so first you need to register yourself :)")
        users=open("users.txt","a+")
        name=input("Enter the name: ")
        email=input("Enter the email: ")
        users.write("Name: "+name+" \n")
        users.write("Email: "+email+" \n")
        print()
        print("The user have been registered successfully! :)")
        print()
        s=input("Now, you may enter the name of the book you want to reserve: ")
        print()
        print("We value your choice and will inform you when we restock",s,",till then don't worry we have reserved your book!")

        
    def renew_book(self): #This user allows the user to reborrow an already checked out book
        print("Seems like you are a familiar customer! :)")
        a=input("Enter the book you want to reborrow: ")
        print("Sorry, we had",a,"a week ago,now will inform you through your email about it's availablity. :)")
  
    def return_book(self): #This function allows the user to return the book back to the librarian
        h=input("Enter the name of the book you want to return: ")
        print("Thankyou for returning",h,"!"
              )

    def check_outbook(self): #This function FIRSTLY SEARCH THE BOOK AND THEN CHECKOUT,so basically iam implementing two functions in a single function
       print("In order to search and lending the book,register the user first!")
       users=open("users.txt","a+")
       name=input("Enter the name: ")
       email=input("Enter the email: ")
       users.write("Name: "+name+" \n")
       users.write("Email: "+email+" \n")
       print()
       print("The user have been registered successfully! :)")
       print()
       with open("users.txt","r+") as r:
           r.seek(0)
           r=r.readlines()
       fh=open("List_of_Books.txt","r")
       word=input("Enter the any word of the book you want to search and borrow: ")
       s=" "
       
       while True:
           s=fh.readline()
           L=s.split()
           if word in L:
            print("The book you want is",s)
            print("Thankyou for borrowing,Have a nice day!")
            break




    def sort_books(self): #This function sorts the books alphabetically.
         with open("List_of_Books.txt", "a+") as f:
            f.seek(0)
            content = f.readlines()
            new_lst = [ ]
            for item in content:
                item = item.split(":")
                lt = item.pop()
                new_lt = ""
                for character in lt:
                    if character == "\n":
                        continue
                    else:
                        new_lt += character
                item.append(new_lt)
                new_lst.append(item)

            alpha_list = [ ]
            for item in new_lst:
                a = item[0]
                b = item[1]
                alpha_item = [b,a]
                alpha_list.append(alpha_item)

            
            length= len(alpha_list)
            for i in range(length-1):
                for j in range(0, length-i-1):
                    if alpha_list[j] > alpha_list[j + 1] :
                        alpha_list[j], alpha_list[j + 1] = alpha_list[j + 1], alpha_list[j]



            for item in alpha_list:
                print("Book Name: ", item[0])
                print("Book ID: ", item[1])
                print()
                print("^"*80)

                

a=librarian()
print()
print('''OPTIONS:
      1)Display books
      2)Register/cancel membership of any user
      3)Check-out a book to borrow
      4)Add book
      5)Remove book
      6)Reserve a book
      7)Renew a book
      8)Return a book
      9)Sort''')
while True:
    choice=input("Now select the option user wants: ")
    if choice=="1":
        a.display_books()
    elif choice=="2":
        a.register()
    elif choice=="3":
        a.check_outbook()
    elif choice=="4":
        a.add_books()
    elif choice=="5":
        a.remove_books() 
    elif choice=="6":
        a.reserve_book()
    elif choice=="7":
        a.renew_book()
    elif choice=="8":
        a.return_book()
    elif choice=="9":
        a.sort_books()
        break
    else:
        print("Enter valid option!")
        
    










    










    









    










    










    









    










    








