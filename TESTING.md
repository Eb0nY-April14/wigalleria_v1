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

This tool was used to validate all my html templates and I got just two warnings on the checkout page about type attribute not necessary on javascript resource while the rest of the pages are free of errors and warnings. See screenshots below:

* cart/templates/cart/cart.html Page:

![shopping cart page](documentation/validation/w3html_validation/cart-templates-cart-cart.html.png)

* checkout/templates/checkout/checkout_success.html Page:

![checkout success page](documentation/validation/w3html_validation/checkout-templates-checkout-checkout_success.html.png)

* checkout/templates/checkout/checkout.html Page:

![checkout page](documentation/validation/w3html_validation/checkout-templates-checkout-checkout.html.png)

* home/templates/home/index.html Page:

![home page](documentation/validation/w3html_validation/home-templates-home-index.html.png)

* products/templates/products/add_comment.html Page:

![add comment page](documentation/validation/w3html_validation/products-templates-products-add_comment.html.png)

* products/templates/products/add_product.html Page:

![add product page](documentation/validation/w3html_validation/products-templates-products-add_product.html.png)

* products/templates/products/delete_product.html Page:

![delete product page](documentation/validation/w3html_validation/products-templates-products-delete_product.html.png)

* products/templates/products/edit_product.html

![edit product page](documentation/validation/w3html_validation/products-templates-products-edit_products.html.png)

* products/templates/products/product_detail.html

![product detail page](documentation/validation/w3html_validation/products-templates-products-product_detail.html.png)

* products/templates/products/products.html
![products page](documentation/validation/w3html_validation/products-templates-products-products.html.png)

* products/templates/products/user_wish_list.html
![user wish list page](documentation/validation/w3html_validation/products-templates-products-user_wish_list.html.png)

![user profile page](documentation/validation/w3html_validation/profiles-templates-profiles-profile.html.png)


[w3CSS validator](http://jigsaw.w3.org/css-validator/)

This tool was used to validate my custom css code and it passed successfully. See screenshot below:

* Custom CSS (checkout/static/checkout/css/checkout.css):

![checkout css validation](documentation/validation/w3css_validation/checkout-static-checkout-css-checkout.css.png)

* Custom CSS (profiles/static/profiles/css/profile.css):

![profile css validation](documentation/validation/w3css_validation/profiles-static-profiles-css-profile.css.png)

* Custom CSS (static/css/base.css):

![profile css validation](documentation/validation/w3css_validation/static-css-base.css.png)

[JSHint validator](https://jshint.com/)

This tool was used to validate my javascript code and they passed successfully. See screenshots below:

![checkout js stripe elements validation](documentation/validation/js_validation/checkout-static-checkout-js-js_stripe_elements1.js.png)

![checkout js stripe elements validation](documentation/validation/js_validation/checkout-static-checkout-js-js_stripe_elements2.js.png)

![products quantity input script validation](documentation/validation/js_validation/products-templates-products-includes-quantity_input_script.html.png)

---

### Manual Testing of wiGalleria app Functionalities 

* Testing User Stories from User Experience (UX) Section

First Time User Goals

i) As a First Time User, I want to be able to easily understand the main purpose of the site and the app to be intuitive so I can navigate through the site easily without any ambiguity. 

a) The purpose of the site is clearly evident from the first time a user lands on the home page. The name of the app 'wiGalleria' and the 'shop now' button speaks volume about what the site is all about. The flow of each element and its position on each page from the shopping cart and navigation links at the top to the footer at the bottom of the page follows the consistency and uniformity that is obtained on all e-commerce websites which makes it easy for a first time user to get a hang of it quickly. See screenshot of the home page below:

![Site's Main Purpose](documentation/user_stories_testing/main_purpose_of_site1.png)

![Site's Main Purpose](documentation/user_stories_testing/main_purpose_of_site2.png)

First Time or Guest User Goals

i) As a First Time or Guest User, I want to be able to register/sign up for an account in order to have a personal account that will allow me view my profile. 

a) On the home page, click on 'My Account' and from the drop-down, click on the 'Register' link and the sign-up page will be displayed to the user. See screenshots below:

![Sign Up Link](documentation/user_stories_testing/guest_user_signup_link.png)

![Sign Up Page](documentation/user_stories_testing/guest_user_signup_page1.png)

