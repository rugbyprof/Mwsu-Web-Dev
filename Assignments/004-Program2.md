## Assignment 4 - Fix Registration& Login
#### Due July 14<sup>th</sup> by class time.

- Login to your server.
- Go to `/var/www/html`
- Create a folder called `program_2`
- Change into that folder.
- Run `wget http://mwsu-webdev/program2.zip`
- Unzip program2 (if it errors, install zip with `apt-get install zip`)

- Install phpmyadmin on your server
- Create a user called `web-dev`
- Create a database called `web-dev`
- Database user password = 'mwsumustangsmwsu'
- Create a table in web-dev called users:

```sql 
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(5) NOT NULL AUTO_INCREMENT,
  `fname` varchar(25) NOT NULL,
  `lname` varchar(25) NOT NULL,
  `display_name` varchar(32) NOT NULL,
  `email` varchar(35) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;
```

- Fix the error on registration page to NOT display when initially loaded.
- After a user is logged in, do NOT print the form, but provide a link (or button) to send the to the login page (login.php).
- Then implement a login script that will authenticate them, and send them to "home.php" otherwise print an error message telling them to retry.
- http://www.codingcage.com/2015/03/simple-login-and-signup-system-with-php.html

