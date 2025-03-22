print("- Hello and Welcome to the Personal Library Manager by Muhammad Shariq!") # Welcome Message to User. Displaying the programe name and developer (my) name.


books = [] # Empty array to store the books and perform different operations like add, remove, display, search and display statistics.

while True: # Used for infinite loop to keep the program running until the user wants to exit.
    operations = input(
        "\nEnter the operation you want to perform (\n1. Add a Book, \n2. Remove a Book, \n3. Display all Books, \n4. Search for a Book, \n5. Display Statistics, \n6. Exit\n) \n- Enter Operation Number You want to Perform: "
        
        # Helps the user make a choice of operations to perform
    )

    if operations == '6': # If user chooses 6 making sure the program exits with a thank you message.
        print("Thank you for using the Personal Library Manager. Goodbye!") # Thank you message
        break # This breaks the loop and exits the program.

    if operations not in ('1', '2', '3', '4', '5'): # Checks if the user input is not in the list of operations. if not prints an error message.
        
        print("Invalid operation. Please Choose a correct operation!") # Error Message
        continue # If user input is invalid, the loop continues and asks the user to input a valid operation.

    if operations == "1": # If user chooses 1, the program will add a book to the library.
        while True:
            book = {
                "title": input("\nEnter the title of the book: "), # User input for title of book
                "author": input("\nEnter the name of the Author of the book: "), # User input for author of book
                "year": int(input("\nEnter the year of publication of the book (numbers only): ")), # User input for year of publication of book
                "genre": input("\nEnter the genre of the book: "), # User input for genre of book
                "read": input("\nHave you read this book? (Yes/No): ").lower() == "yes" # User input for read/unread of book
            }

            books.append(book) # This adds the book in the books arrays defined above.
            
            print(f"\nBook added successfully: {book['title']} by {book['author']} - ({book['year']}) - {book["genre"]} - {'Read' if book['read'] else 'Unread'}") # Prints book addition successfully message

            another = input("\nDo you want to add another book? (Yes/No): ").lower() # Asks for another book to add
            if another != "yes": 
                break # if no breaks the loop

        print(f"\nTotal Number of Books: {len(books)}") # Prints the total number of books in the array.

    elif operations == "2": # if user chooses 2, the program will remove a book from array
        
        if not books: # makes sure there is a book to remove. if not returns an error message.
            
            print("\nThere is no books to remove. Please add a book first!")
            
        else: # if there is a book runs this code
            title = input("\nEnter the title of the book you want to remove: ") # user input for title of book to remove

            for book in books: # runs a loop through array of books to check if there is a book
                if title == book["title"]: # maches the title of the book to remove
                    
                    books.remove(book) # removes the book from array
                    print(f"\nSuccessfully Removed the Book: {book["title"]} by {book["author"]}!") # prints the removal msg
                    break # breaks the loop
                
                else: # if there is no book with matching title runs this code
                    print(f"\nBook with the title: {title} cannot be found. Check the title again or add the book first.") # prints error message

        print(f"\nTotal Number of Books: {len(books)}") # Prints the total number of books in the array.

    elif operations == "3": # if user chooses 3 runs the code to display all the books in the array
        
        if not books: # makes sure there is a book to display. if not returns an error message.
            
            print("\nNo books to display. Please add some books first!")
            
        else: # if there is a book runs this code
            print("\nBooks in your collection: ")
            
            for index, book in enumerate(books, start=1): # runs a loop through array of books to display all books. the index is used to number each book and enumerate is the function used to perform this. starting the book count from 1.
                print(f"\n{index}. {book['title']} by {book['author']} - ({book['year']}) - {book["genre"]} - {'Read' if book['read'] else 'Unread'}") # prints each book present in array with their list number.

                
        print(f"\nTotal Number of Books: {len(books)}") # Prints the total number of books in the array.
        
    elif operations == "4": # if user chooses 4 runs the code to search for a book in array of books
        
        if not books:
            
            print("\n No books to search. Please add some books first!")
            
        else:
            search = input("Search by (\n1. Title, \n2. Author \n) \n - Enter Your Choice (numbers only): ") # user input for 2 operation search by title or author!

            if search not in ('1', '2'): # checks the user input if not as mentioned runs error msg
                
                print("Invalid input. Please Choose a correct input!")
                continue

            if search == "1": # if user chose 1 make the user search for title of book
                
                title = input("\nEnter the title of the book you want to search: ") # title input
                found = False  # store the status found or not found ina found variable

                for book in books: # runs lop through books array
                    
                    if title == book["title"]: # checks title of book if matches print below msg
                        
                        print(f"\nBook found: {book['title']} by {book['author']} - ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
                        found = True 
                        break  # Stop searching for book once found

                if not found:  # Check outside the loop after all books are checked
                    print(f"Book not found with the title {title}.") # prints msg if no book found

            elif search == "2": # if user chose 2 make the user search for author of book
                
                author = input("\nEnter the author of the book you want to search: ") # author input
                found = False  # store the status found or not found ina found variable

                for book in books:
                    
                    if author == book["author"]: # matches user input with book authors
                        
                        print(f"\nBook found: {book['title']} by {book['author']} - ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
                        found = True
                        break  # Stop searching once found

                if not found:  # Check outside the loop after all books are checked
                    print(f"Book not found with the author {author}.")

                        
                        
    elif operations == "5": # if user chose 5 display statistics of library.
        
        if not books: # Checks books in array
            print("\nNo books to display statistics. Please add some books first!")
            
        else: # if books found
            
            read_books = [book for book in books if book["read"]] # loops through books and checks which books are read
            unread_books = [book for book in books if not book["read"]] # loops through books and checks which books are unread
            
            print(f"\nTotal Number of Books: {len(books)}") # total no: of books
            print(f"\nTotal Number of Read Books: {len(read_books)}") # no: of read books
            print(f"\nTotal Number of Unread Books: {len(unread_books)}") # no: of unread books
            print(f"\nPercentage of Read Books: {len(read_books) / len(books) * 100}%") # percent of read books
            print(f"\nPercentage of Unread Books: {len(unread_books) / len(books) * 100}%") # percent of unread boooks
