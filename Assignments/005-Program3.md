## Assignment 5 - Adding an Api
#### Due July 18<sup>th</sup> by class time.

### Assignment Overview

- Create a products table in your database
- Populate the products table with the data from [here](https://raw.githubusercontent.com/rugbyprof/Mwsu-Web-Dev/master/products_big.json)
- Clone an API from github from [here](https://github.com/mevdschee/php-crud-api)
- Use curl to "test" your api.

### General Requirements
- Create a folder called `Program_3` in your `/var/www/html` directory.
- All files for this assignment will be placed in this folder. 

## Create Table 

- Create a file called `products-table.sql` and place the `sql` command from below inside this file.

```sql
CREATE TABLE IF NOT EXISTS `products` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `category` varchar(64) NOT NULL,
  `desc` mediumtext NOT NULL,
  `price` double(10,2) NOT NULL,
  `img` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6886 ;
```

- Now use the sql command to create your products table within your `web-dev` database.
- We will place all of these items in files, so that if your database crashes or something goes wrong, you can rebuild it.

## Load Table

- Write a php script called `load_products.php` and place it in your project folder.
- Copy the `products_big.json` into the same folder.
- For help, here is a skeleton:

```php
// Include dbconnection string
include('dbconnect.php');

// file_get_contents - reads a file
// json_decode - decodes json obviously, but the "true" turns the json into an associative array.
$json_array = json_decode(file_get_contents('products_big.json'),true);

// These two commands would dump the json array for viewing in a clear manner.
// Only needed for debugging
//echo "<pre>";
//print_r($json_array);

//For each entry in the json_array ... do something with it.
foreach($json_array as $entry){

	// Remember to use  str_replace to replace '160' with a '~'
	// Remember to use substring to turn price into a float.
	// Create sql insert statement
	// Insert each into database here
}
```

- After you are successful, create a file called `products.sql` and put in your project folder.
- From phpmyadmin, "export" your products table and place the sql commands in this file. This will allow us to rebuild in case of catastrophe.

## Api Overview

![](http://f.cl.ly/items/1Z0l3P0a0L3a3v3h3T3C/api.png)

[API](https://en.wikipedia.org/wiki/Application_programming_interface) stands for: Application Programmer Interface, and can let the developer seperate the data layer from the interface (amongst other things). The biggest benefit for us is that we can get away from embedding our php code with our html. This is not the only way to solve our crazy code issue, but using an API to grab data from our backend server will help us "clean" up our code. It will also let us implement an architectural pattern known as [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (Model View Controller). We won't adhere to MVC in the strictest sense, but the use of an API will help us seperate our "Views" (what the user sees) from our "Models" (the database connection layer).

So the first thing we should do is "install" an api on our server. In our case, we can simply use a nice API that I found on github.


### Getting an Api

- Go to https://github.com/mevdschee/php-crud-api and clone this repository on your server.
- Place it in `/var/www/html/` (NOT your Program_2 folder!)
- Rename the folder to `api` so that we can reach it from `http://your.ip.address/api/api.php`
- At the bottom of the file named `api.php` there is a code block that looks similar to the snippet below, except all lines are commented out. Uncomment the top group so we can connect this api to our mysql database:

```
$api = new PHP_CRUD_API(array(
	'dbengine'=>'MySQL',
	'hostname'=>'localhost',
  'username'=>'web-dev',
  'password'=>'mwsumustangsmwsu',
  'database'=>'web-dev',
	'charset'=>'utf8'
));
$api->executeCommand();

//For Microsoft SQL Server 2012 use:

// $api = new PHP_CRUD_API(array(
// 	'dbengine'=>'SQLServer',
// 	'hostname'=>'(local)',
// 	'username'=>'',
// 	'password'=>'',
// 	'database'=>'xxx',
// 	'charset'=>'UTF-8'
// ));
// $api->executeCommand();

//For PostgreSQL 9 use:

// $api = new PHP_CRUD_API(array(
// 	'dbengine'=>'PostgreSQL',
// 	'hostname'=>'localhost',
// 	'username'=>'xxx',
// 	'password'=>'xxx',
// 	'database'=>'xxx',
// 	'charset'=>'UTF8'
// ));
// $api->executeCommand();

//For SQLite 3 use:

// $api = new PHP_CRUD_API(array(
// 	'dbengine'=>'SQLite',
// 	'database'=>'data/blog.db',
// ));
// $api->executeCommand();
```

### Example Usage

#### GET
```
curl -X "GET" http://mwsu-webdev.xyz/api/api.php/users
```


#### POST
```
curl -H "Content-Type: application/json" -X "POST" http://mwsu-webdev.xyz/api/api.php/users -d '{"fname":"susan","lname":"sarandon","display_name":"none","email":"susan@radical.com","password":"a;lsdjf;alsdjf;alsdfja;sdjfasdjfasldkjf"}'
```

#### PUT
```
curl -H "Content-Type: application/json" -X "PUT" http://mwsu-webdev.xyz/api/api.php/users/1 -d '{"fname":"susan"}'
```

#### DELET
```
curl -X "DELETE" http://mwsu-webdev.xyz/api/api.php/users/2
```

## Curl Assignment:

- Using the documentation from [here](https://github.com/mevdschee/php-crud-api) complete the following requests using curl commands.
- Place your answers in a file called `curl_answers.txt` in your project folder.
- When you see "existing value" choose a value that you know exists in your data base.
- The documentation has you use the `filter[]=...` to specify multiple filters. When you want to run a curl command with square brackets in the url, put `--globoff` in your command like so: `curl --globoff -X "GET" .....`. If you have some doubts, you can run your command from a browser address bar to check as well.

1. Find user with email matching "existing value" 
2. Add a new user with the following information:
    - fname: Salman
    - lname: Kahn
    - email: salman.kahn@indianactors.org
    - display_name: coolasiwannabe
    - password: 123456789
3. Find all products with a price equal to 99.99
4. Find all products that have the word "tablet" AND the word "acer" in the description.
5. Find all "Acer" tablets that are less than 100 dollars.
6. Find all the images for laptops that have `intel i7` processors and `ssd` drives.
7. Find all cellphones that are NOT apple products.
8. Update all products that have a price of `0.00` to have a price of `0.13` cents.
8. Make sure you can delete from a table using curl.
