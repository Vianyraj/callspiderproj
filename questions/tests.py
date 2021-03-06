from django.test import TestCase
# import schedule
# import time
# # Create your tests here.
# from scrapy_django.questions.management.commands.run_spider import Command
#
#
# com=Command()
# com.handle()


# schedule.every(5).seconds.do(com.handle)
#
# while 1:
#     schedule.run_pending()
#     time.sleep(1)


import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy_project.scrapy_project.spiders.Spiders import SpiderBmbf,SpiderWiki
#from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Run_spiders:
    ReactorStarted=0
    def __init__(self):
        configure_logging()
        self.ReactorStarted=0

    def f(self):
        runner = CrawlerRunner()
        runner.crawl(SpiderBmbf)

        if (self.ReactorStarted==0):
            d = runner.join()
            d.addBoth(lambda _: reactor.stop())
            reactor.run()  # the script will block here until all crawling jobs are finished
        self.ReactorStarted=1
    # def run_spider(self):
    #     p = Process(target=self.f())
    #     print("forked")
    #     p.start()
    #     p.join()




# Create your views here.
from time import sleep

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.core.paginator import Paginator,EmptyPage
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.views import APIView



from django.contrib.auth.forms import UserCreationForm
from .models import  Wiki_model, Bmbf_model

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control#for again not letting the user to enter into session when
                                                       #back button is pressed

#filters.py
from .filters import OrderFilter, OrderFilter1
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework import generics

from .serializers import WikiSerializer, BmbfSerializer
import datetime








def registerView(request):
    form = "Dummy String"
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=UserCreationForm()

    return render(request,'registration/register.html',{'form':form})




    # Redirect to a success page.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

class WikiList(APIView):
    def get(self,request):
        Wikiobjects= Wiki_model.objects.all()
        serializer = WikiSerializer(Wikiobjects, many=True)
        return Response(serializer.data)