![Sign Up Page](documentation/user_stories_testing/guest_user_signup_page2.png)

ii) As a First Time or Guest User, I want to be able to receive confirmation email after registration/signing up for an account.

a) Once the user has successfully signed up for an account, a message is displayed to her to confirm her email address and after that another message is displayed to inform her that an email has been sent to her address in order to finalise the sign up process so go to your email and click on that link provided and all is then set. See screenshots below:

![Confirmation email Page](documentation/user_stories_testing/confirm_email_address.png)

![Confirmation email Page](documentation/user_stories_testing/email_verify.png)

![Confirmation email Page](documentation/user_stories_testing/user_verify_email_sent.png)

Registered User Goals

i) As a Registered User who is logged in, I want to be able to save my shipping details so that when I'm logged in, I can check out faster anytime I shop again.

a) On the checkout page, after the user fills her delivery details, there is a checkbox provided where a user has the option to save her delivery/shipping details to her profile so that when next she shops again, her shipping details will be prepopulated into the right fields. See screenshots below:

![Save Shipping Details](documentation/user_stories_testing/save_shipping_details1.png)

![Save Shipping Details](documentation/user_stories_testing/save_shipping_details2.png)

ii) As a Registered User who is logged in, I want to be able to have a personalised user profile when I'm logged in so that I can view my personalised order history, order confirmation and payment information. 

a) When a user is logged in, she can view her personalised user profile by clicking on 'My Account' and from the drop-down, click 'Profile', then her profile which contains her order history, order confirmation and payment information will be displayed as shown in the screenshots below:

![View User Profile](documentation/user_stories_testing/personalised_user_profile.png)

iii) As a Registered User who is logged in, I want to be able to add general/specific comments relating to a product so that I can convey any general or specific issue I have with the ordering of the product to the seller.

a) From the home page, the 'shop now' button takes the user to the products page or from any other page, click on 'All Products' displayed at the top of the page and from the drop-down, click on 'All Products' again. Then click on a product's image to open that product in a new tab, then scroll down and you will see the comment section where the user can click on the 'Add Comment' link to add comment. See screenshot below: 

![Add Comment Section](documentation/user_stories_testing/add_comment_section1.png)

![Add Comment Section](documentation/user_stories_testing/add_comment_section2.png)

![Add Comment Section](documentation/user_stories_testing/add_comment_section3.png)


iv) As a Registered User who is logged in, I want to be able to review a product so that I can give feedback to the seller on his product.

a) From the home page, the 'shop now' button takes the user to the products page or from any other page, click on 'All Products' displayed at the top of the page and from the drop-down, click on 'All Products' again. Click on a product's image to open that product in a new tab, then scroll down and you will see the review section where the user can select the number of stars she wishes to give a product and/or leave review in the text area provided. See screenshot below: 

![Add Review Section](documentation/user_stories_testing/add_review_section1.png)

![Add Review Section](documentation/user_stories_testing/add_review_section2.png)

![Add Review Section](documentation/user_stories_testing/add_review_section3.png)

v) As a registered user who is logged in I want to be able to like/unlike a product so that I can spot it easily when I want to buy it later/again or mark it down if it wasn't as described by the seller after purchase.

a) From the home page, the 'shop now' button takes the user to the products page or from any other page, click on 'All Products' displayed at the top of the page and from the drop-down, click on 'All Products' again. Click on a product's image to open that product in a new tab, then in the product description area, click on the heart button and toggle it on or off to like or unlike a product.  See screenshot below: 

![Like/Unlike Product](documentation/user_stories_testing/like-unlike_product1.png)

![Like/Unlike Product](documentation/user_stories_testing/like-unlike_product2.png)

vi) As a Registered User who is logged in, I want to be able to log out of my account so that my account can be safe from unauthorised access.

a) From any page that the user is, click on 'My Account' and then on the 'Logout' link, it displays a message to the user to confirm if she wants to sign out and if the user clicks on the 'sign out' button, she is logged out of her account and a pop-up message is displayed to reflect that as shown in the screenshots below:

![Sign out/Log out Page](documentation/user_stories_testing/logout1.png)

![Sign out/Log out Page](documentation/user_stories_testing/logout2.png)

![Sign out/Log out Page](documentation/user_stories_testing/logout3.png)

