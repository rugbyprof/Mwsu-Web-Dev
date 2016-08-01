## Credit Card Processing

We will be using https://stripe.com/ to process credit cards. They are extremely popular and offer many plug-ins for many platforms. What is really nice though is they offer a "sandbox" which will allow us to set up a "fake" account to process fake payments. In order to set up stripe in your website, you will need to lay the ground work. Below is a set of steps to get all that going. 

See you Tuesday.

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

### Install Composer
- This is to help install the php stripe library.
- https://getcomposer.org/download/
- After you install, then run `mv composer.phar /usr/local/bin/composer`. This will move `composer.phar` to the `\usr\local\bin` directory and let you run composer like this: `composer require stripe/stripe-php` instead of `php composer.phar require stripe/stripe-php`

### Setup Stripe
- Login to your server and go to `/var/www/html`
- Clone https://github.com/stripe/stripe-php.git into your html folder.
- Do the following to make the stripe library available:
    - cd stripe-php
    - composer install
- Now your ready to start with the tutorial

### Stripe Tutorial
- Now that you have a domain name and an SSL certificate, you can start the stripe tutorial.
- I found the tutorial here: https://stripe.com/docs/examples, so if you want you can look at other tutorials as well. 
- A php tutorial for stripe: https://github.com/stripe/wilde-things
- Clone https://github.com/stripe/wilde-things.git into your `/var/www/html` directory.
- To get started, cd into the `Step1` folder.
- If you do a directory listing you will see:

```
-rw-r--r-- 1 root root 2.3K Aug  1 15:14 index.php
-rw-r--r-- 1 root root 1.5K Aug  1 15:14 README.md
```

- Now run `composer require stripe/stripe-php`. 
- You should now see:

```
-rw-r--r-- 1 root root   64 Aug  1 15:24 composer.json
-rw-r--r-- 1 root root 2.4K Aug  1 15:25 composer.lock
-rw-r--r-- 1 root root 1.9K Aug  1 15:29 index.php
-rw-r--r-- 1 root root  963 Aug  1 15:14 README.md
drwxr-xr-x 4 root root 4.0K Aug  1 15:25 vendor
```

- Now edit `index.php` and add your api keys.

```php
$stripe = array(
  'secret_key'      => '<YOUR SECRET STRIPE API KEY>',
  'publishable_key' => '<YOUR PUBLISHABLE STRIPE API KEY>'
  );
```

- Now your first example should work. Make a charge using the face credit card info, and check your dashboard. 
- Continue in this manner for the rest of the Steps.

### Bootstrap Stripe Form
- This is simply a bootstrap form that is built with using stripe in mind. You won't need this until tomorrow. 
- https://github.com/myg0v/Simple-Bootstrap-Stripe-Payment-Form