class bmbfjson(generics.ListAPIView):
    serializer_class= BmbfSerializer
    queryset = Bmbf_model.objects.all()
    filter_backends= (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('id','Title','Url','Dates','Deadline')
    search_fields = ('id','Title', 'Url','Dates','Deadline')
    ordering_fields =('id','Title', 'Url','Dates','Deadline')

class Wikijson(generics.ListAPIView):
    serializer_class= WikiSerializer
    queryset = Wiki_model.objects.all()
    filter_backends= (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('id','Title','Url','Dates','Deadline')
    search_fields = ('id','Title', 'Url','Dates','Deadline')
    ordering_fields =('id','Title', 'Url','Dates','Deadline')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login_url')
def get_Call_for_Proposals(request):#used for searching with filter



                contextwiki = dict()
                contextwiki['contextwiki'] = Wiki_model.objects.all()
                contextwiki = OrderFilter(request.GET, queryset=Wiki_model.objects.all())
                contextBmbf = dict()
                contextBmbf['contextBmbf'] = Bmbf_model.objects.all()
                contextBmbf = OrderFilter1(request.GET, queryset=Bmbf_model.objects.all())
                stuff_items = Bmbf_model.objects.values('Title', 'Url','Deadline').distinct()[::-1]
                stuff_items1 = Wiki_model.objects.values('Title','Where', 'Url','Deadline').distinct()[::-1]
                paginator = Paginator(stuff_items,10)
                p1= Paginator(stuff_items1,10)



                page_num= request.GET.get('page',1)

                try:
                    page = paginator.page(page_num)
                except EmptyPage:
                    page= paginator.page(1)



                context = {
                    'contextwiki': contextwiki,
                    'contextBmbf': contextBmbf,
                    'contextpage': page,

                }

                return render(request, 'dashboard.html', context)  # till here







@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login_url')
def get_Call_for_Papers(request):  # used for searching with filter
        fromdate = request.GET.get('fromdate')
        todate = request.GET.get('todate')


        contextwiki = dict()
        contextwiki['contextwiki'] = Wiki_model.objects.all()
        contextwiki = OrderFilter(request.GET, queryset=Wiki_model.objects.all())
        stuff_items = Wiki_model.objects.values('Title', 'Where', 'Url', 'Deadline').distinct()[::-1]
        paginator_items = Paginator(stuff_items, 10)
        page_num = request.GET.get('page', 1)

        try:
            page = paginator_items.page(page_num)
        except EmptyPage:
            page = paginator_items.page(1)



        context = {
            'contextwiki': contextwiki,
            'contextpage': page,

        }

        return render(request, 'Call_for_Papers.html', context)  # till here

#asdasdasd






def Search_Call_for_Papers(request):#used for searching with filter
                from .models import Wiki_model, Bmbf_model
                fromdate = request.GET.get('fromdate')
                todate = request.GET.get('todate')
                todelete = request.GET.get('todelete')
                extremes = request.GET.get('extremes')


                if  fromdate:
                    count = 0
                    wiki_all_items = Wiki_model.objects.all()
                    wiki_items = Wiki_model.objects.values_list('Url').distinct()

                    for x in wiki_items:
                        not_repeated = ''.join(x)
                        #print("f",not_repeated)
                        count = 0
                        for for_url in wiki_all_items:
                            repeated_url = str(for_url.Url)

                            if not_repeated == repeated_url:
                                count += 1
                                #print("count", count)
                                if (count == 1):
                                    pass
                                elif (count > 1):
                                    id = for_url.id
                                    item_delete = Wiki_model.objects.get(id=id)
                                    #item_delete.delete()  # https://www.oreilly.com/library/view/django-essentials/9781783983704/ch06s06.html


                    from_to_dates = Wiki_model.objects.raw(
                        'select id,Title,Dates,Url,Deadline from questions_wiki_model where Deadline between "' + fromdate + '" and "' + todate + '" ')

                    Wiki_model = Wiki_model.objects.all()
                    lesser_dates = {"Title": [],
                              "Date": [],
                              "Url": [],
                              "paperType": [],
                              "Where": [],
                              "Deadline": []
                              }
                    greater_dates = {"Title": [],
                               "Date": [],
                               "Url": [],
                               "paperType": [],
                               "Where": [],
                               "Deadline": []
                               }

#part2 getting dates greater tan or less than particular date
                    fromdate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')

                    for things in Wiki_model:
                        count = 0
                        if extremes == "Lesserdates":
                            from_to_dates = Wiki_model.none()

                            if things.Deadline is not None:
                                if fromdate > things.Deadline:

                                    if things.Title == lesser_dates["Title"]:
                                        count += 1


                                    lesser_dates["Title"].append(things.Title)
                                    lesser_dates["Deadline"].append(things.Deadline)
                                    lesser_dates["Url"].append(things.Url)
                                    lesser_dates["Where"].append(things.Where)





                        elif extremes == "Greaterdates":
                            from_to_dates = Wiki_model.none()
                            #searchresult=Wiki_model
                            if things.Deadline is not None:
                                if fromdate < things.Deadline:

                                    greater_dates["Title"].append(things.Title)
                                    greater_dates["Deadline"].append(things.Deadline)
                                    greater_dates["Url"].append(things.Url)
                                    greater_dates["Where"].append(things.Where)



                    context = {
                        "from_to_dates": from_to_dates,  # important dont delete
                        "lesser_dates": lesser_dates,
                        "greater_dates": greater_dates,  # important dont delete

                    }
                    return render(request, 'index2.html', context)

                else:

                    contextwiki = dict()
                    contextwiki = Wiki_model.objects.all()


                    context = {
                        'contextwiki': contextwiki,
                    }

                    return render(request, 'index2.html', context)

from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy_project.scrapy_project.spiders.Spiders import SpiderBmbf,SpiderWiki

class Command(BaseCommand):
    help = "Release the spiders"
    process = CrawlerProcess(get_project_settings())
    process.crawl(SpiderBmbf)
    process.crawl(SpiderWiki)
    print("spider runninggggggggggggggggggggggggggggggggggggggggggkkkkkkkkkkkk0000")
    process.start()
    sleep(15)
    print("spider runninggggggggggggggggggggggggggggggggggggggggggkkkkkkkkkkkk0000111")
    process.stop()
    print("spider runninggggggggggggggggggggggggggggggggggggggggggkkkkkkkkkkkk0000222")
    #process.end()
    #     # temp=ScrapyProjectPipeline()
    #     # temp.process_item({"title":"abc"},SpiderBmbf)
    # def handle(self, *args, **options):
    #     process = CrawlerProcess(get_project_settings())
    #     process.crawl(SpiderBmbf)
    #     process.crawl(SpiderWiki)
    #     print("spider runninggggggggggggggggggggggggggggggggggggggggggkkkkkkkkkkkk123")
    #     process.start()


from django.db.models import Count
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login_url')
def Search_Call_for_Proposals(request):#used for searching with filter

            fromdate = request.GET.get('fromdate')
            todate = request.GET.get('todate')
            todelete = request.GET.get('todelete')
            extremes = request.GET.get('extremes')

            if fromdate:
                print("printinfsdsdsdsdsdsdssdsdsdsdsdkljklllllllllllllll")
                # process = CrawlerProcess(get_project_settings())
                # process.crawl(SpiderBmbf)
                # process.crawl(SpiderWiki)
                # print("spider runninggggggggggggggggggggggggggggggggggggggggggkkkkkkkkkkkk0000")
                #process.start()
                #Command()
                # Command1()
                help = "Release the spiders"
                # process = CrawlerProcess(get_project_settings())
                # process.crawl(SpiderBmbf)
                # process.crawl(SpiderWiki)
                # print("spider runninggggggggggggggggggggggggggggggggggggggggggkkkkkkkkkkkk0000")
                # process.start()
                # sleep(15)
                # print("spider runninggggggggggggggggggggggggggggggggggggggggggkkkkkkkkkkkk0000111")
                # process.stop()
                # print("spider runninggggggggggggggggggggggggggggggggggggggggggkkkkkkkkkkkk0000222")
                #

            if  fromdate :
                count=0
                Bmbf_all_items = Bmbf_model.objects.all()
                Bmbf_items = Bmbf_model.objects.values_list('Url').distinct()

                for x in Bmbf_items:
                    non_repeated=''.join(x)

                    count=0
                    for items in Bmbf_all_items:

                        j=str(items.Url)

                        if non_repeated == j :
                            count+=1
                            #print("count",count)
                            if (count==1):
                                    pass
                                    #print("f",non_repeated)
                                    #print("kjh", items.Url,items.id)
                            elif (count > 1):
                                # print("count", count)
                                # print("f", non_repeated)
                                # print("kjh", items.Url, items.id)
                                id=items.id
                                item_delete=Bmbf_model.objects.get(id=id)
                                #print("idd",item_delete)
                                #item_delete.delete() # https://www.oreilly.com/library/view/django-essentials/9781783983704/ch06s06.html



                from_to_dates = Bmbf_model.objects.raw(
                    'select id,Title,Dates,Url,Deadline from questions_bmbf_model where Deadline between "' + fromdate + '" and "' + todate + '" ')

                Bmbfmodel = Bmbf_model.objects.all()
                lesser_dates = {"Title": [],
                          "Date": [],
                          "Url": [],
                          "paperType": [],
                          "Where": [],
                          "Deadline": []
                          }
                greater_dates = {"Title": [],
                          "Date": [],
                          "Url": [],
                          "paperType": [],
                          "Where": [],#changed12/20/2021
                          "Deadline": []
                          }

                todate = datetime.datetime.strptime(todate, '%Y-%m-%d')
                fromdate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')

                for things in Bmbfmodel:

                   count = 0
                   if extremes=="Lesserdates":
                    from_to_dates=Bmbf_model.objects.none()

                    if things.Deadline is not None:
                        if fromdate>things.Deadline:

                            if things.Title == lesser_dates["Title"]  :
                                count+=1


                            lesser_dates["Title"].append(things.Title)
                            lesser_dates["Deadline"].append(things.Deadline)
                            lesser_dates["Url"].append(things.Url)



                   elif extremes=="Greaterdates":
                        from_to_dates=Bmbf_model.objects.none()
                        if things.Deadline is not None:
                         if fromdate<things.Deadline:

                            greater_dates["Title"].append(things.Title)
                            greater_dates["Deadline"].append(things.Deadline)
                            greater_dates["Url"].append(things.Url)


                context= {
                         "from_to_dates": from_to_dates,#important dont delete
                         "lesser_dates":lesser_dates,
                         "greater_dates":greater_dates,#important dont delete

                }



                return render(request, 'Call_for_Proposals.html', context)

            else:
                bmbf_values = Bmbf_model.objects.all()

                context = {

                    'bmbf_values': bmbf_values,

                }
                return render(request, 'Call_for_Proposals.html', context)  # till here

















