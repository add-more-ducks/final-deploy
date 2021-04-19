### Thomas van Genderen Spring 2021 

# Design Document

## Features

The projects main aim is to provide a platform for a easy, holistic and chronological display of historical events for its users. The aim is to provide a way to enter data into a database with a standardised format, then aorder that data in a chronological order, after which it is displayed to the user while taking the assigned type of the data in regard.

### Main features 
- Manual entry of items to be displayed
- Scraping data from Wikipedia (and other sites).
- Selecting filters for types on events. (government, art, religion, royalty, science, warfare, etc.)
- Building a timeline based on the above mentioned filters.
- Storing Wikipedia data in SQL database.
- Zoom feature on timeline scope.
- Selecting events on timeline brings up extensive information and link to article.
- Data storage using a SQL database. (MVP)
- Data exchange between SQL database and Google Spreadsheet file(s). (MVP)
- Spreadsheet data is displayed to user on a highly interactive timeline. (MVP)

## User interface
![User interactability](doc/Interaction_Design_1.png)
Still needs work

![Welcome page](doc/Welcome_page_2.png)

![Timeline page](doc/Timeline_page_2.png)


## Database
Design

![Database design](doc/UML-Class_Diagram.jpeg)

Example

![Database example](doc/UML-Class_Example.png)

## Lists
### Required for this project will be:

Scraped from Wikipedia will be an URL, picture, summary, dates, names, and possibly more with the use of __BeautifulSoup4__

The tool for the JS interactive timeline will be __TimelineJS__. It is very interactive and easy to input data to.

__Google spreadsheet__ will be one of the main data repositories in a csv format. Google spreadsheets can store an online accesable .csv file which houses the data that __TimelineJS__ uses to construct a timeline. It is also a useful format as it is easy to edit.

