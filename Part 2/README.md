# Part 2

## Part A
> Create a Python function that scrapes all links from the Intranet website, based on a file extension provided as input (e.g. .pdf). The function should ensure that only links within the intranet domain are collected, and not any other external links outside of intranet. Also, save the list of URLs in a text file (urls.txt). <br> You may use any python library you are comfortable with (like Scrapy, BeautifulSoup, etc.) for web scraping. <br> (Additional) Scraping by office types (like Academic, Admin, etc.) and saving them in different files.

The code for the script is in the file [Part A/main.py](Part%20A/main.py).

Before running script, two variables have to be configures which is ```file_extension``` and ```file_type```. The first one is self explanatory, it takes the value of the file extension that is meant to be scraped (like ```.pdf```). <br>
The latter is the switch case for the two subtasks. Setting the value as ```all``` will scrape all file links and put in the ```urls.txt``` file, and value of ```office``` will only scrape files which are under an office in the intranet site and put them under their various office files.

I ran the script beforehand and have uploaded the generated files also, which can be found under [Part A/Files/](Part%20A/Files/).

## Part C 
> Go through the codebase of the events submdoule and try to make a flowchart of the event flow from the codebase - from event creation to getting completed. You can use any tool you are comfortable with (like draw.io, Lucidchart, etc.)

![Flowchart](Part%20C/Flowchart.png)