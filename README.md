![Wig Image](documentation/wig_store_readme_logo.jpg)

# wiGalleria E-commerce Wig Store

wiGalleria is an e-commerce wig store app dedicated for the main purpose of purchasing wigs of different colours, shapes and textures as well as hair care products that helps wigs last longer.
This project was created using Python based Django framework. It is a fully featured app similar to real e-commerce apps out there that we use everyday with payment gateway that allows a user make payment but as this is a prototype, users are informed not to use their real debit/credit cards to purchase but can only use test debit/credit card provided by Stripe whose details will be given to anyone who wants to test this out once it's finished. A user will be able to perform full CRUD functionality i.e Create, Read, Update and Delete his data as well as making payment through the use of Stripe gateway API. The programming languages used for the development of this app are a combination of HTML, CSS (both bootstrap & custom) & JavaScript for the front-end and Python based Django framework for the back-end development. 

The purpose of this app is to allow a user purchase wigs and hair care products online in the comfort of their own homes without physically going to the store. Having an online wig store  eliminates the shortfall of store closing as it is on 24/7 except when store maintenance is taking place. The beauty and biggest advantage of building an ecommerce wig store is that it opens up a manually handled local business to a wider reach/audience worldwide so that it can be accessible for anyone to purchase wigs and hair care products from any location. 

The user interacts with the app through the GUI interface i.e front-end templates designed for each functionality such as add & edit products in the cart, view or delete products in the cart, view all products in the store & select the one(s) to purchase. There are role-based authentication system in place that ensures that different users can access different views i.e only registered/login/admin users can access certain views. An admin user will be the only one allowed to manage the store by interacting with the app through the front-end GUI interface & Django backend i.e perform CRUD functionality of Create, Read, Update & Delete products.  This store is protected with a very strong authentication system so that no unauthorised person will have access to its content. 

![wiGalleria app on Desktop, Laptop, Tablet & Smatphone](documentation/wigalleria_amiresponsive.png)

# Features

This E-commerce app named wiGalleria will allow the user register for an account, login, logout, checkout either as a registered user or guest user if they don't want to sign up for an account. It will also give them the ability to add product(s) to, edit or delete product(s) from and view products in the shopping cart.
When a user checks out, it will calculate and display the delivery cost as well as the total cost of products purchased before they make payment. It shows the user a summary of their order while on the checkout page and allows them to edit/update quantity of products they've selected earlier if they change their minds about buying them.
Overall, though the app is a prototype at the moment, yet it is a full fledge e-commerce app except that real purchase & payments cannot be made until some little adjustments are made and hopefully, this will be augmented in the near future to reflect this.

# Existing Features

The wiGalleria app will provide the following features to its users: 

* Create: It will allow a registered or guest user to add product(s) into the shopping cart 
* Read: It will allow a registered or guest user to view the items in their shopping cart
* Update: It will allow a registered or guest user to edit items in their shopping cart 
* Delete: It will allow a registered or guest user to either remove one or all products from their shopping cart
* Sign Up: It will allow a guest user to register for an account if he doesn't have one yet before he can access some features of the app
* Login: It will allow a user to authenticate i.e log in if he already has an account in 
order to be able to access some features of the app.
* Logout: It will allow a user to log out of his account in order to secure his profile/personal information from unauthorised users
* It has a feature that saves a user's delivery info in his profile if he opts in using the check box provided for a faster checkout any time he visits the store again. 
* If a user is logged in while purchasing product(s) and his delivery details has been saved the first time he made an order, during checkout, the delivery details which has been saved already in the user's profile info will be pre-filled in the delivery details section in order to check out faster 
* It will allow a non-registered or not logged in user to purchase products and checkout as a guest user

---

User Experience (UX)

* User stories

First Time User Goals

a) As a First Time User, I want to easily understand the main purpose of the site and the app to be intuitive so I can navigate through the site easily without any ambiguity. 

b) As a First Time User, I want to be able to register/sign up for an account in order to have a personal account that will allow me view my profile.  

c) As a First Time User, I want to be able to access information through their social media links to see their followings on social media to determine how trusted and known the app is.

Registered User Goals

a) As a Registered User who is logged in, I want to be able to save my shipping details so that I can check out faster anytime I shop again.

b) As a Registered User who is logged in, I want to be able to have a personalised user profile so that I can view my personalised order history, order confirmation and save my payment information. 

