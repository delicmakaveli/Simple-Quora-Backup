# Simple Quora Backup

**Web Scraper and Crawler used to backup Quora Bookmarks and Answers.**

**Note 1:** The scripts may not work due to changes on Quora's end in terms of HTML code.

**Note 2:** Quora forbids scraping and has made it very difficult by using lazy loading. These scripts get around it but 
they are still slow in comparison to some scrapers that just need to send a HTTP request and parse the response.

**Simple Quora Backup** is a project I made for personal use to backup my Bookmarks and Answers on Quora.
I made it in case I have to access the content but I don't have internet or if Quora, for whatever reason, disappears :).

The basic idea is to run the scripts, let them log in to Quora automatically, crawl through pages, scroll through content, 
scrape the content once it's loaded and save it as text in simple, minimalistic fashion.

## Contents:

* [Built With](https://github.com/delicmakaveli/Simple-Quora-Backup#built-with)
* [Prerequisites](https://github.com/delicmakaveli/Simple-Quora-Backup#prerequisites)
* [Getting Started](https://github.com/delicmakaveli/Simple-Quora-Backup#getting-started)
* [Deployment](https://github.com/delicmakaveli/Simple-Quora-Backup#deployment)
* [Author](https://github.com/delicmakaveli/Simple-Quora-Backup#author)
* [License](https://github.com/delicmakaveli/Simple-Quora-Backup#license)
* [Acknowledgements](https://github.com/delicmakaveli/Simple-Quora-Backup#acknowledgements)

## Built With

* [Python 3.5](https://www.python.org/doc/) - Program was written in this language only
* [Selenium](http://selenium-python.readthedocs.io/) - Used for automating clicking and scrolling to get around lazy loading
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#) - Used for Web Scraping 

## Prerequisites

What things you need to install and run the software:

* [Python 3.5+](https://www.python.org/doc/)
* [Selenium](http://selenium-python.readthedocs.io/)
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
* [textwrap](https://docs.python.org/3.5/library/textwrap.html#module-textwrap)

## Getting Started

This will get you a copy of the project up and running on your local machine for development and testing purposes.

Just [download](https://github.com/delicmakaveli/Simple-Quora-Backup/archive/master.zip) and extract the project master-folder.

Make sure you have everything from the Prerequisites above.

After that just run the scripts:

* for BOOKMARKS run [backup_bookmarks.py](https://github.com/delicmakaveli/Simple-Quora-Backup/blob/master/backup_bookmarks.py)
* for ANSWERS run [backup_answers.py](https://github.com/delicmakaveli/Simple-Quora-Backup/blob/master/backup_answers.py)

## Deployment

Although this was tested only on Windows and 64bit Linux(Ubuntu) it should run on all platforms that support Python and all the modules used.

## Author

* **Stefan Delic** - *Creation and Initial work* - [delicmakaveli](https://github.com/delicmakaveli)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/delicmakaveli/Simple-Quora-Backup/blob/master/LICENSE) file for details

## Acknowledgments

* Hats off to the good people who wrote the code for all the modules that made building stuff with Python easier and faster.
