# Thomas van Genderen Spring 2021 

# The Past in Perspective

The idea of this site is to bring history into perspective. I envision the user navigating to a year in time and seeing the technology, economy, government etc. of that year. 
The data could be scraped from Wikipedia and displayed on the site. the user will be able to select an object and navigate to its Wikipedia page.

## Problem statement

History is traditionally taught as a series of facts with dates, but context and contemporary events are often disregarded. I want to gather these loose facts on an intuitive timeline that gives a more holistic of overview of history. Sites like http://histography.io/ are rare and often too global (or too narrow like http://www.tiki-toki.com/timeline/entry/585659/Holocaust-in-Europa/ and https://www.kolonienvanweldadigheid.eu/tijdlijn/. They focus of specific periods of history). The target audience will be those interested in Dutch history with a need of context to complement general facts and figures.

## Solution description

The application will be a site that displays which events took place in the same year. Users fill in the data of events relevant to Dutch history into a SQL database. Data will then be displayed on an interactive representation of a timeline. The admin will validate the data provided by the users and when they 

Seperate types of events will be displayed in marked rows, this way the users can see different developments that happened around the same time.

Wikipedia is hard to scrap due to the lack of uniformity. Therefore the data will have to be entered manually. The admin will be able to enter items directly into the database. Users will have their first entries ratified by the admins and after a certain degree of reliability has been estabilished, they will be free to enter data directly. (Admins can still remove faulty data.)

Afterwards the Admin would still need the capacity to police individual users for quality control.
## Details and sketches

![Welcome page for the frontend](doc/Welcome_page_2.png)
![Mainpage eith timeline](doc/Timeline_page_2.png)
![User interactability](doc/Interaction_Design_1.png)

Scraped from Wikipedia will be an URL, picture, summary, dates, names, and possibly more with the use of __BeautifulSoup4__

The database will be created and interacted with with the use of __SQLAlchemy__

The tool for the JS interactive timeline will be __TimelineJS__



Challenges:  

A function will need to be coded to efficiently scrape relevant data in Dutch. Wikipedia is not consistent in its page-design.

The scraped data is not guaranteed to be consistent in composition. The database will need to be flexible and organised. This is something to figure out while designing it.

The mainpage will be fully interactable and will link to different Wikipedia pages. It needs to be created automaticaly based on the database. This will require a lot of JS integration. (A good example is https://www.kaapskil.nl/ontdek/400-jaar-skil/)

# ideas for more complexity:
- User interaction /  commenting
- web scraping (hard)
- better filter system
- opening new windows with a more detailed database for each topic?
- admin control over what is added/commented?
- locatie gebonden
- inzoomen geeft meer detail
- volledig door gebruikers laten invullen (3 item verificatie?)
- doorklikken naar feitjespaginas
- meerdere tijdlijnen onder elkaar hebben? (zelfde jaartal?)