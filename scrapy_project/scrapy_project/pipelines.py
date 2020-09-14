from questions.models import Paper_model,Bmbf_model



class ScrapyProjectPipeline(object):

    def process_item(self, item, spider):  # this function scraped data from wiki and store it into database
        #print(item)

        for i in range(int(len(item["title"]))):#calling for 1 time
            print(spider.name)
            if spider.name == "SpiderWiki":
                MyModel = Paper_model()
            elif spider.name == "SpiderBmbf":
                MyModel = Bmbf_model()
            MyModel = Paper_model()            #django model
            MyModel.Title = item['title'][i]
            MyModel.Dates = item['date'][i]
            MyModel.Url = item['url'][i]
            MyModel.PaperType = item['paperType'][i]
            MyModel.Where = item['where'][i]
            MyModel.Deadline = item['deadline'][i]
            MyModel.save()

    # def process_item(self, item, spider):  # this function scraped data from wiki and store it into database
    #     #print(item)                          #calling for 20 time
    #     MyModel = Paper_model()            #django model
    #     MyModel.Title = item['title']
    #     MyModel.Dates = item['date']
    #     MyModel.Url = item['url']
    #     MyModel.PaperType = item['paperType']
    #     MyModel.Where = item['where']
    #     MyModel.Deadline = item['deadline']
    #     MyModel.save()