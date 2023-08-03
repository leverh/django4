# Validators

## Python

### All issues displayed by the linter have been resolved:

#### **Forms.py**
![Image of linter test](./readme-images/PyLinter%20forms.png)

#### **Urls.py**
![Image of linter test](./readme-images/PyLinter%20urls.png)

#### **views.py**
![Image of linter test](./readme-images/PyLinter%20views.png)

#### **models.py**
![Image of linter test](./readme-images/PyLinter%20models.png)

## **JavaScript**

#### **Update Page**
![image of JSHint validator results](./readme-images/JSHint%20update%20page.png)

#### **Sign Up**
![image of JSHint validator results](./readme-images/JSHint%20signup%20page.png)

#### **Profile Update Page**
![image of JSHint validator results](./readme-images/JSHint%20profile%20update%20page.png)


#### **Create Page**
![image of JSHint validator results](./readme-images/JSHint%20create%20page.png)

#### **Main script.js file**
![image of JSHint validator results](./readme-images/JShint%20script%20file.png)

## **CSS**

![image of CSS validator results](./readme-images/validator%20css.png)

## **HTML**

#### **base.html**
![image of html validator results](./readme-images/Screenshot%202023-07-28%20at%2010-59-14%20Showing%20results%20for%20contents%20of%20text-input%20area%20-%20Nu%20Html%20Checker.png)

#### **home.html**
![image of html validator results](./readme-images/validator%20home.png)

#### **Password Reset Page**
![image of html validator results](./readme-images/validator%20password%20reset.png)

#### **Profile Page**
![image of html validator results](./readme-images/validator%20profile.png)

#### **About Page**
![image of html validator results](./readme-images/validator%20about.png)

#### **Login Page**
![image of html validator results](./readme-images/validator%20login.png)

#### **Recipe Page**
![image of html validator results](./readme-images/validator%20recipe%20detail.png)

#### **Logged In Home and Base pages**
![image of html validator results](./readme-images/validator-%20home%20+%20base.png)

## **Accessibility**

**Descriptive Labels** - **Aria** - are used to provide descriptive labels for form inputs and interactive elements like in the following:
```html
<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
```
or here: 
```html
<img src="{{ recipe.image.url }}" alt="Image of {{ recipe.headline }}" aria-label="Image of {{ recipe.headline }}" class="card-img-top card-img">. 
```
and here:
```html
<button data-bs-toggle="collapse" class="navbar-toggler" data-bs-target="#navcol-1" aria-label="Toggle navigation menu">
```

**Role definition** is used to clarify the function of an element within a page. For example, to let a user with assistive technology know of an alert:
```html
<div class="alert alert-success alert-dismissible fade show" role="alert">
```
**Improving navigation** by adding a label to elements such as the search bar:

```html
<input type="text" name="q" class="form-control" placeholder="Search by keyword" aria-label="Search by keyword">.
```

**Dynamic** use of jinja in aria-labels where content changes on a site like here:

```html
<img src="{{ recipe.image.url }}" alt="Image of {{ recipe.headline }}" aria-label="Image of {{ recipe.headline }}" class="card-img-top card-img">
```

Last but not least, the accessibility validation for contrasts as shown below:

### **Contrast reports**

#### **Background and text color**
![image of contrast validator](./readme-images/Screenshot%202023-08-02%20at%2023-59-51%20WebAIM%20Contrast%20Checker.png)

#### **Buttons and background**
![image of contrast validator](./readme-images/Screenshot%202023-08-03%20at%2011-30-37%20WebAIM%20Contrast%20Checker.png)

#### **Text on buttons and buttons**
![image of contrast validator](./readme-images/Screenshot%202023-08-03%20at%2011-31-25%20WebAIM%20Contrast%20Checker.png)

#### **Search results** 
![image of contrast validator](./readme-images/Screenshot%202023-08-03%20at%2011-50-41%20WebAIM%20Contrast%20Checker.png)