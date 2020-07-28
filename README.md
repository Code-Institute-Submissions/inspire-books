# Inspire Book Repo

Welcome to Inspire were you will find Books recommended by visionaries

Inspire is a book repository where individuals can find and submit details on books that helped influence their heros, visionaries and people of renown.
The aim of the site is to show case what type of stories and knowledge impacted those who are considered paragon's in their field.

The application was created to show case the ability to use CRUD functionalities with MongoDB and Python to give users the ability to create new blog posts, edit and delete them. Allow other users to comment under them. The main application allows users to add to the database new books with person of influence that can be edited deleted and read by others.


## UX
 
## Features

I created this website with 'ease of use' as the fore most idea in implementation. Each user is able to contribute their opinion in blogs & comments section. The main feature of the website are the people and book profiles and can be easily created edited and deleted by the user.

###  User Stories

- Owner Goals

Generate interest in reading and build a strong database of books and people of influence.  
    - Side Goal with time is to create money e.g. Amazon Affiliate linking books and places to buy them.

Generate interest in learning.
    - Side Goal with having people post their 'Hero's' they can have Affiliate links to educational websites with courses in their heros field. 

Create a safe & fun place to discuss books and influencers with a blog. 
    - side goal with increase numbers to a blog is marketing.

- User Goals

Browse a variety of information on books and people that I am interested in learning about.

Discuss books that have been recommended by people and interact with them.

Add books that have influenced people that I admire.

## Wireframes

The wireframs for this project were drawn up on google drive/images

- [Front Page](https://github.com/Wonka86/inspire-books/blob/master/static/wireframes/Inspire%20Front%20Page.jpg)

- [Book Page](https://github.com/Wonka86/inspire-books/blob/c2cea96c630364fa41376b7a8d872f73b1b8499d/static/wireframes/Books%20Page.jpg)

- [People page](https://github.com/Wonka86/inspire-books/blob/c2cea96c630364fa41376b7a8d872f73b1b8499d/static/wireframes/People%20Page.jpg)

- [Submission](https://github.com/Wonka86/inspire-books/blob/c2cea96c630364fa41376b7a8d872f73b1b8499d/static/wireframes/Submission.jpg)

- [Blog](https://github.com/Wonka86/inspire-books/blob/c2cea96c630364fa41376b7a8d872f73b1b8499d/static/wireframes/Blog.jpg)


## Data Architecture
Data architecture had to be thought through before commencement. CI Tutors helped with the layout of blog data.


[Inspire Book Repo](https://github.com/Wonka86/inspire-books/blob/8f025ed314b364df76f0af6b64a9b057aeaffcb6/static/data-layout/book%20repo.png)

- [Book_title](https://github.com/Wonka86/inspire-books/blob/8f025ed314b364df76f0af6b64a9b057aeaffcb6/static/data-layout/books&people.png)

- [Categories](https://github.com/Wonka86/inspire-books/blob/8f025ed314b364df76f0af6b64a9b057aeaffcb6/static/data-layout/book%20categories.png)

- [Category](https://github.com/Wonka86/inspire-books/blob/8f025ed314b364df76f0af6b64a9b057aeaffcb6/static/data-layout/work%20categories.png)

- [Blog](https://github.com/Wonka86/inspire-books/blob/8f025ed314b364df76f0af6b64a9b057aeaffcb6/static/data-layout/blog.png)

### Existing Features

The Following features have all been implemented to help achieve the projects goals of showcasing CRUD functionalities.

- Navbar - All pages contain navigation for website and mobile allowing access to CRUD finctions. Web page Name is located on the left hand side and doubles as a retrun to home button.

- Footer - Footer contains the ability to add submissions to the database for Books and People. It also contains the ability to add to The Blog posts.

- Homepage - Highlights the featured people and books that the user will come across before continuing to acces the pages.

- People - This is where the user will find the people who are submitted along with the book submissions.

- Books - The user will find all the information on the books submitted such as title synposis and author. The ability to edit and delete are alson found here.

- Categories - Are found in both the books section and people section. The help with providing further information and will hel in future features.

- Blog - The user is able to interact with others here, add comments and delete them.

### Features Left to Implement

- Search Page - In the fuuture as the database grows i would like to add the ability to search for people and books.

- Select Category - To help find books and people in certain subjects i would like to be able to select categories and have it show only the one i select.

- Edit Comments - Currently i only have the ability to delete comments as i dont expect long conversations just yet. As the site grows this may have to be relooked at.

- Login in - Currently not implemented but as time goes on i expect this to be a feature that may have to be implemented. I dont what to do this yet as i want to encourage people to use with having to give away much information. As time goes on and the site grows this will be needed to control aspects of the site.

- Increase Business use with affiliate links and marketing - new areas on the site will need to be looked at to help with this implementation.

## Technologies Used

[HTML5](https://en.wikipedia.org/wiki/HTML5) was employed for markup text.

[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) was used to style each of the pages on the website.

[JavaScript](https://en.wikipedia.org/wiki/JavaScript) was added to improve the functionality of the website. Most Javascript on this site is required by Materialize.

[Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) Application, written in [Python]

[Materialize](https://materializecss.com/about.html) was used for its design framework. The grid system is used throughout the website.

[Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) A templating language used with python to retrieve data from the database to display on the website.

[MongoDB](https://www.mongodb.com/company) The database used to organize data from the users.

[Pymongo](https://www.w3schools.com/python/python_mongodb_getstarted.asp) The project uses PyMongo as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.

[GitHub](https://en.wikipedia.org/wiki/GitHub) was used for version control.

[Heroku](https://www.heroku.com/what) Used to deploy the final website

[Fontawesome](https://fontawesome.com/) Used for icons in blog

https://inspire-book-repo.herokuapp.com/

## Testing

Following code validators where used

[HTML](https://validator.w3.org/#validate_by_input)
[CSS](https://jigsaw.w3.org/css-validator/#validate_by_input)
[JS](https://jshint.com/)

Browser testing

This website was tested on multiple devices with varying screen sizes and in multiple browsers. All devices and web browsers passed testing.

Web browsers

- Google Chrome
- Firefox
- Edge


Devices

- iPad
- iPhone X
- Wide Screen PC
- 13" Laptop

This was tested manually over the several devices.


Manual Testing

- 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X