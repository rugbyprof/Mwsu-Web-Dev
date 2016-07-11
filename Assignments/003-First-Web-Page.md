## Assignment 3 - First Web Page

#### Due July 13<sup>th</sup> by class time.
- Go to `/var/www/html` on your server and run the following commands:

```bash
$ wget https://github.com/rugbyprof/Mwsu-Web-Dev/blob/master/just_one_page.zip?raw=true
$ unzip just_one_page.zip
$ rm just_one_page.zip
```

- Once you've unzipped `just_one_page.zip`, if you have a `just_one_page` folder, move the contents of `just_one_page` back one directory:

```
$ cd just_one_page
$ mv * ..
$ rm -rf just_one_page
```

The commands above do the following:

1. change into the `just_one_page` directory
2. move all the files and folders back into the portal folder (or up one directory)
3. delete the NOW empty folder: `just_one_page`


### Make the following changes:
- TBD


[1]: https://cdn1.iconfinder.com/data/icons/stilllife/24x24/filesystems/gnome-fs-directory.png
[2]: http://png-2.findicons.com/files/icons/2360/spirit20/20/file_php.png
[3]: http://www.lecollagiste.com/collanews/themes/lilina/web/media/folder.gif
[4]: http://rs.tudelft.nl/~rlindenbergh/publications/html.gif
[5]: https://cdn4.iconfinder.com/data/icons/spirit20/file-css.png
[6]: https://cdn4.iconfinder.com/data/icons/spirit20/file-js.png
