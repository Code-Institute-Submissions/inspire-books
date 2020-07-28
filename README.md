# Inspire Book Repo

Welcome to Inspire were you will find Books recommended by visionaries

Inspire is a book repository where individuals can find and submit details on books that helped influence their heros, visionaries and people of renown.
The aim of the site is to show case what type of stories and knowledge impacted those who are considered paragon's in their field.

The application was created to show case the ability to use CRUD functionalities with MongoDB and Python to give users the ability to create new blog posts, edit and delete them. Allow other users to comment under them. The main application allows users to add to the database new books with person of influence that can be edited deleted and read by others.

Website can be found at https://inspire-book-repo.herokuapp.com/

## UX
 
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

## Features

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

This was tested manually over the several devices. Upon using the mobile platfrom is when i noticed that the mobile navigation was not working. This was fixed with the correct JQuery from Materialize.


Manual Testing

- When Manually testing i started off by going through user stories

- I started withthe site user. I am drawn in by front page to see what others have submitted. I can click pictures of people and see what they have recommended. From there i can go to the book section
and have a look at the book i am interested in and links to buy. I am interested in leaving my on inspiration and decide to submit a person and book through the nav bar. I have made a mistake in the synposis i can edit the submission
and in doing so i have also changed my mind and can easily delete the submission.

Initial bug fix was updating of Jquery in the edit section so that the date of birth would show calander.

- I would like to discuss an entery to the website and go to the blog and find an interesting read along started. I want to leave a comment. Easily done with the add comment. If i change my mind i see the delete button as a trash bun and on hover the word delete.

Bug that showed up here that resonated throught the entire web site was when i accidently hit the add comment button without writing anything. This i found entered a blank comment. This got me thinking and i then realised that this was the case for all
submissions. This was easily fixed with a required field in all form inputs.

- I moved on as site Owner

I started with the front page. I am happy that the page takes the first six data enteries from books and people and shows them in a responsive format. At a later date i would like to keep six showing but create a carousel and siplay a few more images as site grows.
I move on to people and happy with the display of the people there. Initally i have a delete button here but unhappy with the ability of deleteing the person and leaving the book in next page so i have the button removed. Moving on to books i can
edit and delete submissions by others as i make sure content is correct and fit for website purpose. I moved on to the blog and was unhappy with how the buttons stood out so much and ammended them to icons. Upon fixing i was able to edit and delete blogs. In the add blog section i was able to add a new subject and title.



## Deployment

This app is currently deployed on Heroku. The code deployed is stored on the master branch of this project here on GitHub. Heroku requires the following steps to deploy this project. https://inspire-book-repo.herokuapp.com/

1. Once signed in, click the "new" button on the dashboard to create a new application.

2. Name the App and choose the region you are currently in.

3. Create a requirements.txt file to allow Heroku to install the dependencies required by the application.

pip3 freeze --local > requirements.txt

4. Create a procfile to tell Heroku what type of application will be deployed.

echo web: python run.py > Procfile

5. On the deployment page of the Heroku project, choose Heroku GIT for deploying.

6. In the CLI of your environment, input the following code:

$ heroku login
$ heroku git:remote -a <inspire-books-repo>
$ git push heroku master

7. In Heroku settings, chose "Real Config Vars" to set the proper environmental variables
IP:    0.0.0.0
Port:    5000
MONGO_URI mongodb+srv://<username>:<password>@<cluster_name>.mongodb.net/<database>?retryWrites=true&w=majority
SECRET_KEY:   <your_value>

8. Click the "Open App" button to view the final deployed app.


## Credits

### Acknowledgements
I would like to thank CI tutors for helping me work out the $pull $push for adding and deleteing arrays and my mentor Victor for pushing me to find the bugs and with UI layout and the issues they could create.

### Content
- The filler text for the blog was copied from the [reddit fantasy](https://www.reddit.com/r/Fantasy/)

### Media
- images for the books came from [Amazon](https://www.amazon.co.uk/)
- images for people came from [google images](https://www.google.co.uk/imghp?hl=en&tab=wi&ogbl)
