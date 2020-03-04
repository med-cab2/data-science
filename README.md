# data-science
Modeling and Flask API
Proposal

- What problem does your app solve?
New users of medical marijuana want to be able to use marijuana for a non pharmaceutical way to relieve some of their ailments. While doing so, a client will want to find which particular strain is best for their particular ailment.

- Be as specific as possible; how does your app solve the problem?
     Due to the increase of legalization of medical marijuana throughout the country, more people are choosing to go a more holistic route in terms of pain management, etc. With MedCab, a user will be able to register, and give us some information in regards to their individual needs. The client will be able to search different strains, get a short introduction on that particular strain, and decide which are best for them. They will be able to save a list of strains that they have chosen for later use.

- What is the mission statement?
Offering our users a reliable source of information to help them satisfy their needs for alternative medicine. App for new cannabis consumers (especially those trying to get off of pharmaceuticals) who want to use cannabis as a means to battle medical conditions and ailments. Help patients find the right strains, dosing, intake method and intake schedule! (NEEDS SUMMARIZED) 
Features

- What features are required for your minimum viable product?


User creation and login(PENDING)
Dashboard( includes form where user inputs ailments, medical issues)(PENDING)
Strain Recommender(PENDING)
(once user submits provided data, strain recommender should be able to provide user with strain suggestions)(PENDING)
The ability to save Recommendations(PENDING)
(post request: JARED,)(PENDING)

- What features may you wish to put in a future release?
(LOOK AT LEAFLY , gps location to dispensaries?)

- What do the top 3 similar apps do for their users?
Check Leafly, Weed Maps, HighThere!,  Weed Scale 4.20(Pending)
Frameworks - Libraries

- What 3rd party frameworks/libraries are you considering using?
Have not Discussed yet…….
- Do APIs require you to contact its maintainer to gain access?
Have not Discussed yet…….
- Are you required to pay to use the API?
Have not Discussed yet…….
- Have you considered using Apple Frameworks? (MapKit, Healthkit, ARKit?)
Have not Discussed yet…….
For Data Scientists


- Describe the Established data source with at least rough data able to be provided on day 1.

Possibilities:
Source data directly from Leafly (Pending)
Scrape reviews and data from Leafly
Scrape PDF of Cannabis Health Index (https://www.barnesandnoble.com/w/the-cannabis-health-index-uwe-blesching/1121377615)
Scrape PDF of Leafly Handbook (https://www.barnesandnoble.com/w/the-leafly-guide-to-cannabis-the-leafly-team)
Scrape PotGuide.com (https://potguide.com/strain-profiles/)

- You can gather information about the data set you’ll be working with from the project description. Be sure to collaborate with your PM, and your Backend Architect to chat about the resources you have.

Data might include:
THC content
CBD Content
User reviews
Symptom relief
Strain Type: (Sativa, Indica, Hybrid)

- Write a description for what the DS problem is (what uncertainty/prediction are we trying to do here? Sentiment analysis? Why is this a useful solution to a problem?)

Identify the most effective products (MVP) administration methods, and dosing practices for your needs and goals (STRETCH).

- Describe a target (e.g. JSON format or such) for output that DS students can deliver to web/other students for them to ingest and use in the app

Flask is able to relay JSON objects. Will the data engineers communicate with front end or back end directly?

So far we’re looking at receiving text data description of what the user expects to solve with cannabis. The DS team will return a strain prediction in JSON format.
Target Audience

- Who is your target audience? Be specific.

People suffering from ailments that could be potentially aided by the use of cannabis products. People in search of alternative medicine so they aren’t reliant on Pharmaceutical drugs  (with potential undesired side effects)

- What feedback have you gotten from potential users?

(Jared considered reaching out to some Medical Users in the SoCAL area) anyone else living in a LEGAL state?

- Have you validated the problem and your solution with your target audience? How?

Research

- Research thoroughly before writing a single line of code. Solidify the features of your app conceptually before implementation. Spend the weekend researching so you can hit the ground running on Monday.
Prototype Key Feature(s)

User Creation and Login
Customer will be able to have a custom username as well as password. Will register with Name, email, location.
Information Form
Customer will fill out a form based upon constraints that will be submitted to the DS API