c) As a Registered User, I want to be able to log in to my account so that I can access my personal account information.

d) As a Registered User who is logged in, I want to be able to log out of my account so that my account can be safe from unauthorised access.

---

Registered & Guest User Goals

a) As a Registered, First time or Returning Guest User, I want to be able to easily see the image, name, price, rating & category of the product I want to buy in order to know that I'm buying the right product at the price I can afford.

b) As a Registered, First time or Returning Guest User, I want to be able to quickly identify deals, clearance items and special offers in order to take advantage of special savings on products I'd like to purchase.

c) As a Registered, First time or Returning Guest User, I want to be able to easily view the total of my purchase at any time so that I can avoid spending too much.

d) As a Registered, First time or Returning Guest User, I want to be able to view all available products in order to select some for purchase.

e) As a Registered, First time or Returning Guest User, I want to be able to easily check out in order to purchase products without logging in or setting up an account.

f) As a Registered, First time or Returning Guest User, I want to be able to easily delete product(s) in the cart in order to have the choice to remove it if not needed anymore.

g) As a Registered, First time or Returning Guest User, I want to be able to edit products in the cart in order to adjust it any time if I change my mind.

h) As a Registered, First time or Returning Guest User, I want to be able to view products in the cart in order to know what I'm purchasing.

i) As a Registered, First time or Returning Guest User, I want to be able to add product/products to the cart in order to purchase a single one or check out multiple items in one click.

j) As a Registered, First time or Returning Guest User, I want to be able to access information through their social media links to see their followings on social media to determine how trusted and known the app is.

---

Admin User Goals

a) As an Admin User, I want to be able to log into my account in order to have the authorised access to manage products in the database.

b) As an Admin User, I want to be able to log out of my account in order to protect it from unauthorised access.

c) As an Admin User, I want to be able to manage products within the store i.e create, read, update & delete products into/from the database so that users of the website can enjoy a good user experience when interacting with the site.

---

# Design

* Colour Scheme

The two main colours used in this app are Pink and White in order to get a good contrast, enhance usability and make users enjoy a great User experience. The choice of pink is borne out of the fact that since it's a girly website that deals with wigs & wigcare products and pink is loved by most women, I decided to go for this with a contrast of white for the font colour. The background colour used for the navigation bar and footer sections is Pink with font colour of white for the texts while for the content area, the home page has a background image while the rest of the pages have a background colour of white with font colour of black.

* Typography

The Roboto font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the Roboto font isn't being imported into the site correctly. The Roboto typeface is elegant and renders well on high-resolution screens such as Android phones and as such, it’s a perfect fit for many applications.  

* Imagery

The major image in this app is the one used as background image for the home page. The products and product detail pages also have images but those are must haves since it's an e-commerce site that sells physical products that must be displayed for users to see and choose. The logo used for this app is not an image logo but rather, the name of the app/site is used as the logo and if clicked, takes the user back to the home page.

---

# Wireframes

For prototyping, the wireframes were designed manually by hand without using any automated tool in order to bring this idea to life. See screenshots below:

Home/Landing Page for Mobile Screen sizes:
![Home/Landing Page](documentation/wireframes/home_page_mobile_screen.jpg)

Home/Landing Page for Medium & Large Screen sizes:
![Home/Landing Page](documentation/wireframes/home_page_md_lg_screen.jpg)

All Products Page for Small Screen sizes: 
![All Products Page](documentation/wireframes/all_prod_page_sm_screen.jpg)

All Products Page for Medium & Large Screen sizes: 
![All Products Page](documentation/wireframes/all_products_page_md_lg_screen.jpg)

All Products Page for Extra Small Screen sizes,
Product Description Page for Small & Medium Screen sizes: 
![All Products & Product Description Pages](documentation/wireframes/all_prod_pg_xs_n_prod_desc_pg_sm_md_screens.jpg)

Shopping Cart Page for Small Screen sizes: 
![Shopping Cart Page](documentation/wireframes/shopping_cart_page_sm_screen.jpg)

Shopping Cart Page for Medium & Large Screen sizes: 
![Shopping Cart Page](documentation/wireframes/shopping_cart_page_md_lg_screen.jpg)

Checkout Page for Small & Medium Screen sizes: 
![Checkout Page](documentation/wireframes/checkout_page_sm_md_screen.jpg)

