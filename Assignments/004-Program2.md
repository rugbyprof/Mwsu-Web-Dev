Grab this zip file: http://mwsu-webdev/program2.zip

1. Install phpmyadmin on your server
2. Create a user called `web-dev`
3. Create a database called `web-dev`
4. Create a table in web-dev called users:

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
