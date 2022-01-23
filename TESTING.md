# TESTING

## Validator Testing

[PEP8 online validator](https://www.pep8online.com)

This tool was used to validate my .py files to ensure there are no syntax errors or improper code indentation. They passed the test as seen in the screenshots below:

* cart/apps.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/cart-apps.py.png)

* cart/contexts.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/cart-contexts.py.png)

* cart/templatetags/cart_tools.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/cart-templatetags-cart_tools.py.png)

* cart/urls.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/cart-urls.py.png)

* cart/views.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/cart-views.py.png)

* checkout/admin.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/checkout-admin.py.png)

* checkout/apps.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/checkout-apps.py.png)

* checkout/forms.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/checkout-forms.py.png)

* checkout/models.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/checkout-models.py.png)

* checkout/signals.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/checkout-signals.py.png)

* checkout/urls.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/checkout-urls.py.png)

* checkout/views.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/checkout-views.py.png)

* checkout/webhook_handler.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/checkout-webhook_handler.py.png)

* checkout/webhooks.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/checkout-webhooks.py.png)

* home/apps.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/home-apps.py.png)

* home/urls.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/home-urls.py.png)

* home/views.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/home-views.py.png)

* products/admin.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/products-admin.py.png)

* products/apps.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/products-apps.py.png)

* products/forms.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/products-forms.py.png)

* products/models.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/products-models.py.png)

* products/urls.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/products-urls.py.png)

* products/views.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/products-views.py.png)

* products/widgets.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/products-widgets.py.png)

* profiles/apps.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/profiles-apps.py.png)

* profiles/forms.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/profiles-forms.py.png)

* profiles/models.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/profiles-models.py.png)

* profiles/urls.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/profiles-urls.py.png)

* profiles/views.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/profiles-views.py.png)

* wigalleria/asgi.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/wigalleria-asgi.py.png)

* wigalleria/custom_storages.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/wigalleria-custom_storages.py.png)

* wigalleria/settings.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/wigalleria-settings.py.png)

* wigalleria/urls.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/wigalleria-urls.py.png)

* wigalleria/wsgi.py:
![PEP8 Validator Testing](documentation/validation/pep8_validation/wigalleria-wsgi.py.png)

[w3html validator](https://validator.w3.org) 

This tool was used to validate all my html templates and I got just two warnings on the checkout page about type attribute not necessary on javascript resource while the rest of the pages are free of errors and warnings. as_p }}. Here below are the screenshots of the validations:

* cart/templates/cart/cart.html Page:

![shopping cart page](documentation/validation/w3html_validation/cart-templates-cart-cart.html.png)

* checkout/templates/checkout/checkout_success.html Page:

![checkout success page](documentation/validation/w3html_validation/      .png)

* checkout/templates/checkout/checkout.html Page:

![checkout page](documentation/validation/w3html_validation/       .png)

* home/templates/home/index.html Page:

![home page](documentation/validation/w3html_validation/       .png)

* products/templates/products/add_comment.html Page:

![add comment page](documentation/validation/w3html_validation/      .png)

* Logout Page:

![logout page](documentation/validation/w3html_validation/html_validator_logout_page.png)

* Register/Sign Up Page:

*  I'm aware that there were some errors found by the w3html validator in the Register template, this is NOT my form code but has to do with the Django built in form template used. Since I used the Django built-in {{ form.as_p }} and my code input in this page is very minimal, the error isn't from any written code of mine. My findings however showed that the built-in Django forms template has the following issues:

* Screenshot #1 below was obtained by opening the DevTools on the Register page. It shows that there's an opening 'paragraph' (i.e p) tag element that is used for the Password Field which has a corresponding closing 'paragraph' tag element and same with the 'span' tag and all other element tags within the django form. They all have their matching tags in place as seen in the screenshot below:

![register.html code screenshot from gitpod workspace](documentation/validation/w3html_validation/register_page_dev_tool_code_inspect_screenshot.png)

* Screenshot #2 below is the HTML validator result that shows it's expecting a closing 'paragraph' (i.e p) tag, but instead saw the opening 'unordered list' (i.e ul) element. Since 'ul' elements cannot be direct children of 'p' tags... they're both block-elements, so they cannot be nested inside of each other. This is the reason why the validator thinks a closing 'p' tag should be seen BEFORE the 'ul' is started and therefore flags these chain of errors.
With this logic however, the Django built-in {{ form.as_p }} generator is actually incorrect, semantically. See screenshot below:

![register/signup page error screenshot](documentation/validation/w3html_validation/html_validator_error_screenshot_for_register_page.png)