vii) As a Registered User who is logged in, I want to be able to add product to my wishlist so that I can easily find them for purchase later.

a) On the product detail page, a user can add products to the wishlist by clicking on the 'Add to Wish List' button located underneath the 'Continue Shopping' button. See screenshot below:

![Add Product to Wish List](documentation/user_stories_testing/add_to_wishlist1.png)

![Add Product to Wish List](documentation/user_stories_testing/add_to_wishlist2.png)

viii) As a Registered User who is logged in, I want to be able to view product(s) in my wishlist so that I can be reminded of the product I want to buy later.

a) A user can view products in her wish list in 2 ways, either by clicking on the 'View Wish List' button located underneath the 'Add to Cart' button or by clicking on the heart icon located at the top of the page in the navigation bar area. See screenshots below: 

![View Product in Wish List](documentation/user_stories_testing/view_product_in_wishlist1.png)

![View Product in Wish List](documentation/user_stories_testing/view_product_in_wishlist2.png)

![View Product in Wish List](documentation/user_stories_testing/view_product_in_wishlist3.png)

ix) As a Registered User who is logged in, I want to be able to remove product(s) in my wishlist so that I can free up space to add more products.

a) From any page that the user is, click on the heart icon located at the top of the page in the navigation bar area which will take the user to the wishlist page. The wishlist contains all the products the user saved so to remove any product, click on the 'Remove' button located beside the product you want to remove and it's done. See screenshots below:

![Remove Product from Wish List](documentation/user_stories_testing/remove_from_wishlist1.png)

![Remove Product from Wish List](documentation/user_stories_testing/remove_from_wishlist2.png)

x) As a Registered User, I want to be able to log in to my account so that I can access my personal account information.

a) From any page that the user is, click on 'My Account' located at the top of the page and then on the 'Login' link, it displays the 'sign in' page where she's prompted to fill her details into their appropriate boxes and if they match what's on record, she is successfully logged into her account and a pop-up message is displayed to reflect that. See screenshots below:

![Login Page](documentation/user_stories_testing/login1.png)

![Login Page](documentation/user_stories_testing/login2.png)

![Login Page](documentation/user_stories_testing/login3.png)


xi) As a Registered User, I want to be able to access information through their social media links to see their followings on social media to determine how trusted and known the app is.

a) On most websites, the footer houses the social media icons and links and ours is not an exception so from any page that the user is, scroll down to the bottom of the page and the link to our facebook page is there for the user to use. See screenshot below:

![Social media link on Footer](documentation/user_stories_testing/social_media_link.png)

---

First Time, Registered or Guest User Goals

i) As a First Time, Registered or Guest User, I want to be able to easily see the image, name, price, category, rating & description of the product I want to buy in order to know that I'm buying the right product at the price I can afford.

a) On the product detail page, the user can see all these information displayed to her as seen in the screenshot below:

![Product Attributes on product-detail Page](documentation/user_stories_testing/product_attributes.png)

ii) As a First Time, Registered or Guest User, I want to be able to quickly identify deals, clearance items and special offers in order to take advantage of special savings on products I'd like to purchase.

a) This can be accessed from any page that the user is currently on by clicking on 'Deals' displayed at the top of the page and then select any of the links i.e reductions, clearance or deals based on what she wants. See screenshot below:

![Identify reductions, Clearance & Deals](documentation/user_stories_testing/reductions_clearance_deals.png)

iii) As a First Time, Registered or Guest User, I want to be able to easily view the total price of my purchase at any time so that I can avoid spending too much.

a) This can be easily seen from any page that the user is within the site. It's displayed underneath the shopping cart icon at the top right corner of the page. See screenshot below:

![View Total Price of Products Purchased](documentation/user_stories_testing/view_total_price_of_products_in_cart.png)

iv) As a Registered, First time or Guest User, I want to be able to view all available products in order to select some for purchase.

a) This can be accessed from any page that the user is within the site. In the navigation area at the top of the page, click on 'All Products' and then on 'All Products' again and it will display all the products available in the store as seen in the screenshots below:

![View all Products](documentation/user_stories_testing/products_page1.png)

![View all Products](documentation/user_stories_testing/products_page2.png)

![View Products](documentation/user_stories_testing/products_page3.png)

![View Products](documentation/user_stories_testing/products_page4.png)

