Bloc_1 Construction et alimentation d'une infrastructure de gestion de données.

Contact: Arnaud DALAIS
E-mail  : arnaud.dalais@free.fr

Video link : 👉  👈

Subject

The marketing team needs help on a new project. After doing some user research, the team discovered that 70% of their users who are planning a trip would like to have more information about the destination they are going to.

In addition, user research shows that people tend to be defiant about the information they are reading if they don't know the brand which produced the content.

Therefore, Kayak Marketing Team would like to create an application that will recommend where people should plan their next holidays. The application should be based on real data about:

    Weather
    Hotels in the area

The application should then be able to recommend the best destinations and hotels based on the above variables at any given time.

You can find the whole description of the project in 5 steps:

Step 1:
 cities_weather.ipynb is the first notebook where i creat the dataframe with the 35 cities and add with api the gps coordinates and the weather for the next week(save into ciyies_weather.csv), and plotling the 5 best destinations.

 Step 2:
 Scrape booking for hotels in the 35 cities, with scrapy (booking_spider.py) and at the end we have booking.json file

 Step 3:
 i merge the both file in cities_weather_booking.ipynb into a kayak.csv 

 Step 4:
 on uploading_to_s3_and_RDS.ipynb, i upload this csv on AWS S3, i extract, transform and load cleaned data(ETL) to RDS (connection with pgAdmin)

 Step 5;
 Ploting the 20 hotels of the 5 best destinations (on uploading_to_s3_and_RDS.ipynb )




