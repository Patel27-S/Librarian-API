# Librarian-API

A Librarian's API, as the title suggests, is created to help a Librarian who wants to keep the record of the incoming books in the Library, track the authors of those books, and create entries by entering the book and its corresponding authors when a new book is received.

We are helping the Librarian, in the best way possible by Defining the Database Relationship after listening to his problem, and then creating API endpoints using Django REST Framework so well, that he'd be taken care of, for all of his library proper classification of authors', books' and entries' issues.

We've created endpoints so that the Librarian of our town will be able to :-

- Add New Books to the Database. (He doesn't need to worry about duplicating the same book while entering, as we've written the Logic in the CreateAPI endpoint for that to not happen)..
- Add New Authors to the Database. (Again, No worries for the Librarian as the code won't allow any more than one time entries of the same author in the Database).
- Create Entries for new books that becomes a part of the Library books family.
- List Books, List Authors, List the Entries and also filter them on the whatever basis he wants, for e.g. Category of books, First Name of the Authors etc.
- Delete Books, Authors that are no more now a part of the Library Stock, and the corresponding Entries will be automatically deleted. (As, Books and Authors are Foreign Keys of the Entries' table in Database).


### TO DO :-
- We'll create a strong authentication system yet to make sure that no one other than the Librarian has the access to the Database of Library ;)
- Dockerize the API app and write steps eventually, to have the project run without any hassle on any machine with Docker installed. AT the end ;);) 

