# Recipe Collection

The Recipe Collection web application is a comprehensive Django project with a focus on creating a platform for food enthusiasts to explore, share, and discover their favorite recipes. Throughout this project, I have utilized various technologies and implemented key functionalities to create a seamless and engaging user experience.

### Key Features:

* Recipe Database: The heart of the application lies in its extensive recipe database. I have designed a database structure to store recipes contributed by users. Each recipe is stored with essential details, such as ingredients, preparation steps, cooking time, and an image.
* User Authentication: To provide a personalized experience, I have implemented user authentication features. Users can register, log in, and create their profiles, allowing them to save their favorite recipes and submit new recipes.
* Recipe Submission: As part of the user experience, I have integrated a recipe submission feature. Authenticated users can easily submit their unique recipes, complete with images and additional notes. These contributions enrich the platform and encourage the exchange of diverse culinary creations.
* Search Functionality: To facilitate recipe discovery, I have implemented a search feature. Users can search for recipes based on specific ingredients, cuisines, etc.
* User Interaction: I have included an interactive feature that allows authenticated users to 'like' other recipes posted.
* Responsive Design: Recognizing the importance of a seamless user experience across devices, I have ensured that the web application is responsive and mobile-friendly. Users can access Recipe Collection on various devices without compromising usability.

## User Experience

### Overview

Recipe Collection is designed with the user in mind, offering an enjoyable experience for both cooking enthusiasts and casual visitors. The platform's user experience centers around simplicity, accessibility, and interactivity, ensuring that users can effortlessly navigate through the site and discover inspiring recipes. Below are key aspects of the user experience and the corresponding user stories.

#### Viewing and Navigation
* Users can explore Recipe Collection on various devices, ensuring a consistent experience regardless of screen size.
* A user-friendly home page welcomes visitors, showcasing the site's goal and motivating them to sign up.
* The registration process is straightforward, allowing users to quickly create an account and gain access to the site's features.

#### Searching
* Recipe Collection offers a search feature, allowing users to find recipes based on ingredients, categories, or specific keywords.
* Users also have the option to browse the pages of posted recipes and click on images of recipes that they find interesting- those are open for viewing also for non-registered users. 

#### Accounts
* Each user has a personalized user profile, showcasing their culinary achievements and uploaded recipes.

### User Stories
#### As site user:
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

### Site owner stories:
1. I want to restrict access to certain sections of the app to unauthenticated users, ensuring basic standards of data protection and privacy.
2. Authenticated users should have full access to the web app and its complete functionality, fostering a seamless and immersive experience.
3. I want to have control as site administrator so I can remove posts or edit them or even delete users. 

## Features

### Strcuture

#### base.html

**base.html** serves as the foundational template for the Healthy Choices web application, providing a structure and consistent design across all pages. This reusable template incorporates essential elements, such as a navigation bar, footer, and login/signup options, to enhance user experience and streamline navigation.

The top **navigation** bar features the Healthy Choices logo, a red radish emblem, reinforcing the app's theme of healthy living. The navigation bar is collapsible on smaller screens to optimize space and create a user-friendly experience. Users can navigate through various sections, including the Home and About pages, ensuring easy access to essential information.

Healthy Choices **empowers** its users to contribute and engage actively with the community. Unauthenticated users are encouraged to register and create an account, enabling access to exclusive features. Authenticated users have the privilege to add their choices, fostering a sense of belonging and personalization.

The app's clean and **responsive** layout ensures a seamless experience across devices of different sizes. From the landing page, users can explore the latest posts, staying updated with a vibrant community. A detailed view of each post provides in-depth information and an opportunity to like recipes, encourages interaction and participation.

The **footer** presents essential copyright information and credits the creative minds behind Healthy Choices. The footer also includes convenient social media contact links, allowing users to reach out to the app's creator effortlessly, as well as fellow users that are also connected to the app one Facebook/Instagram.

**base.html** ensures that each page within the Healthy Choices web application adheres to a consistent and visually appealing design, providing a memorable and delightful user experience.

#### home.html

The home page prompts new visitors to **create an account**, enabling them to access exclusive features, such as recipe creation and interaction with the community. Authenticated users can log in and out securely, ensuring a personalized and protected environment.

The home page is the first page visitors see on the site so it needed to be **vibrant** and **eye-catching**.The page dynamically displays the latest culinary creations. Each recipe card is automatically generated and enriched with captivating images, engaging headlines, and succinct descriptions, making browsing a (hopefully) delightful experience.

Interactive elements on the Home page enrich user engagement. For example, the recipe image hover effect is intersting and attracts user interaction. Authenticated users can easily move to create new recipes by clicking the **create recipe button**. User interactions are further personalized with dynamic greetings- Authenticated users are addressed by their usernames, creating a sense of belonging and enhancing the platform's friendly ambiance.

The Home page utilizes a responsive **pagination** system to efficiently manage recipe listings. Users can navigate through multiple pages of recipes, ensuring optimal performance and user satisfaction, regardless of the volume of content.

Advanced **search functionality** empowers users to find recipes based on specific keywords. The Home page processes search queries and delivers relevant results promptly. The intuitive search bar and efficient backend mechanisms ensure a smooth search experience.

