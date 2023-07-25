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

## Technologies, tools, and frameworks Used

### Languages:
* Python
* JavaScript
* HTML5
* CSS3

### Frameworks:
* Django
* Bootstrap

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




icons: <a href="https://www.flaticon.com/free-icons/radish" title="radish icons">Radish icons created by Futuer - Flaticon</a>

documentaion for the js scroll effect: 
https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/isIntersecting
http://scrollmagic.io/docs/

about.html image: Photo by <a href="https://unsplash.com/@charlesdeluvio?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">charlesdeluvio</a> on <a href="https://unsplash.com/backgrounds/things/food?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  