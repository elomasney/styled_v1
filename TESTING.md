## **Testing**

### **Tests Carried Out**

### **Validation**
**HTML**
- I used the [W3C Markup Validator](https://validator.w3.org/)
- I tested all HTML pages by either url link or the 'view source code' link on Google DevTools
- When I first ran my code through the HTML validator, there were a few minor errors
- I resolved these minor issues and ran all page through the validator again.
- All HTML pages passed the validation

**CSS**
- I used the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- All CSS code passed the validation process with no errors

**Javascript**
- I used [JSHint](https://jshint.com/)
- When I ran the Javascript code through the validator all code passed with no errors

**Python**
- I used [pep8online](http://pep8online.com/) to validate my Python code
- All code passed and meets the PEP8 standards.

### **General**
**_Check alt text appears for all images_**

- Hover over images to see if there is clear alt text visible.
All images were tested and alt text appears on images.

**_Conducted spell check on README file and text used in both HTML files._**

- All spelling errors were corrected.

**_Autoprefixer CSS_**

- Ran code through Autoprefixer and copied code back into css file.

**_Mobile Friendly Test_**

- Ran code on [Mobile Friendly Test](https://search.google.com/test/mobile-friendly) page and passed all tests. The site is mobile friendly.

**_Testing on physical devices_**

- I also asked friends and family members to test the website on many different devices including large screen laptops,
iPhone, android, android table and iPad and across a variety of browsers Internet Explorer, Google Chrome, and Firefox

### **User Story Tests**
**_As a user I would like to understand the purpose of the website._**
- The homepage carousel jumbotron states the purpose of the site clearly for all visitors.

**_As a user I want to be able to create my own profile that holds all my content._**
- Once a user registers for an account and verifies their email address they can access their own profile page. 
- This profile page contains the user's default delivery address which can be updated and their order history.

**_As a user, I want to be able to navigate the website with ease._**
- The navigation bar is in a fixed position and always on display
- The navigation links are clearly defined and change depending on user status.
- Call to action buttons are defined and easy to identify
- Redirects and buttons are provided to take the user to the targeted area.

**_As a user I expect to be able to quickly find products and services I am looking for._**
- The navigation bar provides links to all the products available on the website as well as a link for each service availble which will direct the user to that specific service information page.
- There is a search bar located on the navigation bar that is always accessible to all users. Users can quickly search for the product they are looking for using this functionality.

**_As I user I want to know the price of the products._**
- The all products page provides the price information for each service which is clearly defined and visible to the user immediately.
- The product price information is also clearly visible to the user on the product detail page below the product description.

**_As a user, I would like information about what is included in the service I am purchasing._**
- All services available on the site have a list of product features displayed at the bottom of the product detail page.
- These features outline the details of what will be included as part of each service and give further guidance and a better understanding of what is included as part of these services.

**_As I user I want to easily see the total price of my current shopping bag._**
- The total of the user's shopping bag is clearly displayed for the user below the shopping bag icon at all times.
- If the user adds an item to their shopping bag, this price is updated immediately to reflect this change and a success toast indicates to the user which items have been added and the associated costs.
- The shopping bag total is also visible from the shopping bag page which can be accessed by clicking the shopping bag icon on the navigation bar.

**_As a user I want the ability to update and delete items in my shopping bag._**
- The shopping bag page includes a quantity update functionality, where users can increase and decrease the quantity of each item.
- The update and delete links to handle this functionality are located directly below the quantity selector input.
- The user can use the update link to update the quantity of the items.
- The user can use the delete link to remove items from their shopping bag.

**_As a user I would like a profile that holds all the information on my previous orders._**
- There is a section of the profile page that contains the user's previous orders in their order history.
- This displayed in a column to the right on larger screens and at the top on mobile devices.
- It contains information such as order number, order date, order items and subtotal.
- The order number acts as a link for the user, and when clicked, will direct the user to the order confirmation page for that specific order.

**_As a user I would like to login and logout easily._**
- The login and logout links are available at all times on the navigation bar.
- The user can locate these links by navigating to the 'My Account' dropdown menu on the navbar and selecting the 'Login' or 'Logout' links.

**_As a user I would like receive email confirmation of any purchases made._**
- This is achieved through the use of Gmail. 
- Once an order is placed and the user has made payment successfully, a Bootstrap toast will alert the user that an email confirmation of their order has been sent to their email address.

**_As a user I would like to have all the order details specified in my email order confirmation._**
- The order confirmation email sent to the user contains all the order information including order number, order date, order items, delivery address, billing address and order total.

**_As a user, I would like to receive alerts/messages when I submit, enquire or make a purchase that inform me it was successful._**
- This is achieved through the implementation of Bootstrap toasts. I have set up toasts for warnings, errors, information and success messages.
- These are triggered when a user action is completed.
- A success message will be displayed to the user at top right hand corner of the screen when, a purchase has been made, the user has logged in, the user has logged out, added an item to their bag, updated an item in their bag or deleted an item from their bag.
- In the contact form page, once the contact form has been sent successfully, the user will be directed to the thank you page where the user is informed that their email has been sent successfullly.

**_As a user, I would like to have access to a fast secure payment system when purchasing items._**
- This is achieved through the use of Stripe as a fast, reliable and secure payment system for users.

**_As a new user, I would like the ability to register for a user account_**
- New users can easily register for an account on the website.
- There is a 'Register' link provided in the 'My Account' dropdown menu on the navigation bar.
- The user is directed to the register page where they will be asked to complete the registration form by providing a username, email and password.
- The user will then be sent an email to verify their email.
- Once the email has been verified, the user can then log into their account using the 'Login' link provided in the navigation bar.

**_As a user, I would like the ability to recover my password._**
- On the 'Login' page a 'Forgot Password' link is provided at the end of the login form.
- This link is highlighted in orange.
- A user can click this link and will be directed to the reset password page.
- Here a user will be asked to enter their email address and a reset password link will be sent to the email address provided.
- User can then navigate to their emails, click on the link provided and will be directed to the set password page.
- From here they have the ability to set a new password and login with the new password they just created.

**_As a user I would like the ability to be able to communicate with the company via email from the site._**
- This website provides a 'Contact Us' page which can be accessed directly from the navigation bar that is always visible to the user.
- This link directs the user to the contact page form which includes fields for the user's email, a subject and their message.
- All fields are required and will result in an error if not filled in correctly.
- Once validated, the user can click the 'Send' button to submit the message.
- This email is then sent directly to the company email address via Gmail.
- The user is then directed to the thank you page which will inform them that the message was sent successfully and someone will respond as soon as possible.

**_As the owner and user, I want to encourages users to make purchases and earn an income._**
- This website is an e-commerce website that allows users to purchase the products and services available.
- Stripe is used to allow for fast, reliable and secure payment transactions on the site.

**_As the owner and user, I want to be able to add, update or delete products on the website._**
- Admin users have extra functionality throughout the website.
- Under the 'My Account' dropdown menu in the navigation bar, an admin user an admin user can select 
    - Product Managment (allows an admin user to add a product to the database)
- Admin users also have the ability to edit and delete products.
- These update and delete links are provided in both the product detail page page directly below the product image.
- The delete functionality also has an added security measure using a Sweet Alert popup confirmation that will prompt the user to check if they are sure they wish to delete the product.
- The user then has a choice to confirm or cancel the delete action. This is to ensure that no items are deleted accidentally from the database.

**_As the owner and user, I want the ability to create, update and delete product features._**
- Admin users have extra functionality throughout the website.
- Under the 'My Account' dropdown menu in the navigation bar, an admin user can select
    - Product Feature Management(allows an admin user to add a product feature to the database)
- Admin users also have the ability to edit and delete product features.
- These update and delete links are provided in both the product detail page directly below the product image.
- The delete functionality also has an added security measure using a Sweet Alert popup confirmation that will prompt the user to check if they are sure they wish to delete the product feature.
- The user then has a choice to confirm or cancel the delete action. This is to ensure that no items are deleted accidentally from the database.

**_As the owner and user, I want the ability to create, update and delete gallery images._**
- Admin users have extra functionality throughout the website.
- Under the 'My Account' dropdown menu in the navigation bar, an admin user can select
    - Look Book Management(allows an admin user to add an image to the database)
- Admin users also have the ability to edit and delete images.
- These update and delete links are provided in both the Look Book gallery page directly below the image.
- The delete functionality also has an added security measure using a Sweet Alert popup confirmation that will prompt the user to check if they are sure they wish to delete the image.
- The user then has a choice to confirm or cancel the delete action. This is to ensure that no items are deleted accidentally from the database.

**_As the owner and user, I want other users to be able to contact me if they have any questions or complaints or general feedback._**
- Users can contact the company owners through the contact form provided on the contact page.
- This form is set up to send the email form directly to the site owner's Gmail account.
- The email will include the user's email so that the site owner can respond directly to the user.

**_As the owner and user, I want provide users with incentive to sign up._**
- Registered users have added benefits when they sign up for a user account on the website.
- Registered users have access to a profile page of their own which contains their default delivery information and their order history.

**_As a guest user, I would like to be able to search for products and services._**
- A guest user can access all the products and services available on the website.
- They can access these through the navigation bar, via the services dropdown menu and gift voucher links provided. These are visible to users at all times.
- They can also access the products and services through the use of the search bar functionality on the navigation bar.

### **Site Functionality**
| Test  | Test Action  |  Expected Outcome |  Test Result |   |
|---|---|---|---|---|
|Navigation Links   |  Test that all navigation links take the user to the correct page | All navigation links should take the user to the correct targeted page  | Pass - The navigation links all work as intended and operate correctly. |   |
| Navigation links should change depending on user status  | Access the site as different user types and check navbar links are correct  |  The correct links are visible to Admin, Registered Users and Guest Users of the site | Pass - All intended links are showing up depending on user status  |  |
| Navigation bar responsiveness  | Check responsiveness of navigation bar using Chrome DevTools to check if it worked across all devices  | The navigation bar is fully responsive, showing links to the right hand side on larger screens and collapses into a hamburger menu on medium and smaller devices.  | Pass - Navbar is working as expected and is responsive |   |
| Test  | Test Action  |  Expected Outcome |  Test Result |   |
| Test  | Test Action  |  Expected Outcome |  Test Result |   |
| Test  | Test Action  |  Expected Outcome |  Test Result |   |
| Test  | Test Action  |  Expected Outcome |  Test Result |   |
| Test  | Test Action  |  Expected Outcome |  Test Result |   |