**User data**, is securely managed by the application's back-end. Password encryption, data validation, and user authentication mechanisms safeguard sensitive information, ensuring user privacy and data integrity.

The **hero image** on the Home page has an interactive effect, dynamically scaling upon user interaction. The effect, implemented using JavaScript and the Intersection Observer API, creates, I hope, an eye-catching visual element.

#### My profile page

Once **logged in**, users can access their personalized profile pages, where they have the freedom to change their profile bio, making their presence unique and identifiable. On the profile page users also have the buttons and links to update their profile, change or reset their passwords, and access their posted recipes. This enables users to use the website as an electronic paperless recipe-database.

#### Search results page

The search functionality is open to both registered and non-registered users. The page itself will present all the recipes that include the key word the user searched for, as well as display the number of results found. The user can then simply click on the link and be redirected to the appropriate recipe. 

#### Signup and login pages

These pages contains simple responsive forms for registration/logging in. On the registration page is again a small text promoting the app and encouraging users to join- and for ease of registration, users are only required to input a username, email address, and a password. 

#### Create a new recipe page

This page contains a simple recipe creation form with a headline, description, ingredients, and preparation input boxes (with placeholders so that users know what each input box is for) as well as the requirement to upload a recipe image. Once a user uses the browse button to choose an image, the preview image will show up on the page.

#### Recipe pages

Individual recipe pages contain an image, headline, description, ingredients, preparation instructions, name of the recipe's author, the date and time it was posted and the amount of likes the recipe got. Authenticated users will also see a like button. Authenicated users that authored the recipe will also see a link to edit the recipe, and delete the recipe. 

#### Update Recipe page
The update recipe is only accessible to an authenticated recipe author. They are able to edit the recipe, or change the image. This page will also give them the option to delete the recipe if they wish to do so. If the user chooses to delete the recipe, a modal window will open up requesting confirmation. If nothing had been updated and the user clicked on update, the page will simply reload.

## CRUD functionality 

This web application allows registered users to view, create, delete, or update recipes. The updates take place immediately. Site adminidtrators have the 'superpower' the control other users' recipes too in addition to the above mentioned capabilities. 

## Design

### Colors

![color palette of usage]


## Technologies, tools, and frameworks Used

### Languages:
* Python
* JavaScript
* HTML5
* CSS3

### Frameworks:
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)

### Deployment: 
* [Heroku](https://heroku.com/)

### Version control:
* [Git](https://github.com/) - version control and respository hub

### IDE's: 
* [Gitpod](https://gitpod.io/)
* Visual Studio Code

### Media and static storage:
*[Cloudinary](https://cloudinary.com/)

### Tools:
* [Google Fonts](https://fonts.google.com/)
* [Flaticons](https://www.flaticon.com/)


## Tests

container gave itself a boostrap !important that i cannot override since it's not in my css but in the bootstrap - tried to use JS to figure out the issue and did some tests to see if i could apply styles: 

## Bugs and bug fixes

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

---

There were many more bugs but I learned to: 

1. Not be dismayed- most things can be fixed by looking at it from a different perspective.
2. If my Python doesn't work- employ JavaScript.
3. Sometimes changing the logic to a different logic can give me a much simpler and clearer solution to a problem. 



## Testing

### Manual tests

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


---
---
### Automated testing:

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
In the end i realised it was just a cache issue... :face_palm:

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

## Credits

* Icons: <a href="https://www.flaticon.com/free-icons/radish" title="radish icons">Radish icons created by Futuer - Flaticon</a>

* Documentaion for the js scroll effect: 
https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/isIntersecting
http://scrollmagic.io/docs/

* about.html image: Photo by <a href="https://unsplash.com/@charlesdeluvio?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">charlesdeluvio</a> on <a href="https://unsplash.com/backgrounds/things/food?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

* [Jamie Oliver](https://www.jamieoliver.com/recipes/category/special-diets/vegan/) recipe images and recipes.

* [Feasting At Home](https://www.feastingathome.com/vegan-dinner-recipes/) recipe images and recipes.

* [Maangchi](https://www.maangchi.com/recipe/chaesik-kimchi) recipe image and recipe.

* [BudgetBytes](https://www.budgetbytes.com/category/recipes/vegetarian/) recipe images and recipes.

* [Delish](https://www.delish.com/cooking/g1486/healthy-vegetarian-dinner-recipes/) recipe images and recipes.

* [GoodFood (BBC)](https://www.bbcgoodfood.com/recipes/collection/vegetarian-dinner-recipes) recipe images and recipes.

* [Gordon Frampy](https://www.deviantart.com/thegothengine/gallery) by TheGothEngine

* [Code Institue](https://codeinstitute.net/) Django Walkthrough for project setup and deployment.

### Acknoledgements

[Code Institue](https://codeinstitute.net/) tutors: 
* Alan that always has patience for even the silliest of questions, 

and,

* Oisin for figuring out in less than one minute an error in the code. 

* Gemma for sorting out more gitpod hours! 

PPhoto by <a href="https://unsplash.com/@dosejuice?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Dose Juice</a> on <a href="https://unsplash.com/images/food?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  