![View Products](documentation/user_stories_testing/products_page5.png)

v) As a First time, Registered or Guest User, I want to be able to easily check out anonymously in order to purchase products without logging in or setting up an account.

a) From the home page, the user can select products, put in her cart, checkout, make payment and receive confirmation of successful checkout as an anonymous user i.e without logging in. One of the screenshots show that under the 'My Account' navigation header, the 'Register' and 'Login' links are displayed while the 'Logout' link is not in view which means that the user is not logged in as seen in the screenshots below: 

![Anonymous/Guest Checkout](documentation/user_stories_testing/anonymous_checkout_shopping1.png)

![Anonymous/Guest Checkout](documentation/user_stories_testing/anonymous_checkout_shopping2.png)

vi) As a First time, Registered or Guest User, I want to be able to easily delete product(s) in the cart in order to have the choice to remove it if not needed anymore.

a) When a user adds products into the shopping cart and navigates to the cart by clicking on the 'Continue to Secure Checkout' button, she can remove any one using the remove link provided underneath the 'Qty' button and that product will be removed from the cart. See screenshots below:

![Before Delete Product(s) in Cart](documentation/user_stories_testing/before_delete_product_in_cart.png)

![After Delete Product(s) in Cart](documentation/user_stories_testing/after_delete_product_in_cart.png)

vii) As a First time, Registered or Guest User, I want to be able to update products in the cart in order to adjust it any time if I change my mind.

a) When a user adds products into the shopping cart and navigates to the cart to view it by clicking on the 'Continue to Secure Checkout' button, she can update the contents of the shopping cart in many ways e.g clicking on the 'Continue Shopping' button to add more products into the cart, clicking on the '+' or '-' quantity button first before clicking on the 'Update' link under it to increase or decrease the quantity of products already in the cart. See screenshots below:

![Before Update Product(s) in Cart](documentation/user_stories_testing/before_update_product_in_cart.png)

![After Update Product(s) in Cart](documentation/user_stories_testing/after_update_product_in_cart.png)

![Update Product Message](documentation/user_stories_testing/update_product_message_in_cart.png)

viii) As a First time, Registered or Guest User, I want to be able to view products in the cart in order to know what I'm purchasing.

a) When a user adds products into the shopping cart either from 'products' or 'product-detail' page and clicks on the 'Continue to Secure Checkout' button, it takes her to the shopping cart where she can view the products (i.e contents) in her shopping cart as seen in the screenshots below:

![View Product(s) in Cart](documentation/user_stories_testing/shopping_cart_content1.png)

![View Product(s) in Cart](documentation/user_stories_testing/shopping_cart_content2.png)

![View Product(s) in Cart](documentation/user_stories_testing/shopping_cart_content3.png)

ix) As a First time, Registered or Guest User, I want to be able to add product/products to the cart in order to purchase a single one or check out multiple items in one click.

a) From either the 'products' or 'product-detail' page, a user can add product(s) into the shopping cart as seen in the screenshots below:

![Add Product(s) to Cart from Product Detail Page](documentation/user_stories_testing/add_product_to_cart1.png)

![Add Product(s) to Cart from Product Detail Page](documentation/user_stories_testing/add_product_to_cart2.png)

![Add Product(s) to Cart from Products Page](documentation/user_stories_testing/add_product_to_cart_from_products_page.png)

x) As a First time, Registered or Guest User, I want to be able to access information through their social media links to see their followings on social media to determine how trusted and known the app is. 

a)  On most websites, the footer houses the social media icons and links and ours is not an exception so from any page that the user is, scroll down to the bottom of the page and the link to the facebook page is there for the user to use. See screenshot below:

![Social media link on Footer](documentation/user_stories_testing/social_media_link.png)

xi) As a First time, Registered or Guest User, I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records.

a) When a user checks out successfully after purchase, a confirmation email is sent to her as a proof of order. See screenshot below:

![Email Confirmation after Successful Checkout](documentation/user_stories_testing/email_confirm_after_checkout_success.png)

xii. As a First time, Registered or Guest User, I want to be able to view my order confirmation after checkout so that I can verify that I haven't made any mistakes while placing the order.

a) After a successful checkout, a user receives an order confirmation showing the order number and details of her order. See screenshots below:

