## Assignment 5 - Adding an Api
#### Due July 18<sup>th</sup> by class time.

## Api Overview

![](http://f.cl.ly/items/1Z0l3P0a0L3a3v3h3T3C/api.png)

[API](https://en.wikipedia.org/wiki/Application_programming_interface) stands for: Application Programmer Interface, and can let the developer seperate the data layer from the interface (amongst other things). The biggest benefit for us is that we can get away from embedding our php code with our html. This is not the only way to solve our crazy code issue, but using an API to grab data from our backend server will help us "clean" up our code. It will also let us implement an architectural pattern known as [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (Model View Controller). We won't adhere to MVC in the strictest sense, but the use of an API will help us seperate our "Views" (what the user sees) from our "Models" (the database connection layer).

So the first thing we should do is "install" an api on our server. In our case, we can simply use a nice API that I found on github.

### Products Structure

```sql
CREATE TABLE IF NOT EXISTS `products` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `category` varchar(64) NOT NULL,
  `desc` mediumtext NOT NULL,
  `price` double(8,3) NOT NULL,
  `img` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6886 ;
```


### Getting an Api

- Go to https://github.com/mevdschee/php-crud-api and clone this repository on your server.
- Place it in `/var/www/html/`
- Rename the folder to `api`
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

### Using the Api

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
