![Wig Image](media/wig_store_readme_logo.jpg)

# wiGalleria E-commerce Wig Store

wiGalleria is an e-commerce wig store app dedicated for the main purpose of purchasing wigs of different colours, shapes and textures as well as hair care products that helps wigs last longer.
This project was created using Python based Django framework. It is a fully featured app similar to real e-commerce apps out there that we use everyday with payment gateway that allows a user make payment but as this is a prototype, users are informed not to use their real debit/credit cards to purchase but can only use test debit/credit card provided by Stripe whose details will be given to anyone who wants to test this out once it's finished. A user will be able to perform full CRUD functionality i.e Create, Read, Update and Delete his data as well as making payment through the use of Stripe gateway API. The programming languages used for the development of this app are a combination of HTML, CSS (both bootstrap & custom) & JavaScript for the front-end and Python based Django framework for the back-end development. 

The purpose of this app is to allow a user purchase wigs and hair care products online in the comfort of their own homes without physically going to the store. Having an online wig store  eliminates the shortfall of store closing as it is on 24/7 except when store maintenance is taking place. The beauty and biggest advantage of building an ecommerce wig store is that it opens up a manually handled local business to a wider reach/audience worldwide so that it can be accessible for anyone to purchase wigs and hair care products from any location. 

The user interacts with the app through the GUI interface i.e front-end templates designed for each functionality such as add & edit products in the cart, view or delete products in the cart, view all products in the store & select the one(s) to purchase. There are role-based authentication system in place that ensures that different users can access different views i.e only registered/login/admin users can access certain views. An admin user will be the only one allowed to manage the store by interacting with the app through the front-end GUI interface & Django backend i.e perform CRUD functionality of Create, Read, Update & Delete products.  This store is protected with a very strong authentication system so that no unauthorised person will have access to its content. 

![wiGalleria app on Desktop, Laptop, Tablet & Smatphone]()

# Features

This E-commerce app named wiGalleria will allow the user register for an account, login, logout, checkout either as a registered user or guest user if they don't want to sign up for an account. It will also give them the ability to add product(s) to, edit or delete product(s) from and view products in the shopping cart.
When a user checks out, it will calculate and display the delivery cost as well as the total cost of products purchased before they make payment. It shows the user a summary of their order while on the checkout page and allows them to edit/update quantity of products they've selected earlier if they change their minds about buying them.
Overall, though the app is a prototype at the moment, yet it is a full fledge e-commerce app except that real purchase & payments cannot be made until some little adjustments are made and hopefully, this will be augmented in the near future to reflect this.

# Existing Features

The wiGalleria app will provide the following features to its users: 

* Create: A registered or guest user can add product(s) into the shopping cart 
* Read: A registered or guest user can view the items in their list
* Update: A registered or guest user can edit items in their list 
* Delete: A registered or guest user can either remove an item from their list or delete an entire list.
* Sign Up: A guest user can register if he doesn't have an account yet before he can access some features of the app
* Login: A user must be authenticated i.e logged in if he already has an account in 
order to be able to perform any action on his shoppinglist.
* Logout: A user can log out of his account to secure his shopping list
* Check out as a registered user if logged in
* Checkout as a guest user if not registered or logged in
* A user's delivery info can be saved in his profile for a faster checkout any time he visits the store again. 

---
