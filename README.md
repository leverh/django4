# Recipe Collection

The Recipe Collection web application is a comprehensive Django project with a focus on creating a platform for food enthusiasts to explore, share, and discover their favorite recipes. Throughout this project, I have utilized various technologies and implemented key functionalities to create a seamless and engaging user experience.

Link to [**Recipe Collection**](https://recipe-collection-deea6c7fa662.herokuapp.com/) live app website
# Table of Contents


1. [Key-Features](#key-features)

2. [User-Experience](#ux)
   - [Viewing and Navigation](#viewing-and-navigation)
   - [Searching](#searching)
   - [Accounts](#accounts)

3. [User Stories](#user-stories)
   - [As site user](#as-site-user)
   - [Site owner stories](#site-owner-stories)

4. [Features](#structure)
   - [base.html](#basehtml)
   - [home.html](#homehtml)
   - [My profile page](#my-profile-page)
   - [Search results page](#search-results-page)
   - [Signup and login pages](#signup-and-login-pages)
   - [Create a new recipe page](#create-a-new-recipe-page)
   - [Recipe pages](#recipe-pages)
   - [Update Recipe page](#update-recipe-page)

5. [CRUD functionality](#crud-functionality)

6. [Design](#design)
   - [Wireframes](#wireframes)
   - [Colors](#colors)

8. [Flowcharts](#flowcharts)

9. [Heroku Deployment Steps](#heroku-deployment-steps)
   
10. [Version Control History](#version-control-history)

 11. [Technologies, Tools, and Frameworks Used](#technologies-tools-and-frameworks-used)
   - [Languages](#languages)
   - [Frameworks](#frameworks)
   - [Deployment](#deployment)
   - [Version Control](#version-control)
   - [IDE's](#ides)
   - [Media and Static Storage](#media-and-static-storage)
   - [Tools](#tools) 

12. [Agile Work Plans](#agile-work-plans)
   
13. [Bugs And Fixes](#bugs-and-fixes)

14. [Testing](#testing)
   - [Manual Tests](#manual-tests)
   - [Automated Testing](#automated-testing)
   - [Validators](#validators)

15. [Credits](#credits)

### Key Features <a name="key-features"></a>

* Recipe Database: The heart of the application lies in its extensive recipe database. I have designed a database structure to store recipes contributed by users. Each recipe is stored with essential details, such as ingredients, preparation steps, cooking time, and an image.
* User Authentication: To provide a personalized experience, I have implemented user authentication features. Users can register, log in, and create their profiles, allowing them to save their favorite recipes and submit new recipes.
* Recipe Submission: As part of the user experience, I have integrated a recipe submission feature. Authenticated users can easily submit their unique recipes, complete with images and additional notes. These contributions enrich the platform and encourage the exchange of diverse culinary creations.
* User alerts: I have incorporated Django alerts for various actions: recipe creation, recipe updates, profile updates, etc. 

![Image of Django user alerts](./readme-images/Screenshot%202023-07-31%20at%2017-12-12%20Recipe%20Collection.png)
--
* Search Functionality: To facilitate recipe discovery, I have implemented a search feature. Users can search for recipes based on specific ingredients, cuisines, etc.

![Image of search results](./readme-images/Screenshot%202023-07-31%20at%2023-48-43%20Recipe%20Collection.png)

The results will show the keyword searched again, as well as a total results found. All results are naturally clickable and will direct the users to their recipe of choice.
* User Interaction: I have included an interactive feature that allows authenticated users to 'like' other recipes posted.
* Responsive Design: Recognizing the importance of a seamless user experience across devices, I have ensured that the web application is responsive and mobile-friendly. Users can access Recipe Collection on various devices without compromising usability.

## User Experience <a name="ux"></a>


### Overview

Recipe Collection is designed with the user in mind, offering an enjoyable experience for both cooking enthusiasts and casual visitors. The platform's user experience centers around simplicity, accessibility, and interactivity, ensuring that users can effortlessly navigate through the site and discover inspiring recipes. Below are key aspects of the user experience and the corresponding user stories.

#### Viewing and Navigation <a name="viewing-and-navigation"></a>


* Users can explore Recipe Collection on various devices, ensuring a consistent experience regardless of screen size.
* A user-friendly home page welcomes visitors, showcasing the site's goal and motivating them to sign up.
* The registration process is straightforward, allowing users to quickly create an account and gain access to the site's features.

#### Searching <a name="searching"></a>


* Recipe Collection offers a search feature, allowing users to find recipes based on ingredients, categories, or specific keywords.
* Users also have the option to browse the pages of posted recipes and click on images of recipes that they find interesting- those are open for viewing also for non-registered users. 

#### Accounts <a name="accounts"></a>


* Each user has a personalized user profile, showcasing their culinary achievements and uploaded recipes.

### User Stories <a name="user-stories"></a>

#### As site user: <a name="as-site-user"></a>


1. I want the app's navigation to be intuitive and user-friendly so that I can easily explore the content and features.
2. I expect clear and concise information about the app's purpose and functionality, enabling me to utilize it effectively for mutual benefit. I also want it to be simple to use.
3. I can register, log in, and log out from the website, ensuring a secure and personalized experience.
4. I can visit the posting page and browse through all the posts made on the website chronologically, keeping myself updated with the latest content.
5. Clicking on a post gives me a detailed view of that particular post, providing in-depth information and context.
6. If I'm logged in, I can interact with posts by liking them.
7. On the landing page, I can easily find the newest posts and comments, staying informed about recent activities.
8. When logged in, I have the option to go to my profile page and change my profile details, personalizing my account.
9. As a registered user, I can create my own posts, contributing my content to the platform.
10. If I'm logged in, I have the privilege to edit and delete my created posts, maintaining control over my contributions.
11. I expect to see appropriate error messages when I encounter issues or attempt to access forbidden links, guiding me to correct actions.
12. For security purposes, I have the option to change my password.

### Site owner stories: <a name="site-owner-stories"></a>


1. I want to restrict access to certain sections of the app to unauthenticated users, ensuring basic standards of data protection and privacy.
2. Authenticated users should have full access to the web app and its complete functionality, fostering a seamless and immersive experience.
3. I want to have control as site administrator so I can remove posts or edit them or even delete users. 

## Features <a name="structure"></a>


### Strcuture

#### <u>base.html</u> <a name="basehtml"></a>


**base.html** serves as the foundational template for the Healthy Choices web application, providing a structure and consistent design across all pages. This reusable template incorporates essential elements, such as a navigation bar, footer, and login/signup options, to enhance user experience and streamline navigation. **base.html** ensures that each page within the Healthy Choices web application adheres to a consistent and visually appealing design.

The top **navigation** bar features the Healthy Choices logo, a red radish emblem, reinforcing the app's theme of healthy living. The navigation bar is collapsible on smaller screens to optimize space and create a user-friendly experience. Users can navigate through various sections, including the Home and About pages, ensuring easy access to essential information.

![navbar image](./readme-images/Screenshot%202023-07-31%20at%2023-55-04%20Recipe%20Collection.png)

or the responsive version for small screens: 

![navbar image for small screens](./readme-images/Screenshot%202023-07-31%20at%2023-56-25%20Recipe%20Collection.png)

Healthy Choices **empowers** its users to contribute and engage actively with the community. Unauthenticated users are encouraged to register and create an account, enabling access to exclusive features. Authenticated users have the privilege to add their choices, fostering a sense of belonging and personalization.

The app's clean and **responsive** layout ensures a seamless experience across devices of different sizes. From the landing page, users can explore the latest posts, staying updated with a vibrant community. A detailed view of each post provides in-depth information and an opportunity to like recipes, encourages interaction and participation.

![Image of responsive layout for medium sized screens](./readme-images/Screenshot%202023-07-31%20at%2023-59-54%20Recipe%20Collection.png)

The **footer** presents essential copyright information and credits the creative minds behind Healthy Choices. The footer also includes convenient social media contact links, allowing users to reach out to the app's creator effortlessly, as well as fellow users that are also connected to the app one Facebook/Instagram. The year in the copyright will update automatically.

![image of footer with social links and copyright info](./readme-images/Screenshot%202023-08-01%20at%2000-01-14%20Recipe%20Collection.png)


#### <u>home.html</u> <a name="homehtml"></a>


The home page prompts new visitors to **create an account**, enabling them to access exclusive features, such as recipe creation and interaction with the community. Authenticated users can log in and out securely, ensuring a personalized and protected environment.

The home page is the first page visitors see on the site so it needed to be **vibrant** and **eye-catching**.The page dynamically displays the latest culinary creations. Each recipe card is automatically generated and enriched with captivating images, engaging headlines, and succinct descriptions, making browsing a (hopefully) delightful experience.

Interactive elements on the Home page enrich user engagement. For example, the recipe image hover effect is intersting and attracts user interaction. Authenticated users can easily move to create new recipes by clicking the **create recipe button**. User interactions are further personalized with dynamic greetings- Authenticated users are addressed by their usernames, creating a sense of belonging and enhancing the platform's friendly ambiance.

The Home page utilizes a responsive **pagination** system to efficiently manage recipe listings. Users can navigate through multiple pages of recipes, ensuring optimal performance and user satisfaction, regardless of the volume of content.

![image of pagination on the home page](./readme-images/Screenshot%202023-08-01%20at%2000-03-28%20Recipe%20Collection.png)

Advanced **search functionality** empowers users to find recipes based on specific keywords. The Home page processes search queries and delivers relevant results promptly. The intuitive search bar and efficient backend mechanisms ensure a smooth search experience.

![Image of search bar](./readme-images/Screenshot%202023-07-31%20at%2023-47-19%20Recipe%20Collection.png)

**User data**, is securely managed by the application's back-end. Password encryption, data validation, and user authentication mechanisms safeguard sensitive information, ensuring user privacy and data integrity.

The **hero image** on the Home page has an interactive effect, dynamically scaling upon user interaction. The effect, implemented using JavaScript and the Intersection Observer API, creates, I hope, an eye-catching visual element.

#### <u>My profile page </u><a name="my-profile-page"></a>


Once **logged in**, users can access their personalized profile pages, where they have the freedom to change their profile bio, making their presence unique and identifiable. On the profile page users also have the buttons and links to update their profile, change or reset their passwords, and access their posted recipes. This enables users to use the website as an electronic paperless recipe-database.

#### <u>Search results page</u> <a name="search-results-page"></a>


The search functionality is open to both registered and non-registered users. The page itself will present all the recipes that include the key word the user searched for, as well as display the number of results found. The user can then simply click on the link and be redirected to the appropriate recipe. 

#### <u>Signup and login pages</u> <a name="signup-and-login-pages"></a>


These pages contains simple responsive forms for registration/logging in. On the registration page is again a small text promoting the app and encouraging users to join- and for ease of registration, users are only required to input a username, email address, and a password. 

![Image of signup page](./readme-images/Screenshot%202023-08-01%20at%2000-06-28%20Recipe%20Collection.png)

#### <u>Create a new recipe page</u> <a name="create-a-new-recipe-page"></a>


This page contains a simple recipe creation form with a headline, description, ingredients, and preparation input boxes (with placeholders so that users know what each input box is for) as well as the requirement to upload a recipe image. Once a user uses the browse button to choose an image, the preview image will show up on the page.

#### <u>Recipe pages</u> <a name="recipe-pages"></a>


Individual recipe pages contain an image, headline, description, ingredients, preparation instructions, name of the recipe's author, the date and time it was posted and the amount of likes the recipe got. Authenticated users will also see a like button. Authenicated users that authored the recipe will also see a link to edit the recipe, and delete the recipe. 

![Image of recipe page](./readme-images/Screenshot%202023-08-01%20at%2000-07-58%20Recipe%20Collection.png)

#### <u>Update Recipe page </u><a name="update-recipe-page"></a>

The update recipe is only accessible to an authenticated recipe author. They are able to edit the recipe, or change the image. This page will also give them the option to delete the recipe if they wish to do so. If the user chooses to delete the recipe, a modal window will open up requesting confirmation. If nothing had been updated and the user clicked on update, the page will simply reload.

## CRUD functionality <a name="crud-functionality"></a>


This web application allows registered users to view, create, delete, or update recipes. The updates take place immediately. Site adminidtrators have the 'superpower' the control other users' recipes too in addition to the above mentioned capabilities. 

## Design <a name="design"></a>


The sites are vibrant and visually appealing to all things to do with food and cooking. 

The background contains a warm shade of #FFFFF0- this choice not only provides a cozy and comfortable ambiance but also makes the images users post stand out.
I thought the greens I use for the buttons are playful, as well as sufficiently soft to be attractive and inviting. 

I chose pink for the like button because it stands out from the rest and hopefully makes users feel friendly towards one another. 

The text colors of #333 and #6c757d feel elegant as users read through the recipes. 

But the True colors of this website are the colorful images of food that accompany each and every recipe. From vibrant fruits and veggies in the hero image, to mouth-watering dessers and savory dishes- hopefully inspire users (and make them hungry). 

### <u>Wireframes</u> <a name="wireframes"></a>


These are some of the general ideas i drew up before building my HTML templates:

#### **Home.html:**

![wireframe for the home.html page](./readme-images/home%20wireframe.png)

---

#### **Login page:**

![wireframe for the login page](./readme-images/New%20Wireframe%201(1).png)

---
#### **Individual Recipe page (guest view):**

![wireframe for recipe detail page](./readme-images/New%20Wireframe%201(2).png)

---

#### **Profile page:**
![wireframe for profile page](./readme-images/New%20Wireframe%201(3).png)

---
### Colors <a name="colors"></a>


![color palette of usage](./readme-images/Screenshot%202023-08-03%20at%2017-23-40%20Color%20wheel%20a%20color%20palette%20generator%20Adobe%20Color.png)

I tried to stick to the above colors whenever possible to keep a uniformed look for the app. I believe that even when i used different shades (that aren't listed above), I made every page look like it was part of a system rather than a stand-alone element. That being said, I think a webpage is dynamic and needs to convey a mood- so subtle changes are welcome in my opinion.


## Flowcharts <a name="flowcharts"></a>


* I did some research on how to create proper code flow charts and I tried to create one for models.py based on: 

1. Recipe:
* Fields: headline, description, ingredients, preparation, posted_by, liked_by, date_posted, image.

* Relationships:
* Many-to-one with User through posted_by.
* Many-to-many with User through liked_by.

2. Profile: 
* Fields: user, bio, favorite_recipes, profile_image.

* relationships: 
* One-to-one with User.
* Many-to-many with Recipe through favorite_recipes.


This is my feeble attempt at trying to visualize it:

![flow chart of the models.py file](./readme-images/Blank%20diagram.png)

1 means there is exactly one instance on that side of the relationship. 

M means that there can be many instances on that side of the relationship.

* In my case, the one-to-one relationship between User and Profile is represented as "1:1." This means that each User is associated with exactly one Profile, and each Profile is associated with exactly one User.

* The many-to-one relationship between Recipe and User (for posted_by) can be represented as "m:1." This means that many Recipe objects can be posted by one User, but each Recipe is posted by exactly one User.

* The many-to-many relationship between Recipe and User (for liked_by) can be represented as "m:m"." This means that many Recipe objects can be liked by many User objects, and vice versa.

* Following is the logic HTML basic structure:

![HTML flowchart for project](./readme-images/Recipe%20Collection.png)

## Deployment <a name="heroku-deployment-steps"></a>


The App was deployed to Heroku using the following steps: 

1. In Heroku (account needed):
* From the dashboard select "New" followed by "Create New App"
* Choose the correct region
* Input the App name
* Click "Create App"
* Go to the "Resources" section and search for Heroku Postgres and submit 
* In the settings tab click "Reveal Config Vars", then:
  * Add config var for SECRET_KEY: [[Your Secret Key]]
  * Add Cloudinary_URL: [Your Cloudinary API Key]
  * Add DISABLE_COLLECTSTATIC: [1]
  * DATABASE_URL should already be there having installed Postgres in previous steps
* Click the "Deploy" section, then "Connect to GitHub" and sign-in if asked to do so  
* Choose the repository you would like to deploy and click "Connect"
* You can choose between "Manual Deploy" and "Automatic Deploy" and choose the correct branch.
* Once Heroku finalizes the deploy, you can click on "Deploy" and a new tab will open with the deployed app.

2. In your project folder:

* Create an env.py file in the root diectory of your project
* in your env.py file add the following:
    * import os (at the very top of file)
    * os.environ["DATABASE_URL"] = "postgres://.... (your postgres URL)
    * os.environ["SECRET_KEY"] = (your secret key)
    * os.environ["CLOUDINARY_URL"] = "cloudinary://... (your cloudinary URL)
    * os.environ['DEBUG'] = '1'


**VERY IMPORTANT:**
  * If no .gitignore file is present, you should create one and add your env.py to it before you push your project to GitHub. The file should look something like this: 
  ``` python
  core.Microsoft*
core.mongo*
core.python*
env.py
__pycache__/
*.py[cod]
node_modules/
.github/
cloudinary_python.txt
  ```

* In the project's **settings.py** file add the following: 
```python
  from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
    import env
```
* Change your SECRET_KEY (**settings.py**) to: 

```python
SECRET_KEY = os.environ.get('SECRET_KEY')
```

* Add the Heroku URL to the ALLOWED_HOSTS (**settings.py**) like this: 

```python
ALLOWED_HOSTS = ["URL of Heroku App", ]
```

* Add your new DATABASES (**settings.py**):

```python
DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
} 
``` 

* Add Cloudinary to INSTALLED_APPS (**settings.py**) so:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'recipe_collection',
]
```

* Add the Cloudinary to the following (**settings.py**): 
```python
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
Following that, run the command Run 'python3 manage.py collectstatic' in your terminal.

* Create a Procfile in the root directory and add the following to the file:
```python
web: gunicorn myproject.wsgi
```

* Create a requirments.txt file using the command: **pip3 freeze --local > requirements.txt** in your terminal. Your new file will look similar to this: 
```python
asgiref==3.7.2
cloudinary==1.33.0
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.6
Django==3.2.19
gunicorn==20.1.0
psycopg2==2.9.6
pytz==2023.3
sqlparse==0.4.4
urllib3==1.26.15
Pillow==8.4.0
```
It contains all the apps/databases/helpers you're using in your project.

* Migrate your project by typing: **python manage.py migrate** in your terminal.

* Finally you can git add, git commit, and git push all the changes made. 

3. Prior to final deployment: 

* In settings.py make sure to make the following changes and add:
```python
DEBUG = False

X_FRAME_OPTIONS = 'SAMEORIGIN'
```

* In the Heroku config vars remove DISABLE_COLLECTSTATIC

* Go to the deploy tab on Heroku and follow the same steps as before:
  * Click the "Deploy" section, then "Connect to GitHub" and sign-in if asked to do so
  * Choose the repository you would like to deploy and click "Connect"
  * You can choose between "Manual Deploy" and "Automatic Deploy" and choose the correct branch.
  * Once Heroku finalizes the deploy, you can click on "Deploy" and a new tab will open with the deployed app.

## Version Control <a name="version-control-history"></a>


You will find I actually used 2 repositories for this project- Initially I started the project on [Django-Project-One](https://github.com/leverh/Django-Project-One) but found that I made some mistakes during the setup. I decided then to start again for the setup procedure and started a new repository- [Djano4](https://github.com/leverh/django4). Once i had the setup and first deployment working (And Cloudinary which caused most of the issues), I copied and pasted the code I had already created from Django-Project-One into the Django4 respository. 

I used version control on so many occasions in this project to do hard resets due to rabbit hole bugs, or branch out to test new things. The final branch (appropriately named) [mondaytry](https://github.com/leverh/django4/tree/mondaytry) is the project i actually ended up deploying. 



## Technologies, tools, and frameworks Used <a name="technologies-tools-and-frameworks-used"></a>


### Languages: <a name="languages"></a>

* Python
* JavaScript
* HTML5
* CSS3

### Frameworks: <a name="languages"></a>{#frameworks}

* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)

### Deployment: <a name="deployment"></a>

* [Heroku](https://heroku.com/)

### Version control: <a name="version-control"></a>

* [Git](https://github.com/) - version control and respository hub

### IDE's: <a name="ides"></a>

* [Gitpod](https://gitpod.io/)
* Visual Studio Code

### Media and static storage: <a name="languages"></a>{#media-and-static-storage}

* [Cloudinary](https://cloudinary.com/)

### Tools: <a name="tools"></a>

* [Google Fonts](https://fonts.google.com/)
* [Flaticons](https://www.flaticon.com/)

## Agile Work Plans <a name="agile-work-plans"></a>


This project utilized GitHub's Project feature for the planning. Since I was working on this project alone, it was a good way for me to structure my to-do's, return to ongoing issues, and debug. Tou can find the info [here on GitHub Projects](https://github.com/users/leverh/projects/1/views/1). 

I think that I particularly used the **Sprint Development Cycle** of defining clearly the requirements, developing them, and immediately testing and deploying them. 

## Bugs and bug fixes <a name="bugs-and-fixes"></a>

As I went along with the project, I realised something very important that I will be more aware of in the next big projects: rather than planning ahead logically, I coded and built my app according to the features and the final result in my head. Coding with the 'feel' rather than the 'logic' can lead to constant bugs, some of which i list below:

* I discovered the following bug:  a modal window opens with the js message at the bottom even if the user has not successfully created an account. the message should appear only if there was an account successfully created. If not, it should provide the user with an error message. after several tries I fixed the functionality, but got a **"Error: SyntaxError: JSON.parse: unexpected character at line 2 column 1 of the JSON data".** I then used log comments to try and figure out the bug: 
```javascript
fetch('{% url "signup" %}', {
      method: 'POST',
      body: new FormData(document.querySelector('.signup-form')),
    })
    .then(response => {
      **console.log('Response:', response);**
      return response.json();
```
That indicated the server returned a successful respone but there was an issue with data being returned. So I added another console.log: 
```javascript 
console.log('Content-Type:', response.headers.get('Content-Type'));
```  
to check for a content-type and then a:
```javascript
.then(data => {
  console.log('Data:', data); 
  return JSON.parse(data);
})
```
Eventually after about 20 tests I gathered that the server response was being receieved as text/html instead of the expected application/json.
After a few tries (and a lot of hair pulling) and a Git hard reset I managed to fix the issue.


* After switching debug to false, got a 400 Bad Request page. Developer tools console showed nothing. to debug i did the following: 
1. Check server logs. But i couldn't find anything.
2. Enabling error logging by importing logging and then the code: 
```python 
logging.basicConfig(level=logging.INFO)
```
3. when that failed i asked for tutor support. 

* A bug was discovered when I set success_url to a string, which caused an incorrect redirection after a successful form submission. Instead of using it as a string, i tried using the jinja {% %} which worked.

* I discovered a bug to do with an error due to an image name being too long:
**DataError: value too long for type character varying(100)**. 
It took me a while to diagnose the issue but after extensive online searches i discovered it was due to the max length of characters. I then looked for a solution for this issue and discovered the [truncatechars](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#truncatechars) and checked it in my code: 
```python 
image_filename = form.cleaned_data['image'].name
        truncated_image_filename = truncate_chars(image_filename, 100)
        form.instance.image = truncated_image_filename
```
That didn't fix the issue either. After several tries of different combinations of code and another hard reset i found a fragile status quo that didn't bug. 

* Then i discovered the I forgot to add functionality to my delete button and used an existing delete button to fix the issue and updated the JS to include the delete functionality: 
```javascript
$(document).ready(function() {
    $('#deleteBtn').on('click', function() {
      var confirmMessage = "Are you sure you want to delete this recipe?";
      if (confirm(confirmMessage)) {
        var deleteUrl = $(this).data('url');
        $.ajax({
          url: deleteUrl,
          method: 'DELETE',
          success: function() {
            window.location.href = '/';
          }
        });
      }
    });
  ```

  * Paginator bug: System was not recognizing the current paginator class, preventing the user from knowing what page numbert they were on. I tried several methods for fixing the issue until I decided to go for the JS solution. The JS code took a few tries until i finally got the right combination: 
  ```javascript
  document.addEventListener("DOMContentLoaded", function() {
    const currentPage = new URLSearchParams(window.location.search).get("page");

    const paginationLinks = document.getElementById("pagination-links");
    const links = paginationLinks.getElementsByTagName("a");

    for (const link of links) {
      const page = parseInt(link.innerText);
      if (page === parseInt(currentPage)) {
        link.classList.add("current-page");
      }
    }
  }); 
  ```
  This lead to another bug which I tried to combat by adding a custom_filters.py file and this code for django: 
  ```python
  @register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})
  ```
That didn't work either unfortunately. Eventually i resolved it by adding: 
```python
context['current_page'] = current_page
```  
to my recipelistview and: 
```python
const paginationLinks = document.getElementById('pagination-links');
const links = paginationLinks.getElementsByTagName('a');  
```
to my script.

* A bug with the [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) (according to documentation it's a bug related to target element not being a valid DOM element). I tried switching to a 
```javascript
document.querySelector()
``` 
instead of 
```javascript
getElementById
```
In the end to simplify the process I added a class to the appropriate element, and to the js code a check to ensure that heroImage is not null before proceeding with the checkVisibility logic. It worked!


* I encountered a bug with the password reset option where a user could enter any email address and receieve a reset email. When looking for a fix (approx. 3 days to fix and several tries) I discovered I wasn't using the Django built-in password reset option ([Password Reset tutorial](https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html) and [another](https://django-password-reset.readthedocs.io/en/latest/)) properly. I incorporated it eventually in my code and it works just fine now:
```python
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def form_valid(self, form):
        print("CustomPasswordResetConfirmView - form is valid")
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        print("CustomPasswordResetConfirmView - form is invalid")
        return super().form_invalid(form)


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
```
---

There were many more bugs but I learned to: 

1. Not be dismayed- most things can be fixed by looking at it from a different perspective.
2. If my Python doesn't work- employ JavaScript.
3. Sometimes changing the logic to a different logic can give me a much simpler and clearer solution to a problem. 



## Testing <a name="testing"></a>


### <u>Manual tests </u><a name="manual-tests"></a>


I tested all the functionalities of the app and went about fixing all the bugs that arose (a few of which i listed above in the bugs section). I used Firefox developer tools to inspect my pages and console, and my terminal for error logs.

#### The tests: 


| Expected                                      | Test Performed                                | Result  |
| --------------------------------------------- | --------------------------------------------- | ------- |
| Buttons checked for functionality            | Clicked every button in the app              | Passed  |
| Form required fields not being filled prevent form from being submitted | Tested every form | Passed  |
| Modal window or Django message upon form submission| Tested every form for success or other alert messages| Passed  |
| Search function returns the expected data     | Tested multiple keywords                    | Passed  |
| All links redirect users to the appropriate destination | Clicked every link to check | Passed|
| User authentication works as expected. Non-authenticated users cannot view certain elements authenticated users can | Created several user profile and tested all functionalities | Passed |
| User profile can be updated as expected by changing bio or email info | Tested the different buttons on the user profile page to make sure all are functional | Passed |
| Recipe creation, update and deletion working as expected | Created several recipes which I then attempted to edit by using different text or a different image | Passed |
| Non-recipe-authors should not be able to edit or delete recipes | Checked to see that the options are not available to non-author authenticated and non-authenticated users | Passed |
| Data transfer to Cloudinary to work seamlessly | Checked all images are uploaded to Cloudinary. Checked the time required for upload | Passed |
| Responsiveness of webpages | Checked all pages using the Firefox developer tools | Passed |
| Like button functions | Clicked the Like button on several recipes | Passed |
| User password manipulation |  Changing passwords multiple times, trying to reset passwords |  Partially passed - user password could be changed- however reset didn't work as expected. Please see the bugs section for more details on how I fixed the issue |
| Password functionality | Re-testing password functionalities (change password, reset password) | Passed |


---
---
### <u>Automated testing:</u> <a name="automated-testing"></a>


* As shown in the bug and bug fixing section, I used automated code testing regularly to try and figure out why things were not working as expected. Here are a couple more instances where I used automated tests:

* I couldn't get the styles I wrote for a certain page to appear and decided to use JS to test and maybe overcome the issue: 
```javascript
const prepElements = document.getElementsByClassName("prep-text");
for (let i = 0; i < prepElements.length; i++) {
  prepElements[i].style.backgroundColor = "yellow";
} 
```
and:
```javascript
const prepElements = document.getElementsByClassName("prep-text");
for (let i = 0; i < prepElements.length; i++) {
  prepElements[i].style.textAlign = "left !important";
}
```
Still had no luck so checked to see if I can see console.log statements using the following code: 
```javascript 
console.log("Script is running");

const prepElements = document.getElementsByClassName("prep-text");
console.log(prepElements.length);
for (let i = 0; i < prepElements.length; i++) {
  prepElements[i].style.textAlign = "left";
}
```
That didn't work either so tried the next test along:
```javascript 
 document.addEventListener("DOMContentLoaded", function () {
    console.log("Script is running");
  });
```
  and: 
  ```javascript
  document.addEventListener("DOMContentLoaded", function () {
            console.log("Script is running");
            const prepElements = document.getElementsByClassName("prep-text");
            console.log(prepElements.length);
            for (let i = 0; i < prepElements.length; i++) {
                prepElements[i].style.textAlign = "left";
            }
        });
```
In the end i realised it was just a cache issue... 🤦

* I used the- 
```python
python manage.py test
``` 
for the following tests: 

```python
class RecipeTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_recipe_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
```
to check the app returns a 200 status code. I created a fake recipe:
```python
def test_recipe_detail_view(self):
        recipe = Recipe.objects.create(
            headline='Test Recipe',
            description='This is a test recipe.',
            ingredients='Ingredient 1, Ingredient 2',
            posted_by_id=1)
```
and to check if the recipe detail view returns a 200 respone for an existing recipe:
```python
response = self.client.get(reverse('recipe-detail', args=[recipe.pk]))
        self.assertEqual(response.status_code, 200)
```
and another test for the recipe search view: 

```python
def test_recipe_search_view(self):
        response = self.client.get(reverse('recipe-search'))
        self.assertEqual(response.status_code, 200)
```
* Below is a screenshot of the Django backend email password reset functionality:

![screenshot of terminal's Django backend's password reset email](./readme-images/2023-08-02%20(2).png)



### Validators <a name="validators"></a>


The validator page can be found [here](./READMEVALIDATORS.md).



## Credits <a name="credits"></a>


* Icons: <a href="https://www.flaticon.com/free-icons/radish" title="radish icons">Radish icons created by Futuer - Flaticon</a>

* Documentaion for the js scroll effect: 
[Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/isIntersecting) and [scrollmagic](http://scrollmagic.io/docs/). 



### Media

* about.html image: Photo by <a href="https://unsplash.com/@charlesdeluvio?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">charlesdeluvio</a> on <a href="https://unsplash.com/backgrounds/things/food?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

* [Jamie Oliver](https://www.jamieoliver.com/recipes/category/special-diets/vegan/) recipe images and recipes.

* [Feasting At Home](https://www.feastingathome.com/vegan-dinner-recipes/) recipe images and recipes.

* [Maangchi](https://www.maangchi.com/recipe/chaesik-kimchi) recipe image and recipe.

* [BudgetBytes](https://www.budgetbytes.com/category/recipes/vegetarian/) recipe images and recipes.

* [Delish](https://www.delish.com/cooking/g1486/healthy-vegetarian-dinner-recipes/) recipe images and recipes.

* [GoodFood (BBC)](https://www.bbcgoodfood.com/recipes/collection/vegetarian-dinner-recipes) recipe images and recipes.

* [Gordon Frampy](https://www.deviantart.com/thegothengine/gallery) by TheGothEngine

* Photo by <a href="https://unsplash.com/@dosejuice?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Dose Juice</a> on <a href="https://unsplash.com/images/food?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

### Last But Not Least

* [Code Institue](https://codeinstitute.net/) Django Walkthrough for project setup and deployment.

### Acknoledgements

[Code Institue](https://codeinstitute.net/) tutors: 
* Alan that always has patience for even the silliest of questions, 

and,

* Oisin for figuring out in less than one minute an error in the code. 

* Gemma for sorting out more gitpod hours! 

* Sarah who calmed me down when everything seemed to fail!

  <p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>