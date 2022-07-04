# Librarian-API

A Librarian's API, as the title suggests, is created to help a Librarian who wants to keep the record of the incoming books in the Library, track the authors of those books, and create entries by entering the book and its corresponding authors when a new book is received.

We are helping the Librarian, in the best way possible by Defining the Database Relationship after listening to his problem, and then creating API endpoints using Django REST Framework so well, that he'd be taken care of, for all of his library proper classification of authors', books' and entries' issues.

We've created endpoints so that the Librarian of our town will be able to :-

- Add New Books to the Database. (He doesn't need to worry about duplicating the same book while entering, as we've written the Logic in the CreateAPI endpoint for that to not happen)..
- Add New Authors to the Database. (Again, No worries for the Librarian as the code won't allow any more than one time entries of the same author in the Database).
- Create Entries for new books that becomes a part of the Library books family.
- List Books, List Authors, List the Entries and also filter them on the whatever basis he wants, for e.g. Category of books, First Name of the Authors etc.
- Delete Books, Authors that are no more now a part of the Library Stock, and the corresponding Entries will be automatically deleted. (As, Books and Authors are Foreign Keys of the Entries' table in Database).

## To Run the API in your machine 

- Please clone the repository by running "git clone https://github.com/Patel27-S/Librarian-API.git" command in a location of your machine.
- If you've Docker installed on your machine, please run "docker-compose up --build", in the same directory as the 'docker-compose.yaml' file in your machine's CLI.
- Without docker installed, please install the dependencies for this application by running "pip insall -r requirements.txt".
- Then, as being a good practice, it's always recommended to run migrations by running the commands : "python manage.py makemigrations", "python manage.py migrate".
- Note :- Without Docker, you'd want to install Postgres on your machine and configure its Username, Password details and use the same for configuring Database in the settings.py file. For SQLite, simply uncomment the part for SQLite part that has been commented and comment the Postgres Database configuration part in settings.py file.
- Run, "python manage.py runserver" to have the API running on your localhost.


## API endpoints :-

### Book API Endpoints :-
'create_book/' - To create a book instance. <br>
'list_books/' - To list all the books. <br>
'rud_book/<str:book_name>/' - To list a single book instance, update and destroy it.

### Author API Endpoints :-
'create_author/' - To create an author instance. <br>
'list_authors/' - To list all the authors. <br>
'rud_author/<int:id>/' - To list, update, destroy a single author's instance.

### Entry API Endpoints :-
'create_entry/' - To create new entries for books and its respective authors. <br>
'list_entries/' - To list all the entries. <br>
'rud_entry/<int:id>/' - To list, update and destroy an entry.


