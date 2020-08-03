from questions.models import Paper_model


class ScrapyProjectPipeline(object):

    def process_item(self, item, spider):  # this function scraped data from wiki and store it into database
        MyModel = Paper_model()            #django model
        MyModel.Title = item['title']
        MyModel.Dates = item['date']
        MyModel.Url = item['url']
        MyModel.PaperType = item['paperType']
        MyModel.Where = item['where']
        MyModel.Deadline = item['deadline']
        MyModel.save()
