# Online_Library

## How to Run the API?

1. Install pip which is a reference python package manager:
   
   `python3 -m venv env`

2. Now go into your virtuall environmnet:

   `source /path to you env/bin/activate`

3. Now install pip into this virtual environment


### Home app: 

you can see a carousel of cards of the top 10 most viewed books, the books, with an image on the left and then a short text on the right, like a card. This should be visible on the website. This will be the home page.

### Books List app: 

where you can see all the books, with an image on the left and then a short text on the right, like a card. This page should have a pagination of 20 items per page. Should be visible on the website. This would be the Books page.

### Books app: 

in this there would be a format for how the book page should look like for any book, there would be an image on the top centre. Under this starting from the left like a normal text it should write the “Author” name, then a “summary” of the book, “genres” and then a “star rating” of the book out of 5, and then a button that adds the book into their card. 

### Book Logic app: 

First logic, a book can only be rented out by one person. Let's say two people add the book into their cart at the same time that is fine. But then they rent it at a one second even nano second difference, the person who rents it first gets it and the other should get a pop up that the book has already been rented out. Second Logic,  The book can only be rented out for 14 days, so this logic would have to take in the date when the user rented it and then add 14 days and then tell the user the day the books are due. Third logic, there are two things that can be done once the due date is 2 days away, it can send a pop up alert to the user that their due date to return is 2 days away in which they might return the book or ask for a one time extension for that particular book which would be an extra 7 days more. After that there can be no more extensions and the book will be automatically returned. Fourth Logic, the books can be returned at any time of the 14 days or 21 days if the user had asked for extension.

### Users app: 

Two kinds of main users, normal users who can add a book from an existing list of books to their cart and then to their dashboard on successful takeout from the library management, and they can also put a request for new books to the system. The second are the employees, within which there are two different kinds of employees, one is the normal employee who can use the CRUD operations only on books and the users. The second is the admin employee who can perform all the CRUD operations on a normal employee, books and users, so literally everything. This should not be visible on the website since this is a backend logic.

### Cart app: 

when a user adds a book into a cart, it should first check how many books are already in their dashboard, if there are 2 of them then they should give an error pop out that the user already has 2 books in their dashboard. If they have one then the cart add one more book only and then gives a pop out that now they have 2 in their cart, and then redirect the user to the cart. And obviously if there are none on the dashboard then the cart can get up to 2 books in them and then redirect them to the cart. This should be visible on the website. This would be the cart page represented by a small emoji.

### Login App: 

The login page would be a two step login page. First step is choosing if you are an “employee” or a “user”.  Both will have a simple login page where the user has to input their username and password. Only for the user on the bottom on the login page there should be an option of signing up if they don’t have an existing account. In Sign Up it should have first name, last name, email, username, password 1, password 2. Where password 1 = password2. For the user after Logging in or signing up it should redirect to the home page as for the employee it should redirect to employee dashboard This should be visible on the website. This page will be the Login page.

### Dashboard App: 

Only a user login is required. In this there will be an image on the left top, and a few details like first name and last right next to that image. Under that there would be a section which would be named “Currently renting” would be the books that were added by the user in a carousel of those two books, and below each book would be a bar to show the progress of that book till where the user has read and the due date On the right side of the image of the book would be two buttons which will be “return book” and “extend for 7 days more”. Under that section would be another section  named “Past Rentals” where there would be a list of books that the user had rented before. 

### Employee Dashboard app: 

Only an employee login is required. Over here they can see requests that have been made by users to add a new book on top, using the timestamp of the request made. In the next section there should be an operation where the employee can create new books, on top of this section there should be “Name”, “Author”,”Genres” ,”Published on”, “Short description”,”add an image of the book” sections. In the “add an image of the book” should accept jpg, jpeg, png images, And then a “add chapters” button.

### Add Chapters app: 

Once an employee clicks the “add chapters” button, they should be redirected to a page where there are two sections. One on the left and one on the right, around 20-80% of the page coverage. The left should be 20% where there would be an option to add chapters with a “+” sign and then a thin straight line next to this section. In the right section which would be 80% would have two sections. One on top which says “Add chapter name” which would take in short text. The next would be right below it, which has a small row where you can change and edit the text size, font, Bold, underline, italics etc. and below it would be where the “chapter content” goes. And on the right side below all this would be two buttons that say “save” and “publish”. The “save” button saves all the data that had been just inserted. When the “+” is clicked there will be a new section loaded on the right as the previous one gets saved. And the previous “+” would now be named as the chapter that the name it was given. And there will be a new ”+” below the current page. And the “published” will put that book into the list of books. 
