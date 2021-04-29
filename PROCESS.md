## Thomas van Genderen - Spring 2021

# 15 April 
I handed in my Design doc yesterday. 
Today I will try to contact the TA's again.

- The choice you’ve made
- What you expect to happen as a result of that choice (at this moment in time)
- Why you expect things to pan out that way

# 19 April

Need to decide what I add to increase the complexity and depth to my design doc.
- No decision has yet been taken. Tomorrow I will try again.
- Some unneccessary elements have been trimmed from the design document.

# 20 April

- Started adding new ideas to the design of the application.
-   User input for items
-   Admin validation of users.
This solves the problem of data extraction from wikipedia as it can be easily interpreted by users.

# 21 April
- I chose to give the admin his own page from which most of the site-maintenance controls are accessible.

# 22 April
I am faced with the choice of what to with the .csv file. The TimelineJS site advices to use google spreadsheets. I have found a possible way to forgo that external file and use a local .csv file. source: https://framagit.org/eduinfo/timelinejs-local/-/tree/master/public
other option:
https://timeline.knightlab.com/docs/instantiate-a-timeline.html
https://www.geeksforgeeks.org/json-dumps-in-python/

I will make it work via JSON, boorstrap and local files for the JS.

Today I got the site running, but have not implemented any functions yet.

# 23 April
I have dicided to make hosting the .csv locally the first priority. Afterwards i might try to run timelineJS completely local. 

# 23 April
I run into the problem of having Flask communicate with the .csv and .js files.
In order to use the .js files I need to keep them in a /static folder. To communicate with the .csv, it needs to stay there as well. I now see the difficulty of working with .csv as this probably means it will be hard to edit later. Should I stay with the external google sheets?
Maybe I should just keep the events in my SQL database instead. Will I be able to use them instead?. 

I have a hard time deciding what to do. Hopefully i can discuss it with other students.

Should i work via google forms?

Now I got embeded to work, but it can't find the json
