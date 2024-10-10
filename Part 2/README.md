# Part 2

## Part A
> Create a Python function that scrapes all links from the Intranet website, based on a file extension provided as input (e.g. .pdf). The function should ensure that only links within the intranet domain are collected, and not any other external links outside of intranet. Also, save the list of URLs in a text file (urls.txt). <br> You may use any python library you are comfortable with (like Scrapy, BeautifulSoup, etc.) for web scraping. <br> (Additional) Scraping by office types (like Academic, Admin, etc.) and saving them in different files.

The code for the script is in the file [Part A/main.py](Part%20A/main.py).

Before running script, two variables have to be configured which are ```file_extension``` and ```file_type```. The first one is self explanatory, it takes the value of the file extension that is meant to be scraped (like ```.pdf```). <br>
The latter is the switch case for the two subtasks. Setting the value as ```all``` will scrape all file links and put in the ```urls.txt``` file, and value of ```office``` will only scrape files which are under an office in the intranet site and put them under their various office files.

I ran the script beforehand and also uploaded the generated files, which can be found under [Part A/Files/](Part%20A/Files/).

## Part B
> We want to implement a feature in the Intranet website, where we store the version history and changes of the documents uploaded on the website. Think of how you would implement this feature. Try to go in the details of issues which can occur considering the current Intranet, and your experience with college linked to documents (like Timetable, etc)

The feature can take two routes:<br> 
(1.) We offload the duty of telling the website that a document is being updated to the uploader.<br>
(2.) We try to parse the version history of the documents from the name of the documents. 

1. This feature is relatively more straightforward to develop since we can just have the user select the document that is meant to be updated. The problem with this sort of versioning is that it adds more overhead to the uploader and sometimes they might just decide to not select the previous version, which may lead to outdated/two versions of information being propagated to the enduser.<br>
As can be seen in the homepage of intranet, the timetable files are unique and versioned, so I have to assume this method is followed for the important files.

2. This is the harder to develop for feature, since updated file names can be really inconsistent as can be seen below.
![Almanac](Part%20B/Almanac%20versioning.png)
![Rankings](Part%20B/Rankings%20versioning.png)
<br>We will have to implement some kind of indexing feature of all the files that have already been uploaded (Like the Part A of this task) and use that database to match substrings so as to tag them the same file. This issue is very prone to accidental verisioning to the wrong file since the mathcing cannot be 100% reliable.

I feel like the correct approach would be use a mix of both these options, when a user is uploading a file we can prompt them with some mathching files and ask if they would like to update these files or just create a new entry. And if the index mathcing fails they can manually select an already existing file to update. This reduces the overhead mentioned in (1.) by a bit and also reduces the error proneness of (2.). 

## Part C 
> Go through the codebase of the events submdoule and try to make a flowchart of the event flow from the codebase - from event creation to getting completed. You can use any tool you are comfortable with (like draw.io, Lucidchart, etc.)

![Flowchart](Part%20C/Flowchart.png)