![Order Confirmation after Successful Checkout](documentation/user_stories_testing/order_confirmation1.png)

![Order Confirmation after Successful Checkout](documentation/user_stories_testing/order_confirmation2.png)

xiv. As a First time, Registered or Guest User, I want to be able to easily enter my payment information so that I can check out quickly with no hassles.

a) The user can pay for her products quickly on the checkout page where a form is displayed for the user to fill both her credit card and personal details. The payment is collected using Stripe in a safe and secure manner with all the security checks in place. See screenshots below:

![Payment Information at Checkout](documentation/user_stories_testing/payment_details1.png)

![Payment Information at Checkout](documentation/user_stories_testing/payment_details2.png)

![Payment Information at Checkout](documentation/user_stories_testing/payment_details3.png)

xv. As a First time, Registered or Guest User, I want to be able to update the quantity of individual item in my cart so that I can easily make changes to my purchase before checkout.

a) A user can update the quantity of products already selected in her shopping bag before checking out by selecting the right quantity using quantity selector box and click on the update link provided underneath. See screenshots below:

![Before Update Product(s) in Cart](documentation/user_stories_testing/before_update_product_in_cart.png)

![After Update Product(s) in Cart](documentation/user_stories_testing/after_update_product_in_cart.png)

![Update Product Message](documentation/user_stories_testing/update_product_message_in_cart.png)

xvi. As a First time, Registered or Guest User, I want to be able to easily select a product's quantity during purchase so that I can guard against accidentally selecting the wrong quantity.

a) Each product detail page has its own quantity selector box to avoid selecting the wrong quantity as seen in the screenshot below:

![Select Product Quantity](documentation/user_stories_testing/select_product_quantity.png)

xvii. As a First time, Registered or Guest User, I want to be able to view a specific category of products so that I can quickly find products I'm interested in without having to search through all products.

a) A user can use the search input box provided at the main nav section of the page to display the products with the category she's interested in and filter out other categories.
See screenshot below:

![Search Input Box](documentation/user_stories_testing/search_box.png)

xviii. As a First time, Registered or Guest User, I want to be able to view individual product detail so that I can see detailed information about its description, like, review or leave a comment.

a) The user can access all these features by navigating to the 'product_detail' page. From the navigation bar, click on 'All Products' and then 'All Products' again. This will take you to the page that displays all the products in the store. Click on a product's image to take you to the product-detail page and you will find all the information needed as seen in the screenshot below:

![Product Detail Page](documentation/user_stories_testing/product_detail_page1.png)

![Product Detail Page](documentation/user_stories_testing/product_detail_page2.png)

![Product Detail Page](documentation/user_stories_testing/product_detail_page3.png)

![Product Detail Page](documentation/user_stories_testing/product_detail_page4.png)

---

Admin User Goals

i. As an Admin User, I want to be able to log into my account in order to have the authorised access to manage products in the database.

a) From the home page, navigate to 'My Account' and under it, click on 'Login' and the Sign in page will be displayed. Enter your super user details and if it matches what's on record, it will log you in successfully as seen in the screenshots below:

![Admin User Login](documentation/user_stories_testing/admin_login1.png)

![Admin User Login Page](documentation/user_stories_testing/admin_login2.png)

![Admin User Login Page](documentation/user_stories_testing/admin_login3.png)

ii. As an Admin User, I want to be able to log out of my account in order to protect it from unauthorised access.

a) From any page within the site, navigate to My Account and under it, click on Logout and the pop up message will be displayed to confirm if you want to sign out and if the sign out button is clicked, the user is successfully logged out with a message displayed to reflect this as seen in the screenshots below:

![Admin User Logout Page](documentation/user_stories_testing/admin_logout1.png)

![Admin User Logout Page](documentation/user_stories_testing/admin_logout2.png)

![Admin User Logout Page](documentation/user_stories_testing/admin_logout3.png)

iii. As an Admin User, I want to be able to manage products within the store i.e add, view, edit & delete products into or from the database so that users of the website can enjoy a good user experience when interacting with the site.

a) An admin user can add products into the database. After logging in, navigate to My Accounts in the nav bar area and then select Store Management, this will take you to the add products page where new products can be added to the database at the back end as seen in the screenshot below: 

![Admin User Add Product Page](documentation/user_stories_testing/admin_user_product_add1.png)

