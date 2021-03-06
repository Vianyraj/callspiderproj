

This has 2 parts Django and scrapy projects 

1> django_project is the django project and it has an app called questions.

2> scrapy_project is the scrapy project and has a spider called Crawler in stackoverflow.py.




a>	To initiate the crawler.
		$  python manage.py run_spider

b>	To run the server we have to give in django_project path
		$  python manage.py runserver
 
c>	To restart the server we have to use the runspider button.


 1>	a> Scrapy (Spiders.py) contains the 2 spiders(SpiderBmbf(scrapy.Spider) and SpiderWiki(scrapy.Spider)) which has methods to 
	crawl the required page and the data is stored as items(type:scrapyfield)
	b> The items are loaded to the pipeline where items are processed 
	and then it is saved to the database. The data to be stored are stored in the items 
	which is of the method described by the Django models.
	c> An error is shown if there is any item not present in the xpath i.e, if the xpath has changed.
	d> The repeated data in the database is checked and if present are deleted.

 2>	a> Django Models are created for database(ORM).
    	b> Views functions are used to get the data from database.
     	c> The display of the data from database is done in the dashboard.html file. 
	d> A Login and registration function is present.
		login function    Name: vinay     password: 1234 

 3> 	a> Search function is done using django backend filters.
	b> Json data is displayed on page /wikijson(Call for Papers) and /bmbfjson(Call for Proposals) 
	    with the rest framework.








