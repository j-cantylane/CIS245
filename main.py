#Name: Jazzmon Canty-Lane

def main():         #Main Function
    print('''Let's organize some books!''')
    menu()
    

def menu():         #Function that calls to the other functions
    books = []
    validResponse = 'AaDdLlQq'
    valid = True
    while valid:    #Begins a loop until the user specifies to quit
        print('\nA) Add a new book title')
        print('D) Delete a book title')
        print('L) List all of the book titles')
        print('Q) Quit')
        selection = input('Please select one of the above options: ')
        if selection in validResponse:
            if selection in 'Aa':       #Validates the Response
                addNewBook(books)
                valid       #Continues Loop
            elif selection in 'Dd':     #Validates Repsonse
                bookDelete(books)
                valid       #continues loop
            elif selection in 'Ll':     #Validates Response
                displayList(books)  
                valid       #continues loop
            elif selection in 'Qq':     #Validates Response
                valid = False       #Ends the Loop
                print('Happy Reading!')
        elif selection not in validResponse:
            print('\nSorry, {} is not a valid response. Please choose one of the valid menu options.\n'.format(selection))
            
def addNewBook(x):      #Function to Add a new book to the list. Take the initial list of books as its parameter
    title = input('Please enter the title of the book: ')
    x.append(title)
    print('\n Added "{}"'.format(title))

def bookDelete(x):      #Function to delete a book from the list
    title = input('Please enter the title of the book you would like to delete: ')
    if title in x:      #Validates whether or not the book is on the list
        idx = x.index(title)
        del x[idx]
        print('\n{} has been deleted from your book list'.format(title))                    
    else:               #message if book is not in list
        print('\nNote, could not remove "{}", it was not found!.'.format(title))

def displayList(x):
    if x == []:         #Validates whether or not there is anything in the list
        print('There are currently no books in your list.')
    else:               #If there are books in the list, this bit will print them
        print('\n The Books Currently In Your List Are:')
        for title in x:
            print(title)   
    
main()      #Main call to action
    
