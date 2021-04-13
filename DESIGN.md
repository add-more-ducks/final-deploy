# Thomas van Genderen Spring 2021 

# Design Document

[
    Based on your proposal, you can now start studying your problem in a more technical fashion. Map the separate parts of the solution onto the framework(s) that you are using. What APIs, methods or techniques do you need to implement each feature?

Think about and fully express how the user interface will be handled, where the data is coming from, and how the various parts will work together to form a complete application.

The teaching staff and your fellow students can help you spot fundamental problems that need to be solved, or if technical limitations will likely prevent you from finishing the project.

!!! It is expected that you separate, in your code, handling of the user interface from data management and from complex algorithms whenever possible. It should be clear from your design document how you are going to do this!!!


# Features
First list the features that users will be able to use:

Include a brief list of main features that will be available to users. All features should also be visible in the sketch. If you have complicated features, it might be good to create a separate sketch for each feature. Yes, you will do a lot of sketching! This is required.

Mark which features define the minimum viable product (MVP) and which parts may be optional to implement. An MVP has a minimum amount of features, but is still a good product. This is the part that you have to agree on/negotiate with your teacher before starting to code!

# User interface
Draw a detailed walkthrough of the user interface of your app. You should draw multiple “screens” separately, in order to make very clear the things that happen on screen when navigating the app.

You must create “professional” drawings using a software tool. Some examples of what we expect:


Do make sure that you use realistic content in your sketches! Google a few images, write real texts and make sure it gives a good impression of what you want to make.

Lists
Include a couple of lists that are more detailed than in your proposal document:

a list of APIs and frameworks or plugins that you will be using to provide functionality in your app (and explain exactly what features you’re using them for)

a list of data sources if you will get data from an external source, including information on how your are going to filter and transform the data for your project, with examples of raw data and the actual data you need

] 

# Don't forget to update README.md !!!

## Features

Include a brief list of main features that will be available to users. All features should also be visible in the sketch. If you have complicated features, it might be good to create a separate sketch for each feature. Yes, you will do a lot of sketching! This is required.

The projects main aim is to provide a platform for a easy, holistic and chronological display of historical events for its users. The aim is to provide a way to enter data into a database with a standardised format, then aorder that data in a chronological order, after which it is displayed to the user while taking the assigned type of the data in regard.

### Main Features 
- Manual entry of items to be displayed
- Scraping data from Wikipedia (and other sites).
- Selecting filters for events.
- Building a timeline based on filters.
- Storing Wikipedia data in SQL database.
- Zoom feature on timeline scope.
- Selecting events on timeline brings up extensive information and link to article.
- Data storage using a SQL database. (MVP)
- Data exchange between SQL database and Google Spreadsheet file(s). (MVP)
- Spreadsheet data is displayed to user on a highly interactive timeline. (MVP)

![User interactability](doc/Interactie.png)
![Database design](doc/UML-klassendiagram.png)
![Database design](doc/UML-ClassDiagram.jpeg)