Checkout Page for Large Screen sizes: 
![Checkout Page](documentation/wireframes/checkout_page_lg_screen.jpg)

Order Confirmation Page for Small Screen sizes: 
![Order Confirmation Page](documentation/wireframes/order_confirm_page_sm_screen.jpg)

Order Confirmation Page for Medium & Large Screen sizes: 
![Order Confirmation Page](documentation/wireframes/order_confirm_page_md_lg_screen.jpg)

---

Agile Approach Used

* The agile planning tool used for my Django app is the Kanban board. I used the board on GitHub for the planning of my wiGalleria e-commerce site project. Three boards are created to represent the 3 iteration phases used to plan this project. 
Each project was created with issues and milestones set. I also used the MoSCoW labelling technique to prioritise my user stories into Must-Have, Should-Have, Could-Have and Won't-Have. At the start, all the user stories are put in the "To do" section of each board, then the Must-Haves are moved into the "In progress" section and once a functionality is completed and everything responds as expected, it's moved to the "Done" section.
The links to these 3 boards are given below:
![kanban board 1 on GitHub](https://github.com/Eb0nY-April14/wigalleria_v1/projects/1) 
![kanban board 2 on GitHub](https://github.com/Eb0nY-April14/wigalleria_v1/projects/2)
![kanban board 3 on GitHub](https://github.com/Eb0nY-April14/wigalleria_v1/projects/3)

---

# Database Schema

This e-commerce store is made up of different apps each with its own model and the database schema below is used to show/describe how these models interact with each other i.e the relationship that exists between objects within the said models. This relationship can either be one to one, one to many or many to many relationship but in this project, they are all one to many.

* View the database Schema below: 

![Database Schema](documentation/database_schema_wigalleria.jpg)

---

# Issues Encountered and Resolved

* There were some issues experienced with the products page after deployment to Heroku. 12 of the products were missing but visible on the development side. I went to the media folder of the aws bucket created for wiGalleria to check if the products names there corresponds to the ones in the media folder on gitpod workspace and discovered that I gave the wrong extension to some i.e .jpg instead of .png, some had name mismatch and as soon as I corrected those, most of the images showed up leaving 2 products missing. I then went to the database through Django admin and re-entered the names of those 2 products checking that they match the ones in aws bucket, then add, commit & push them to GitHub, refreshed the Heroku deployed site and all products images were displayed correctly. See screenshots below:
![Products missing](documentation/bugs/missing_products_screenshots_crop.jpg)

* The stripe webhook failed when I sent a test event to a webhook endpoint. It gave an error message of "Test webhook error: 502" and after thorough checking, two causes were discovered which are:
* The empty variables placeholders I left in the env.py file were preventing Stripe from seeing the stripe keys in there. They were left there in case more environment variables need to be added to my env.py file but I didn't realise quickly enough that this was the root cause that prevents Stripe from seeing the stripe keys in env.py files. 
* Secondly, I placed the env.py in the wrong location i.e in the wigalleria app instead of the root directory. I fixed these issues by commenting the environment variables placeholders out and moving the env.py file to the root directory, then ran the webhook test again & received a successful message this time, it worked. See screenshots below:

![Stripe webhook failed1](documentation/bugs/webhook_test_failed_terminal_error_msg.png)
![Stripe webhook failed2](documentation/bugs/webhooks_error_msg_from_stripe.png)
![Stripe webhook failed3](documentation/bugs/env_py_wigalleria_location.png)

* When an admin user wants to carry out a delete product opertion, there is a confirmation message displayed to him to confirm if he actually wants to delete that product or cancel the delete and return to home. It should specifically mention the name of that product to be deleted so the user can make a choice if to go ahead with the deletion or cancel it but when I tested this feature on completion, it displayed the message quite alright but didn't render the product's name but left it blank. It was discovered that the issue with this was that in my delete_product function view views.py, I didn't render the product got by the get_object() function in a context so the context had no name of product to render so it displayed an empty quotes (i.e "") but onec I added the product variable name into the context, the issue was solved. See screenshots of before and after below:

![Missing Product name](documentation/bugs/delete_product_missing_var_msg.png)
![Missing Product name](documentation/bugs/delete_product_name_var_missing_out_dev_tools.png)
![Rendered Product name](documentation/bugs/delete_product_complete_var_msg.png)

* Also, I had an issue with the products delete view for an admin user. I included a message that allows an admin user to confirm deletion or cancel before the actual deletion takes place. This was put in place to avoid deletion by mistake but when it was run in the browser, it threw an error with the message "delete view template does not exist". This was due to the fact that I omitted "products/" that should precede the delete_product.html template name in my path name when I was rendering it. According to my file path, the delete_product.html template resides inside the products folder so that should be specifed as "products ---> templates ---> products" directory but as soon as that was corrected, the template rendered appropriately. See screenshot of error message and its solution below:

![Delete template not exist](documentation/bugs/template_not_exist_product_error.png)
![Delete template location](documentation/bugs/delete_button_error_fix.png)
![Delete view not correct](documentation/bugs/delete_product_view_not_correct.png)
![Delete view correct](documentation/bugs/delete_product_view_correct.png)

* An issue erupted during the Heroku deployment. Since the rule is that after connecting to Postgres, we must run migrations again using the commands "showmigrations" & "migrate" afterwards. I ran the showmigrations successfully but when I put in the terminal the "migrate" command, it threw an error that says "AssertionError: database connection isn't set to UTC". I then googled for this issue to find the cause & possible solutions to this sort of error and found a very helpful resource on stackoverflow which explained that this issue was caused as a result of a recent update to version 2.9 of psycopg2 as explained in this GitHub issue: 
[GitHub Link to resolve database UTC Issue](https://github.com/psycopg/psycopg2/issues/1293#issuecomment-862835147)

* The solution given to this problem on stackoverflow is to downgrade psycopg2 (or psycopg2-binary if you are using the stand-alone package) below 2.9 (e.g. psycopg2>=2.8,<2.9) in your requirements file e.g downgrade to 2.8.6 using: pip3 install psycopg2==2.8.6
I did that and the issue was resolved. 
The link to the solution on stackoverflow is below:
[stackoverflow Link to resolve database UTC Issue](https://stackoverflow.com/questions/68024060/assertionerror-database-connection-isnt-set-to-utc)

* After creating the footer code in my base.html template and viewed it in the browser, I found out that it didn't display at the right location. It was joined together with the navbar section at the top of each page instead of the bottom. I tried playing around with the chunk of the footer code by moving it from one section to the other to see if that would resolve the issue but it didn't so I had to contact Code Institute tutor support for help. It was there that the tutor pointed my attention to where I placed the footer, immediately after the closing head tag and ignoring the block content code there. In the tutor's words: 
"The main content and the header is actually below the footer, please look at line starting 181 - 185 in base.html, I believe that should be moved to line 147". I followed his instruction, viewed my code in the browser and found out that the footer has rightly moved to the bottom across all pages. See screenshots below:

![Footer code placed at wrong Location](document/bugs/footer_code_placed_at_wrong_location.png)
![Footer code placed at right Location](document/bugs/footer_code_placed_at_right_location.png)
![Footer code placed at wrong Position](document/bugs/footer_code_placed_wrongly_in_base_template.png)
![Template showing footer at wrong Location](document/bugs/footer_section_in_base_template_show_wrongly.png)
![Template showing footer at right Location](document/bugs/footer_section_in_base_template_show_rightly.png)

* Another issue was encountered during the implementation of Stripe payment for my project. I created the payment intent in my checkout views.py but when I opened it in the browser to check it out, it broke my checkout page giving an error that says "Authenticationerror at checkout. You did not provide an API key. You need to provide your API key in the Authorization header, using Bearer auth (e.g. 'Authorization: Bearer YOUR_SECRET_KEY')". I tried to solve this issue but was unable to so I contacted tutor support and after much troubleshooting, she noticed that 'env.py' file is not being read correctly in settings.py. On a closer look by the tutor and her colleague, it was discovered that the error was caused as a result of the empty variables set with no name and values in env.py file. Commenting out all these empty variables in env.py file solved the issue and the code ran successfully.
See screenshots below:
![Authentication Error at Checkout](documentation/bugs/authentication_error_at_wigalleria_checkout.png)
![Solution to Authentication Error at Checkout](documentation/bugs/webhook_test_failed_terminal_error_msg.png) 

---

# Technologies Used

* Languages Used

* HTML, CSS and JavaScript for front-end development

* Python for backend development

---

Frameworks, Libraries and Programs Used

1. Git

* Git was used for version control by utilising the Gitpod terminal to commit to Git and push to GitHub.

2. GitHub

* GitHub was used to store the project's code after being pushed from Git.

3. Bootstrap 4.1.3 & Custom CSS

* Bootstrap 4 and custom made CSS files were used to assist with the responsiveness and styling of the website.

4. Django & Jinja templating Language

* The entire project anchors on this framework as it was used to build this app

5. Amazon S3 Bucket

* S3 Bucket was used to host static and media files that will be needed for storing products images, background image and CSS files. Since Heroku can't serve static and media files on its own but works seamlessly with amazon S3 bucket, an aws account has to be created and S3 bucket created within it so that all static and media files can be uploaded there and it can serve all the static files on Heroku as it works well with it.

6. Roboto Google Fonts:

* They were used on all pages throughout the project.

7. Font Awesome:

* Font Awesome was used to add social media, shopping cart and all other icons across all pages throughout the app for excellent UX.

8. jQuery:

* jQuery came with Bootstrap to make the navbar responsive.

9. Windows 10 built-in Photo Editor:

* This was used to resize the logo used on all page across the app.     

---

## Testing

To view all testing documentation, click to view the [TESTING.md](TESTING.md) file.

# Deployment

* Firstly, visit Heroku website to sign up for a free account at https://heroku.com/ 

* Create an account by clicking the "Sign Up" button and provide your details as required.

* Heroku sends an activation link to the email you provided so open that email, click on the link and it will take you to the Heroku site. 

* Enter your password and confirm it, then hit the "save" button.

* Heroku then takes you to the dashboard where you can create your first app

* To create your first app, you can either click on the "Create new app" button located in the middle of the page or on the "New" button located on the top right corner of the page and select "Create new app" option from the drop down box. Then, give your app a name and choose the region/location nearest to you e.g Europe and click on the "Create app" button. 

* To add a database, click on the "Resources" tab located at the top of the page. In the "Add-ons" section of the page, search for "postgres" using the search box provided and select "Heroku Postgres" to add it to your app. It then displays another popup box to select your plan, the default is free plan so leave it that way and click on the 'Submit Order Form' button provided.

* To use Postgres, go back to your Gitpod IDE and at the terminal, install 'dj_database_url' first and 'psycopg2-binary' next using pip3 install command i.e
pip3 install dj_database_url and press the Enter key at the keyboard. Do same for the other package

* Freeze the requirements with the command: pip3 freeze > requirements.txt
This will ensure that Heroku installs all our apps requirements when it's deployed.

* NOTE: Ensure that all your secret environment variables (keys and values pair) such as DATABASE_URL, secret keys, stripe keys etc are safely stored in your env.py file and the env.py added to .gitignore file so it will not end up in version control and be publicly visible to everyone. To set all thses variables, do the following:  

* Now that the database is added, go back to Heroku "Settings" tab and click on "Reveal Config Vars" button. This will provide the "DATABASE_URL" which is the connection to your Postgres database so copy the string in the box beside the "DATABASE_URL" box and store it somewhere as it will be added to your project later.

* Go back to your code and in the same directory as the "manage.py" file, create a file called "env.py" which will be used to store your secret environment variables" as these variables must be hidden and should not be publicly visible. Add your "env.py" file to the ".gitignore" file so that when you push your code to GitHub, the secret environment variables and secret keys will not be visible for everyone to see. 

In the "env.py" file, import the os (operating system) library and use it to set a couple of environment variables which are:

i. Set "DATABASE_URL" and then paste in the URL copied from Heroku earlier i.e
os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link" 

ii. Add your secret key as this should not be visible on GitHub too. It will be made up by you and can comprise of whatever you like or search for secret key generator tool online and use it to generate one. An example of how to add it is shown below:
os.environ["SECRET_KEY"] = "Make up a randomSecretKey" 

iii. Save the env file

* Copy the "SECRET_KEY" value above and add it to your "Config Vars" on Heroku so go back to Heroku dashboard, click on the "Settings" tab and under the "Config Vars" section, click on the "Reveal Config Vars" button once again. In the first pair of empty text box provided, type "SECRET_KEY" in one and its value copied earlier from "env.py" file into the other box i.e 
SECRET_KEY, “randomSecretKey” and click the "Add" button next to it. Repeat same with all your stripe public and secret keys i.e PUBLIC_KEY, SECRET_KEY, STRIPE_SECRET_KEY and STRIPE_WH_SECRET

* Next, reference "env.py" file in the "settings.py" file and do a few imports so go back to "settings.py" file and at the top of the file and undrneath the first import (i.e from pathlib import Path), type the following to import them: 
import os
import dj_database_url
if os.path.isfile("env.py"):
import env

* In the "SECRET_KEY" section a little further down in the same settings.py file, remove the insecure secret key that is presently there and replace it with the new and secured "SECRET_KEY". Do same with the other keys too for security purpose i.e
SECRET_KEY = os.environ.get('SECRET_KEY')

* To set up wiGalleria store's new database, go to settings.py file and import dj_database_url. Down in the "DATABASES" section of settings.py file, comment out the default configuration and replace it with 'dj_database_url.parse()'. Inside the empty parenthesis, type in the database url from Heroku e.g 'dj_database_url.parse(postgres://mexamr......)'.
This url can be obtained from either your config variables in your Heroku app's settings tab or the command line by typing 'Heroku Config' and then press the enter key. Save this and you're now ready to connect to your new Heroku database and run migrations.

* Run all migrations again since you're connecting to Postgres now using the following commands one after the other:
python3 manage.py showmigrations and press enter key
python3 manage.py migrate and press enter key
This last command will apply all those migrations and get your database setup

* if a 'fixtures' file was used to populate your database with products in the local environment (development side), then it'll be used again by first loading in the 'categories' and then the 'products' in that order since the products depend on the categories already existing. 
To load the categories, use:
python3 manage.py loaddata categories and press enter key 
Next, to load the products, use:
python3 manage.py loaddata products and press enter key

* Finally, create a superuser to log in with using the command:
python3 manage.py createsuperuser and press enter key

* Before committing all these changes to GitHub, remove the Heroku database config added earlier in settings.py file and uncomment the one commented out earlier too so that the database URL doesn't end up in version control. Then commit your code to GitHub.

* Then under 'DATABASES' section in settings.py file, use an if statement so that when your app is running on Heroku where the database URL environment variable is defined, it will connect to Postgres otherwise (i.e in local development environment), it'll connect to sqlite which is the local DB.

* To make the deployment work on first try, other things must be installed amongst which is gunicorn. Install this using the command:
pip3 install gunicorn and press the Enter key
Then freeze it into your requirements.txt file using the command:
pip3 freeze > requirements.txt and press the Enter key

* Create your Procfile in the root directory of your file structure which means that it should be at the same level as your README.md file. To create this, right-click on any empty space in the file explorer and select 'New File', give it the name 'Procfile' with a capital P or else it won't work. Open the file up and type this into it:
web: gunicorn PROJ_NAME.wsgi:application
Don't forget to replace PROJ_NAME with the name of your project as shown below:
web: gunicorn wigalleria.wsgi:application
The content of this Procfile tells Heroku to create a web dyno which will run gunicorn and serve your django app.

* At the terminal prompt, type: heroku login -i and press the enter key
It will prompt for your heroku login details so type them in at the terminal as requested.

* Lastly, disable collectstatic temporarily by typing this command at the terminal: 
heroku config:set DISABLE_COLLECTSTATIC=1 and press the enter key
NOTE: If there is more than one app, don't forget to include the --app flag and the name of your app e.g wigalleria when typing the collctstatic command as shown below: 
heroku config:set DISABLE_COLLECTSTATIC=1 --app <TYPE NAME OF YOUR APP HERE> and press the enter key
This ensures that Heroku won't try to collect static files that does not exist yet during first deployment.

* Add the hostname of your Heroku app to 'ALLOWED_HOSTS' in settings.py file, the hostname is your deployed Heroku URL link so either copy it from the 'Settings' tab in Heroku or the live site & paste it in here. Add in the name 'localhost' there too separated by a comma so that Gitpod will still work too i.e:
ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]. Example is below:
ALLOWED_HOSTS = ['cyot14-wigalleria.herokuapp.com', 'localhost']

* Attempt to deploy your app by adding, committing and pushing your code to your repository using the following commands:
git add .
git commit -m Initial Commit”
git push

* Then use the command below to deploy to Heroku:
git push heroku main and press the enter key

NOTE: If an error occurs which says 'fatal', then you have to initialise your heroku git remote if the app was created on the Heroku website rather than the CLI as that's the cause of the error. To initialise your heroku git remote, use this command at the terminal:
heroku git:remote -a <TYPE YOUR APP NAME HERE> and press the enter key. Then repeat the command below again to deploy to Heroku:
git push heroku main and press the enter key

If it throws an error again that says "Push rejected, source repository is a shallow one. Unshallow it with 'git fetch --all --unshallow'", then you have to do the deployment manually instead of automatic deployment by going to your Heroku app and click the 'Deploy' tab. Under the 'Deployment method', click on the 'GitHub ---> Connect to GitHub' option, then search in the text box provided for your repository name and click on the 'Search' button, then on the 'Connect' button beside it to connect your GitHub account to Heroku. 

* In the 'Manual Deploy' section, click on the 'Deploy Branch' button and Heroku will start building your app. Go to the 'Activity' tab and click on the "View Build log" link in order to view logs of activity and be able to watch the deployment as it's happening in the build log. It will pop this out in a full view page for you to see. It will display 'Build finish' once it's successfully built and the URL of the deployed site too with a message that says 'deployed to Heroku'.

* Finally, to view the deployed site live, there are two ways to get the link of the deployed site. It's available under the 'Activity' and 'Settings' tabs. From the 'Activity' tab, copy the link, open a new tab and paste it in. The second way is to go to 'Settings' tab, scroll down the page and under the 'Domains' heading, the link to your newly deployed app/site will be displayed there. Click on that link and it will open your live site in a new tab but without any static files yet. That will be fixed when you set up the Amazon aws S3 Bucket for storing your static and media files later on. 

* If those two errors above did not occur in your case, then skip those steps above that deals with the errors and proceed to set up automatic deploy. To set your app up to automatically deploy when you push to GitHub, go to your app in Heroku and on the 'Deploy' tab, set it to "Connect to GitHub". Next, search for your repository and click on "Connect" button, then click on "Enable Automatic Deploys" button to activate automatic deployment. This ensures that whenever you push to GitHub, your code will automatically be deployed to Heroku as well.

* To test if your automatic deployment works, make a minor change to your code in your Gitpod workspace and push to GitHub. Then go to your Heroku app and select on your app, click on the 'Activity' tab and you'll see that there's a build in progress whuch shows that your automatic deployment is working. 

View the live project [here](https://cyot14-wigalleria.herokuapp.com/)
View the GitHub Repository [here](https://github.com/Eb0nY-April14/wigalleria_v1)

---








    # Web Marketing

    * Out of all the web marketing strategies available for marketing e-commerce sites, Facebook was chosen to market this wiGalleria website because it has a wider reach to target customers and is also a social media platform mostly used by ladies/women. Since wiGalleria is an online wig store, it feels appropriate to target our customers through this social media platform. The Facebook page called wiGalleria has been created with the necessary information such as link to deployed site on Heroku, physical address/location of the business, phone number and shop now button provided to customers. The link to wiGalleria Facebook page is provided below:

    [wiGalleria Facebook Page Link](https://www.facebook.com/wiGalleria-110791034831427/) 

    Also, the screenshots of my wiGalleria Facebook Page are below:

    ![wiGalleria Facebook Page Screenshots](documentation/facebook_page_screenshots/wigalleria_facebook_page1.png)
    ![wiGalleria Facebook Page Screenshots](documentation/facebook_page_screenshots/wigalleria_facebook_page2.png)
    ![wiGalleria Facebook Page Screenshots](documentation/facebook_page_screenshots/wigalleria_facebook_page3.png)
    ![wiGalleria Facebook Page Screenshots](documentation/facebook_page_screenshots/wigalleria_facebook_page4.png)
    ![wiGalleria Facebook Page Screenshots](documentation/facebook_page_screenshots/wigalleria_facebook_page5.png)
    ![wiGalleria Facebook Page Screenshots](documentation/facebook_page_screenshots/wigalleria_facebook_page6.png)
    ![wiGalleria Facebook Page Screenshots](documentation/facebook_page_screenshots/wigalleria_facebook_page7.png)
    ![wiGalleria Facebook Page Screenshots](documentation/facebook_page_screenshots/wigalleria_facebook_page8.png)