[w3CSS validator](http://jigsaw.w3.org/css-validator/)

This tool was used to validate my custom css code and it passed successfully. See screenshot below:

* Custom CSS (style.css):

![custom css validation](documentation/validation/w3css_validation/shoppinglist_app_custom_css_validator_result.png)


### Manual Testing of shoppinglist|planner app Functionalities 

* Testing User Stories from User Experience (UX) Section

First Time User Goals

i. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the app

a) When a visitor clicks on the app's url and since he's not registered, he lands on the welcome page where extensive details about the app is given so he can read through to get an understanding of the main purpose of the site and learn more about the app. See screenshot below:

![Visitors Welcome Page](documentation/views/welcome_page_visitors.png)

---

ii. As a First Time Visitor, I want to be able to sign up for an account in order to enjoy all the features of the app. 

a) When a user clicks on the app link or copies it into any search box such as Google engine, he lands on the welcome page. At the top right side of this page are the nav links, one of which is the "Register" link as seen in the screenshot below:

![Welcome Page Screenshot](documentation/views/welcome_page_screenshot1.png)
![welcomePage Screenshot](documentation/views/welcome_page_screenshot2.png)

b) If he clicks on the "Register" link, he is taken to the "Sign Up" form page where he can fill in his details as seen in the screenshot below: 

![SignUp Page Screenshot](documentation/views/signup_page_screenshot1.png)
![SignUp Page Screenshot](documentation/views/signup_page_screenshot2.png) 

---

iii. As a First Time Visitor, I want to be able to access information through their social media links to see their followings on social media to determine how trusted and known the app is.

a) The social media icons are located in the footer section (i.e bottom) of the welcome Page for both unregistered and not logged in Users to have access. See screenshot below:

Footer Section:

![Social Media Links](documentation/views/footer_social_media_links.png)

---

Registered User Goals

i. As a Registered User who is logged in, I want to be able to view my shopping list and see what items I have purchased and the ones left. 

a) User logs in and if successful, he is redirected to the home page where he can view his shopping list as seen in the screenshots below:

![homePage/viewShoppingList Screenshot](documentation/views/view_shoppinglist_screenshot1.png)
![homePage/viewShoppingList Screenshot](documentation/views/view_shoppinglist_screenshot2.png)
![homePage/viewShoppingList Screenshot](documentation/views/view_shoppinglist_screenshot3.png)

---

ii. As a Registered User who is logged in, I want to be able to add a new item to my shopping list and view them during shopping.

a) The User will find the "Add an item" button close to the footer section of the home page. See screenshot below: 

![AddItemButton Screenshot](documentation/views/add_item_button_screenshot.png)

b) On clicking the "Add an item" button, he is taken to the add item's form page and if he fills the form and submits it, the new item is added to the shopping list in the database and he is taken back to the home page where he'll see his newly added item. See the screenshots below:  

![AddItemPage Screenshot](documentation/views/add_item_page_screenshot1.png)
![AddItemPage Screenshot](documentation/views/add_item_page_screenshot2.png)

---

iii. As a Registered User who is logged in, I want to be able to login to my account and add, view, modify or delete an item in my shopping list or delete my entire list.

a) When a user clicks on the app link or copies it into any search box such as Google, he lands on the welcome page. At the top right side of this page are the nav links, one of which is the "Login" link as seen in the screenshot below:

![WelcomePage Screenshot](documentation/views/welcome_page_screenshot1.png)
![welcomePage Screenshot](documentation/views/welcome_page_screenshot2.png)

b) When he clicks on the "Login" link, he is taken to the login form page where he can fill in his details and if correct, he logs in successfully. See screenshot below: 

![LoginPage Screenshot](documentation/views/login_page_screenshot1.png)
![LoginPage Screenshot](documentation/views/login_page_screenshot2.png)
![LoginSuccess Screenshot](documentation/views/login_success_message_display_screenshot.png)

---

iv. As a Registered User who is logged in, I want to be able to mark an item in my list as either bought or unbought. 

a) The third button beside each item on the home/viewing page is the one for toggling an item to mark it as either done when it's purchased or not. When the button is clicked, it strikes out the item as "bought" and is moved to the bottom of the row and if clicked again, the "strike out" mark is removed & the item is moved back up which means it hasn't been bought yet. See screenshot below:

Items marked as unbought: 
![UnstrikeNotBoughtItem Screenshot](documentation/views/not_bought_item_screenshot.png)

Items marked as bought: 
![StrikeOutBoughtItem Screenshot](documentation/views/bought_item_screenshot.png)

---

v. As a Registered User who is logged in, I want to be able to logout of my account to keep my information private and secure.

a) The "Logout" link is displayed to the user on the nav bar at the top right side of the home page once he is authenticated. See screenshot below:

![LogoutPage Screenshot](documentation/views/logout_link_screenshot.png)

b) When he clicks on the "Logout" link, he is logged out of his account and a message is displayed to confirm his successful logout operation as seen in the screenshot below:

![LogoutPage Screenshot](documentation/views/logout_message_screenshot.png) 

---

vi. As a Registered User who is logged in, I want to be able to retrieve and make changes on any item on my shopping list.

a) The first button beside each item on the home/viewing page is the "Edit item" button which the User needs for updating an item in the database as shown in the screenshot below: 

![EditItemButton Screenshot](documentation/views/edit_item_button_screenshot.png)

b) On clicking the "Edit item" button, the User is taken to the edit item's form page where the input fields are prepopulated with their current values in the database and waiting for the user to make changes to the relevant field(s). After making his desired changes, he clicks on the "Update item" button and the changes are made in the database and user is redirected back to the home page to view his shopping list in order to confirm that the changes has actually been made. See screenshot below:

![EditItemPage Screenshot](documentation/views/edit_item_page_screenshot1.png)
![EditItemPage Screenshot](documentation/views/edit_item_page_screenshot2.png)

---

vii. As a Registered User who is logged in, I want to be able to remove a purchased item from the list to avoid the mistake of repurchasing it.

a) The second button beside each item on the home/viewing page is the "Delete item" button which the User needs for removing/deleting an item in the database as shown in the screenshot below: 

![DeleteItemButton Screenshot](documentation/views/delete_item_button_screenshot.png)

b) When he clicks on the "Delete item" button, another page that contains a confirmation message is displayed to the user and if he confirms with the "Delete item" button again, the item is removed from the database. See screenshot below:

![DeleteItemMessage Screenshot](documentation/views/delete_item_message_confirm_screenshot.png)

---

viii. As a Registered User who is logged in, I want to be able to delete my list and have a blank space to start a new list.

a) The User will find the "Delete List" button beside the "Add an item" button close to the footer section of the home page and if clicked, the entire shopping list is deleted outrightly and a blank page is displayed back to the user to show that his list has been deleted. See screenshot below: 

![DeleteListButton Screenshot](documentation/views/delete_list_button_screenshot.png)

---

ix. As a Registered User who is logged in, I want to be able to enter my item's quantity and unit price and get the total price calculated and displayed automatically.

a) When the "Add an item" form page is displayed to the User, he enters the item name, unit price and quantity in the appropriate fields and when he moves the cursor into the input box for the total price field, it automatically gets populated with the total price for that particular item as seen in the screenshot below:

![AutoCalculateTotalPrice Screenshot](documentation/views/auto_calc_total_price_add_item_page_screenshot.png) 

b) Similar process as "Add an item" also goes for the "Edit an item" operation. Find below the screenshot taken before the item was updated:

![BeforeEditItemOperation Screenshot](documentation/views/before_edit_item_operation_page_screenshot.png) 

c) When the User changes the values for both the "unit price" and "quantity", the total price is automatically calculated and its field populated with the right amount as seen in the screenshot below: 

![AutoCalculateTotalPrice Screenshot](documentation/views/auto_calc_price_qty_change_edit_item_screenshot.png) 

d)  When the User changes the value for the "unit price" only, the total price is automatically calculated and its field populated with the right amount as seen in the screenshot below: 

![AutoCalculateTotalPrice Screenshot](documentation/views/auto_calc_price_change_edit_item_screenshot.png) 

e) When the User changes the value for the "quantity" only, the total price is automatically calculated and its field populated with the right amount as seen in the screenshot below: 

![AutoCalculateTotalPrice Screenshot](documentation/views/auto_calc_qty_change_edit_item_screenshot.png) 

---

### Manual Testing of JavaScript function that calculates the total price of an item. 

When a user adds a new item or edits one, this function calculates the total price automatically and populates the "total_price" field with the result. The screenshots below are the add item and edit item templates, the calculated & prepopulated value of total price showing that it is calculated correctly and the JSHint Validator result. 

i. add item Page:
![Screenshot of Calculate TotalPrice on add_item Page](documentation/views/add_item_calc_total_price_screenshot.png)

ii. edit item Page before the edit operation:
![Screenshot of Calculate TotalPrice on edit_item Page](documentation/views/before_edit_item_calc_total_price_screenshot.png)

iii. edit item Page after the edit operation:
![Screenshot of Calculate TotalPrice on edit_item Page](documentation/views/after_edit_item_calc_total_price_screenshot.png)

iv. JavaScript Function that calculates Total Price:
![Screenshot of JSHint Validator Result](documentation/validation/jshint_validation/jshint_javascript_validation.png)
