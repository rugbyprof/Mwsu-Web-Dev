## Assignment 8 - Shopping Cart

#### Due Aug 1<sup>st</sup> by class time.

## General Requirements
- Copy `program_7` to `program_8`.
- Download the following bootstrap templates:
    - Single Product View:
        - http://startbootstrap.com/template-overviews/shop-item/
    - Multiple Products View:
        - http://startbootstrap.com/template-overviews/shop-homepage/


## Requirements
- Products
    - Using the multiple product view template, add the proper logic to make products show up in each of the "custom content" boxes with pagination below the products. 
    - Set the number of products to be viewed to 12.
- Sidebar Menu
    - Populate the sidebar menu with each category from the `categories` table in our database. 
    - When a category is clicked, filter the products in the main view to show only those products.
    - Set the class to "active" for that particular button, and remove active from any remaining buttons.

## Category Table

```sql
CREATE TABLE IF NOT EXISTS `categories` (
  `id` int(4) NOT NULL,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(0, 'tablet'),
(1, 'smartphone'),
(2, 'laptop'),
(3, 'ipad'),
(4, 'game console'),
(5, 'desktop computer'),
(6, 'camera');
```

### Some Links 
(not necessarily needed for assignment)

Login and Registration 
https://github.com/fethica/PHP-Login

Password Strength:
https://github.com/ablanco/jquery.pwstrength.bootstrap

Single Product View:
http://startbootstrap.com/template-overviews/shop-item/

Multiple Products View:
http://startbootstrap.com/template-overviews/shop-homepage/

Contact Form from Bootsnipp
http://bootsnipp.com/search?q=contact


