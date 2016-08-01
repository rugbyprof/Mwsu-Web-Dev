## Credit Card Processing

We will be using https://stripe.com/ to process credit cards. They are extremely popular and offer many plug-ins for many platforms. What is really nice though is they offer a "sandbox" which will allow us to set up a "fake" account to process fake payments. In order to set up stripe in your website, you will need to lay the ground work. Below is a set of steps to get all that going. 

See you Tuesday.

### Install Composer
- This is to help install the php stripe library.
- https://getcomposer.org/download/
- After you install, then run `mv composer.phar /usr/local/bin/composer`. This will move `composer.phar` to the `\usr\local\bin` directory and let you run composer like this: `composer require stripe/stripe-php` instead of `php composer.phar require stripe/stripe-php`

### Domain Name
- To run credit cards you need SSL. To setup SSL you need a domain name! So, let's get a domain name.
- A good place is here: https://www.namecheap.com. They have domains for $0.88. 
- Or here: https://godaddy.com. They have domains for $0.99.

### SSL
- The following tutorial is the most pain free way to install an SSL certificate on your server. 
- You need to have your own domain name already.
- https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-14-04

### Create a Stripe Account
- Create your test stripe account at https://stripe.com
- Create a fake business name to go along with your account. 
- Also make sure you generate your api keys: https://dashboard.stripe.com/account/apikeys
- These are needed in the first tutorial.
- Also when testing, use fake card numbers from here: https://stripe.com/docs/testing

### Stripe Tutorial
- Now that you have a domain name and an SSL certificate, you can start the stripe tutorial.
- I found the tutorial here: https://stripe.com/docs/examples, so if you want you can look at other tutorials as well. 
- A php tutorial for stripe: https://github.com/stripe/wilde-things

### Bootstrap Stripe Form
- This is simply a bootstrap form that is built with using stripe in mind. You won't need this until tomorrow. 
- https://github.com/myg0v/Simple-Bootstrap-Stripe-Payment-Form

