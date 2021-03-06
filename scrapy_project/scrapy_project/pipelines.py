from questions.models import  Bmbf_model, Wiki_model



class ScrapyProjectPipeline(object):

    def process_item(self, item, spider):  # this function scraped data from wiki and store it into database

        for item_data in range(int(len(item["title"]))):#calling for 1 time
            if spider.name == "SpiderWiki":
                MyModel = Wiki_model() #Wiki_model() #change for wiki table
                MyModel.Title = item['title'][item_data]
                MyModel.Dates = item['date'][item_data]
                MyModel.Url = item['url'][item_data]
                MyModel.PaperType = item['paperType'][item_data]
                MyModel.Where = item['where'][item_data]
                MyModel.Deadline = item['deadline'][item_data]
                MyModel.save()
            elif spider.name == "SpiderBmbf":
                MyModel = Bmbf_model()
                MyModel.Title = item['title'][item_data]
                MyModel.Dates = item['date'][item_data]
                MyModel.Url = item['url'][item_data]
                MyModel.Deadline = item['deadline'][item_data]
                MyModel.save()

        wiki_all_items = Wiki_model.objects.all()
        wiki_items = Wiki_model.objects.values_list('Url').distinct()

        for x in wiki_items:
                    not_repeated = ''.join(x)

                    count = 0
                    for for_url in wiki_all_items:
                        repeated_url = str(for_url.Url)

                        if not_repeated == repeated_url:
                            count += 1

                            if (count == 1):
                                print( repeated_url)
                            elif (count > 1):
                                id = for_url.id
                                item_delete = Wiki_model.objects.get(id=id)
                                item_delete.delete()


        bmbf_all_items = Bmbf_model.objects.all()
        bmbf_items = Bmbf_model.objects.values_list('Url').distinct()

        for x in bmbf_items:
                    not_repeated = ''.join(x)

                    count = 0
                    for for_url in bmbf_all_items:
                        repeated_url = str(for_url.Url)

                        if not_repeated == repeated_url:
                            count += 1

                            if (count == 1):
                                print( repeated_url)
                            elif (count > 1):
                                id = for_url.id
                                item_delete = Bmbf_model.objects.get(id=id)
                                item_delete.delete()