![Admin User Add Product Page](documentation/user_stories_testing/admin_user_product_add2.png)

![Admin User Add Product Page](documentation/user_stories_testing/admin_user_product_add3.png)

b) An admin user can view products in the database in 2 ways i.e either through the front-end with the products page or back end using the django admin. For the front-end access, navigate to All Products header in the nav bar area after logging in and then select All Products link and the products page will be displayed where you can view all products in the database. For the back-end view, on the home page, append forward slash admin to the URL and navigate to Django admin login page. Provide your login details as seen in the screenshot below:

* Front end Products view:

![View all Products](documentation/user_stories_testing/products_page1.png)

![View all Products](documentation/user_stories_testing/products_page2.png)

![View Products](documentation/user_stories_testing/products_page4.png)

![View Products](documentation/user_stories_testing/products_page5.png)

* Back end Products view:

![View Products Backend](documentation/user_stories_testing/django_admin_login.png)

![View Products Backend](documentation/user_stories_testing/django_admin_products_view1.png)

![View Products Backend](documentation/user_stories_testing/django_admin_products_view2.png)

c) An admin user can edit products in the database in 2 ways i.e either through the products or product detail page. From the home page or any other page, navigate to All Products in the nav bar area and click on All Products link again. It will display the products page, click on the edit button displayed beside the product you want to edit and it will display the edit page for you to make the ammendment and save it back into the database. The 2nd way to edit is that while on the products page, click on the image of the product you want to edit and it will open in new tab, click on the edit button displayed beside the product and it will display the edit page for you to make the ammendment after which you can save it back to the database. See screenshots below:

![Admin-User Edit Products Page](documentation/user_stories_testing/admin_user_edit_page1.png)

![Admin-User Edit Products Page](documentation/user_stories_testing/admin_user_edit_page2.png)

![Admin-User Edit Products Page](documentation/user_stories_testing/admin_user_edit_page3.png)

![Admin-User Edit Products Page](documentation/user_stories_testing/admin_user_products_page_edit.png)

![Admin-User Edit Products Page](documentation/user_stories_testing/admin_user_product_detail_page_edit.png)

d) An admin user can delete products in the database in 2 ways i.e either through the products or product detail page. From the home page or any other page, navigate to 'All Products in the nav bar area and click on All Products link again. It will display the all products page, click on the delete button displayed beside the product you want to remove and it will be deleted immediately and a pop up message displayed to confirm that the product has been deleted from the database.
The 2nd way to delete a product is this: while on the products page, click on the image of the product you want to delete and it will open in new tab, click on the delete button displayed beside the product and it will be removed immediately from the database. See screenshot below:

![Admin-User Delete Products Page](documentation/user_stories_testing/admin_user_delete_page1.png)

![Admin-User Delete Product-Detail Page](documentation/user_stories_testing/admin_user_delete_page2.png)

![Admin-User Delete Products Page](documentation/user_stories_testing/admin_user_delete_prod_confirm.png)

![Admin-User Delete Products Page](documentation/user_stories_testing/admin_user_delete_success.png)

---

# Browser Compatibility Testing

* I carried out compatibility test across three different browsers below and the site rendered correctly and were responsive across these browsers. See screenshots below:

i. Google Chrome

![Google Chrome](documentation/browser_compatibility_test/chrome_all_products.png)

![Google Chrome](documentation/browser_compatibility_test/chrome_home_page.png)

![Google Chrome](documentation/browser_compatibility_test/chrome_prod_detail.png)

![Google Chrome](documentation/browser_compatibility_test/chrome_shopping_cart.png)

ii. Microsoft Edge

![Microsoft Edge](documentation/browser_compatibility_test/ms_edge_all_products.png)

![Microsoft Edge](documentation/browser_compatibility_test/ms_edge_home_page.png)

![Microsoft Edge](documentation/browser_compatibility_test/ms_edge_prod_detail.png)

![Microsoft Edge](documentation/browser_compatibility_test/ms_edge_shopping_cart.png)

iii. Opera

![Opera](documentation/browser_compatibility_test/opera_all_products.png)

![Opera](documentation/browser_compatibility_test/opera_home_page.png)

![Opera](documentation/browser_compatibility_test/opera_prod_detail.png)

![Opera](documentation/browser_compatibility_test/opera_shopping_cart.png)

