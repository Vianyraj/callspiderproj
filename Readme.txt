Scrapy: 
PaperSpider is the main spider which will scrap the paths of different events,
itemloader loads it to the containers(like Eventname=ScrapyField()),
which are used in the PaperscrapyPipline to send the data to the Database.

Django:
1> Models(tables) are created from django in the database. 
2> The data sent from scrapy will be present in DB. 
3> Then list_todo_items is used to get all the data from database.
4> list.html is used to dispaly the data on html webpage. 


Files:
Scrapy:
1> paper_spider will contain spider with parse method to parse the paths of website 
and loader to load it.
2>items.py has the containers for storing data of the parsed items.
3>pipelines.py will upload the file to database with process_item

Django:
1>models.py has the table to be created in DB.
2>views.py contains list_todo_items method to get the objects from DB.
3>list.html will display all the objects collected in the above method. 


Steps:
1> In scrapy to run spider to put data to database: scrapy crawl paper
2> In django for running server: python manage.py runserver 