


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



#for base command to run the process to call spiders.
from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy_project.scrapy_project.spiders.Spiders import SpiderBmbf,SpiderWiki



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

count=0

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login_url')
def get_Call_for_Proposals(request):#used for searching with filter
                count = 0
                Restart = request.GET.get('Restart')#Restarting the server
                Restartagain = request.GET.get('Restartagain')



                if Restart:
                    import random
                    import string
                    reading_file = open(
                        "C:/Users/Vinay/PycharmProjects/callspiderproj/scrapy_django/questions/views.py", "r")
                    # a_file = open("sample.txt", "r")
                    letters = string.ascii_lowercase
                    random_comments = "#" + ''.join(random.choice(letters) for i in range(10))

                    print(random_comments)

                    n = random.random()
                    list_of_lines = reading_file.readlines()
                    x = "Line2\n"
                    list_of_lines[1000] = random_comments
                    # alskdklad
                    # kjh
                    reading_file = open(
                        "C:/Users/Vinay/PycharmProjects/callspiderproj/scrapy_django/questions/views.py", "w")

                    reading_file.writelines(list_of_lines)

                    reading_file.close()
                    contextwiki = dict()
                    contextwiki['contextwiki'] = Wiki_model.objects.all()
                    contextwiki = OrderFilter(request.GET, queryset=Wiki_model.objects.all())
                    contextBmbf = dict()
                    contextBmbf['contextBmbf'] = Bmbf_model.objects.all()
                    contextBmbf = OrderFilter1(request.GET, queryset=Bmbf_model.objects.all())
                    stuff_items = Bmbf_model.objects.values('Title', 'Url', 'Deadline').distinct()[::-1]
                    stuff_items1 = Wiki_model.objects.values('Title', 'Where', 'Url', 'Deadline').distinct()[::-1]
                    paginator = Paginator(stuff_items, 10)
                    p1 = Paginator(stuff_items1, 10)

                    page_num = request.GET.get('page', 1)

                    try:
                        page = paginator.page(page_num)
                    except EmptyPage:
                        page = paginator.page(1)

                    buttons=1
                    # for l in range(1,10000):
                    #     buttons = 1
                    #     print("buttoonnnssss", buttons)
                    #     if l >= 9000:
                    #         buttons=0
                    #         print("buttoonnnssss",buttons)


                    context = {
                        'contextwiki': contextwiki,
                        'contextBmbf': contextBmbf,
                        'contextpage': page,
                        'buttons': buttons,

                    }

                    return render(request, 'dashboard.html', context)  # till here

                else:
                    buttons = 0

                    contextwiki = dict()
                    contextwiki['contextwiki'] = Wiki_model.objects.all()
                    contextwiki = OrderFilter(request.GET, queryset=Wiki_model.objects.all())
                    contextBmbf = dict()
                    contextBmbf['contextBmbf'] = Bmbf_model.objects.all()
                    contextBmbf = OrderFilter1(request.GET, queryset=Bmbf_model.objects.all())
                    stuff_items = Bmbf_model.objects.values('Title', 'Url', 'Deadline').distinct()[::-1]
                    stuff_items1 = Wiki_model.objects.values('Title', 'Where', 'Url', 'Deadline').distinct()[::-1]
                    paginator = Paginator(stuff_items, 10)
                    p1 = Paginator(stuff_items1, 10)

                    page_num = request.GET.get('page', 1)

                    try:
                        page = paginator.page(page_num)
                    except EmptyPage:
                        page = paginator.page(1)

                    context = {
                        'contextwiki': contextwiki,
                        'contextBmbf': contextBmbf,
                        'contextpage': page,
                        'buttons': buttons,

                    }

                    return render(request, 'dashboard.html', context)  # till here







@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login_url')
def get_Call_for_Papers(request):  # used for searching with filter
        fromdate = request.GET.get('fromdate')
        todate = request.GET.get('todate')
        count = 0
        Restartagain = request.GET.get('Restartinwiki')
        if Restartagain:
            import random
            import string

            reading_file = open(
                "C:/Users/Vinay/PycharmProjects/callspiderproj/scrapy_django/questions/views.py", "r")
            # a_file = open("sample.txt", "r")
            letters = string.ascii_lowercase
            m = "#" + ''.join(random.choice(letters) for i in range(10))

            print(m)
            buttons = 1
            n = random.random()
            list_of_lines = reading_file.readlines()
            x = "Line2\n"
            list_of_lines[1000] = m
            # alskdklad
            # kjh
            reading_file = open(
                "C:/Users/Vinay/PycharmProjects/callspiderproj/scrapy_django/questions/views.py", "w")

            reading_file.writelines(list_of_lines)

            reading_file.close()

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

        buttons=1

        context = {
            'contextwiki': contextwiki,
            'contextpage': page,
            'buttons':buttons

        }

        return render(request, 'Call_for_Papers.html', context)  # till here

#asdasdasd


from django.views.generic import TemplateView
class PostTemplateView(TemplateView):
    template_name= 'style.html'
def post_json(request):
    bmbf_values = Bmbf_model.objects.all()

    context = {

        'bmbf_values': bmbf_values,

    }
    return render(request, 'Call_for_Proposals.html', context)  # till here






def Search_Call_for_Papers(request):#used for searching with filter
                from .models import Wiki_model, Bmbf_model
                fromdate = request.GET.get('fromdate')
                todate = request.GET.get('todate')
                todelete = request.GET.get('todelete')
                extremes = request.GET.get('extremes')


                if  fromdate and todate:
                    from_to_dates = Wiki_model.objects.none()
                    lesser_dates = Wiki_model.objects.none()
                    greater_dates = Wiki_model.objects.none()
                    if extremes != "Lesserdates" and extremes != "Greaterdates":
                        from_to_dates = Wiki_model.objects.raw(
                            'select * from questions_wiki_model where Deadline between "' + fromdate + '" and "' + todate + '" ')
                        lesser_dates = Wiki_model.objects.none()
                        greater_dates = Wiki_model.objects.none()
                    elif extremes == "Lesserdates":
                        greater_dates = Wiki_model.objects.none()
                        lesser_dates = Wiki_model.objects.raw(
                            'select * from questions_wiki_model where (Deadline <= "' + fromdate + '"  ) ORDER BY Deadline')
                    elif extremes == "Greaterdates":
                        lesser_dates = Wiki_model.objects.none()
                        greater_dates = Wiki_model.objects.raw(
                            'select * from questions_wiki_model where (Deadline >= "' + fromdate + '"  ) ORDER BY Deadline ')


                    # python code to show lesser or greater dates
#                     count = 0
#                     wiki_all_items = Wiki_model.objects.all()
#                     wiki_items = Wiki_model.objects.values_list('Url').distinct()
#
#                     for x in wiki_items:
#                         not_repeated = ''.join(x)
#                         #print("f",not_repeated)
#                         count = 0
#                         for for_url in wiki_all_items:
#                             repeated_url = str(for_url.Url)
#
#                             if not_repeated == repeated_url:
#                                 count += 1
#                                 #print("count", count)
#                                 if (count == 1):
#                                     pass
#                                 elif (count > 1):
#                                     id = for_url.id
#                                     item_delete = Wiki_model.objects.get(id=id)
#                                     #item_delete.delete()  # https://www.oreilly.com/library/view/django-essentials/9781783983704/ch06s06.html
#
#
#                     from_to_dates = Wiki_model.objects.raw(
#                         'select * from questions_wiki_model where  (Deadline between "' + fromdate + '" and "' + todate + '" ) ORDER BY Deadline ')
#
#                     Wiki_model = Wiki_model.objects.all()
#                     lesser_dates = {"Title": [],
#                               "Date": [],
#                               "Url": [],
#                               "paperType": [],
#                               "Where": [],
#                               "Deadline": []
#                               }
#                     greater_dates = {"Title": [],
#                                "Date": [],
#                                "Url": [],
#                                "paperType": [],
#                                "Where": [],
#                                "Deadline": []
#                                }
#
# #part2 getting dates greater tan or less than particular date
#                     fromdate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')
#
#                     for things in Wiki_model:
#                         count = 0
#                         if extremes == "Lesserdates":
#                             from_to_dates = Wiki_model.none()
#
#                             if things.Deadline is not None:
#                                 if fromdate > things.Deadline:
#
#                                     if things.Title == lesser_dates["Title"]:
#                                         count += 1
#
#
#                                     lesser_dates["Title"].append(things.Title)
#                                     lesser_dates["Deadline"].append(things.Deadline)
#                                     lesser_dates["Url"].append(things.Url)
#                                     lesser_dates["Where"].append(things.Where)
#
#
#
#
#
#                         elif extremes == "Greaterdates":
#                             from_to_dates = Wiki_model.none()
#                             #searchresult=Wiki_model
#                             if things.Deadline is not None:
#                                 if fromdate < things.Deadline:
#
#                                     greater_dates["Title"].append(things.Title)
#                                     greater_dates["Deadline"].append(things.Deadline)
#                                     greater_dates["Url"].append(things.Url)
#                                     greater_dates["Where"].append(things.Where)
#
#

                    context = {
                        "from_to_dates": from_to_dates,  # important dont delete
                        "lesser_dates": lesser_dates,
                        "greater_dates": greater_dates,  # important dont delete

                    }
                    return render(request, 'Call_for_Papers_Search_Result.html', context)


                elif fromdate:
                    from_to_dates = Wiki_model.objects.none()
                    lesser_dates = Wiki_model.objects.none()
                    greater_dates = Wiki_model.objects.none()
                    if extremes != "Lesserdates" and extremes != "Greaterdates":
                        from_to_dates = Wiki_model.objects.raw(
                            'select * from questions_wiki_model where Deadline between "' + fromdate + '" and "' + todate + '" ')
                        lesser_dates = Wiki_model.objects.none()
                        greater_dates = Wiki_model.objects.none()
                    elif extremes == "Lesserdates":
                        greater_dates = Wiki_model.objects.none()
                        lesser_dates = Wiki_model.objects.raw(
                            'select * from questions_wiki_model where (Deadline <= "' + fromdate + '"  ) ORDER BY Deadline')
                    elif extremes == "Greaterdates":
                        lesser_dates = Wiki_model.objects.none()
                        greater_dates = Wiki_model.objects.raw(
                            'select * from questions_wiki_model where (Deadline >= "' + fromdate + '"  ) ORDER BY Deadline ')
                    # python code to show lesser or greater dates
                    #                     count = 0
                    # count = 0
                    # wiki_all_items = Wiki_model.objects.all()
                    # wiki_items = Wiki_model.objects.values_list('Url').distinct()
                    #
                    # for x in wiki_items:
                    #     not_repeated = ''.join(x)
                    #     # print("f",not_repeated)
                    #     count = 0
                    #     for for_url in wiki_all_items:
                    #         repeated_url = str(for_url.Url)
                    #
                    #         if not_repeated == repeated_url:
                    #             count += 1
                    #             # print("count", count)
                    #             if (count == 1):
                    #                 pass
                    #             elif (count > 1):
                    #                 id = for_url.id
                    #                 item_delete = Wiki_model.objects.get(id=id)
                    #                 # item_delete.delete()  # https://www.oreilly.com/library/view/django-essentials/9781783983704/ch06s06.html
                    #
                    # from_to_dates = Wiki_model.objects.raw(
                    #     'select * from questions_wiki_model where  (Deadline >= "' + fromdate + '"  ) ORDER BY Deadline ')
                    #
                    # Wiki_model = Wiki_model.objects.all()
                    # lesser_dates = {"Title": [],
                    #                 "Date": [],
                    #                 "Url": [],
                    #                 "paperType": [],
                    #                 "Where": [],
                    #                 "Deadline": []
                    #                 }
                    # greater_dates = {"Title": [],
                    #                  "Date": [],
                    #                  "Url": [],
                    #                  "paperType": [],
                    #                  "Where": [],
                    #                  "Deadline": []
                    #                  }
                    #
                    # # part2 getting dates greater tan or less than particular date
                    # fromdate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')
                    #
                    # for things in Wiki_model:
                    #     count = 0
                    #     if extremes == "Lesserdates":
                    #         from_to_dates = Wiki_model.none()
                    #
                    #         if things.Deadline is not None:
                    #             if fromdate > things.Deadline:
                    #
                    #                 if things.Title == lesser_dates["Title"]:
                    #                     count += 1
                    #
                    #                 lesser_dates["Title"].append(things.Title)
                    #                 lesser_dates["Deadline"].append(things.Deadline)
                    #                 lesser_dates["Url"].append(things.Url)
                    #                 lesser_dates["Where"].append(things.Where)
                    #
                    #
                    #
                    #
                    #
                    #     elif extremes == "Greaterdates":
                    #         from_to_dates = Wiki_model.none()
                    #         # searchresult=Wiki_model
                    #         if things.Deadline is not None:
                    #             if fromdate < things.Deadline:
                    #                 greater_dates["Title"].append(things.Title)
                    #                 greater_dates["Deadline"].append(things.Deadline)
                    #                 greater_dates["Url"].append(things.Url)
                    #                 greater_dates["Where"].append(things.Where)

                    context = {
                        "from_to_dates": from_to_dates,  # important dont delete
                        "lesser_dates": lesser_dates,
                        "greater_dates": greater_dates,  # important dont delete

                    }
                    return render(request, 'Call_for_Papers_Search_Result.html', context)

                else:

                    contextwiki = dict()
                    contextwiki = Wiki_model.objects.all()
                    contextwiki = OrderFilter(request.GET, queryset=Wiki_model.objects.all())

                    context = {
                        'contextwiki': contextwiki,
                    }

                    return render(request, 'Call_for_Papers_Search_Result.html', context)



class Command(BaseCommand):
    help = "Release the spiders"
    process = CrawlerProcess(get_project_settings())
    process.crawl(SpiderBmbf)
    process.crawl(SpiderWiki)
    print("Process started")
    process.start()
    sleep(2)

    process.stop()
    print("process stopped")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login_url')
def Search_Call_for_Proposals(request):#used for searching with filter

            fromdate = request.GET.get('fromdate')
            todate = request.GET.get('todate')
            todelete = request.GET.get('todelete')
            extremes = request.GET.get('extremes')



            if  fromdate and todate :
                count=0
                Bmbf_all_items = Bmbf_model.objects.all()
                Bmbf_items = Bmbf_model.objects.values_list('Url').distinct()

                from_to_dates = Bmbf_model.objects.none()
                if extremes != "Lesserdates" and extremes != "Greaterdates":
                    from_to_dates = Bmbf_model.objects.raw(
                        'select id,Title,Dates,Url,Deadline from questions_bmbf_model where Deadline between "' + fromdate + '" and "' + todate + '" ')
                    lesser_dates = Bmbf_model.objects.none()
                    greater_dates = Bmbf_model.objects.none()
                elif extremes == "Lesserdates":
                    greater_dates=Bmbf_model.objects.none()
                    lesser_dates = Bmbf_model.objects.raw(
                    'select id,Title,Dates,Url,Deadline from questions_bmbf_model where (Deadline <= "' + fromdate + '"  ) ORDER BY Deadline')
                elif extremes == "Greaterdates":
                    lesser_dates=Bmbf_model.objects.none()
                    greater_dates = Bmbf_model.objects.raw(
                    'select id,Title,Dates,Url,Deadline from questions_bmbf_model where (Deadline >= "' + fromdate + '"  ) ORDER BY Deadline ')

                # python code to show lesser or greater dates
                Bmbfmodel = Bmbf_model.objects.all()
                # lesser_dates = {"Title": [],
                #           "Date": [],
                #           "Url": [],
                #           "paperType": [],
                #           "Where": [],
                #           "Deadline": []
                #           }
                # greater_dates = {"Title": [],
                #           "Date": [],
                #           "Url": [],
                #           "paperType": [],
                #           "Where": [],#changed12/20/2021
                #           "Deadline": []
                #           }
                #
                # todate = datetime.datetime.strptime(todate, '%Y-%m-%d')
                # fromdate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')
                #
                # for things in Bmbfmodel:
                #
                #    count = 0
                #    if extremes=="Lesserdates":
                #     from_to_dates=Bmbf_model.objects.none()
                #
                #     if things.Deadline is not None:
                #         if fromdate>things.Deadline:
                #
                #             if things.Title == lesser_dates["Title"]  :
                #                 count+=1
                #
                #
                #             lesser_dates["Title"].append(things.Title)
                #             lesser_dates["Deadline"].append(things.Deadline)
                #             lesser_dates["Url"].append(things.Url)
                #
                #    elif extremes=="Greaterdates":
                #         if things.Deadline is not None:
                #          if fromdate<things.Deadline:
                #
                #             greater_dates["Title"].append(things.Title)
                #             greater_dates["Deadline"].append(things.Deadline)
                #             greater_dates["Url"].append(things.Url)
                #

                context= {
                         "from_to_dates": from_to_dates,#important dont delete
                         "lesser_dates":lesser_dates,
                         "greater_dates":greater_dates,#important dont delete

                }
                return render(request, 'Call_for_Proposals_Search_Result.html', context)

            elif fromdate:
                from_to_dates = Bmbf_model.objects.none()
                if extremes != "Lesserdates" and extremes != "Greaterdates":
                    from_to_dates = Bmbf_model.objects.raw(
                        'select id,Title,Dates,Url,Deadline from questions_bmbf_model where Deadline between "' + fromdate + '" and "' + todate + '" ')
                    lesser_dates = Bmbf_model.objects.none()
                    greater_dates = Bmbf_model.objects.none()
                elif extremes == "Lesserdates":
                    greater_dates=Bmbf_model.objects.none()
                    lesser_dates = Bmbf_model.objects.raw(
                    'select id,Title,Dates,Url,Deadline from questions_bmbf_model where (Deadline <= "' + fromdate + '"  ) ORDER BY Deadline')
                elif extremes == "Greaterdates":
                    lesser_dates=Bmbf_model.objects.none()
                    greater_dates = Bmbf_model.objects.raw(
                    'select id,Title,Dates,Url,Deadline from questions_bmbf_model where (Deadline >= "' + fromdate + '"  ) ORDER BY Deadline ')
                # python code to show lesser or greater dates
                # count = 0
                # Bmbf_all_items = Bmbf_model.objects.all()
                # Bmbf_items = Bmbf_model.objects.values_list('Url').distinct()
                #
                # for x in Bmbf_items:
                #     non_repeated = ''.join(x)
                #
                #     count = 0
                #     for items in Bmbf_all_items:
                #
                #         j = str(items.Url)
                #
                #         if non_repeated == j:
                #             count += 1
                #             # print("count",count)
                #             if (count == 1):
                #                 pass
                #                 # print("f",non_repeated)
                #                 # print("kjh", items.Url,items.id)
                #             elif (count > 1):
                #                 # print("count", count)
                #                 # print("f", non_repeated)
                #                 # print("kjh", items.Url, items.id)
                #                 id = items.id
                #                 item_delete = Bmbf_model.objects.get(id=id)
                #                 # print("idd",item_delete)
                #                 # item_delete.delete() # https://www.oreilly.com/library/view/django-essentials/9781783983704/ch06s06.html
                #
                # from_to_dates = Bmbf_model.objects.raw(
                #     'select id,Title,Dates,Url,Deadline from questions_bmbf_model where Deadline >= "' + fromdate + '" ')
                #
                # Bmbfmodel = Bmbf_model.objects.all()
                # lesser_dates = {"Title": [],
                #                 "Date": [],
                #                 "Url": [],
                #                 "paperType": [],
                #                 "Where": [],
                #                 "Deadline": []
                #                 }
                # greater_dates = {"Title": [],
                #                  "Date": [],
                #                  "Url": [],
                #                  "paperType": [],
                #                  "Where": [],  # changed12/20/2021
                #                  "Deadline": []
                #                  }
                #
                #
                # fromdate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')
                #
                # for things in Bmbfmodel:
                #
                #     count = 0
                #     if extremes == "Lesserdates":
                #         from_to_dates = Bmbf_model.objects.none()
                #
                #         if things.Deadline is not None:
                #             if fromdate > things.Deadline:
                #
                #                 if things.Title == lesser_dates["Title"]:
                #                     count += 1
                #
                #                 lesser_dates["Title"].append(things.Title)
                #                 lesser_dates["Deadline"].append(things.Deadline)
                #                 lesser_dates["Url"].append(things.Url)
                #
                #     elif extremes == "Greaterdates":
                #         if things.Deadline is not None:
                #             if fromdate < things.Deadline:
                #                 greater_dates["Title"].append(things.Title)
                #                 greater_dates["Deadline"].append(things.Deadline)
                #                 greater_dates["Url"].append(things.Url)
                #
                # from1_to_dates = Bmbf_model.objects.raw(
                #     'select id,Title,Dates,Url,Deadline from questions_bmbf_model where Deadline >= "' + fromdate + '" ')

                context = {
                    "from_to_dates": from_to_dates,  # important dont delete
                    "lesser_dates": lesser_dates,
                    "greater_dates": greater_dates,
                    #"from1_to_dates":from1_to_dates,# important dont delete

                }
                return render(request, 'Call_for_Proposals_Search_Result.html', context)

            else:

                    bmbf_values = dict()
                    bmbf_values = Bmbf_model.objects.all()
                    bmbf_values = OrderFilter1(request.GET, queryset=Bmbf_model.objects.all())


                    context = {
                        'bmbf_values': bmbf_values,
                    }
                    return render(request, 'Call_for_Proposals_Search_Result.html', context)



#blgbclfufh#wqujlailqc
#jmqklquczr
























































































































































































































































#uaadzgqchc





































#gsgovjkkav


















































































































































































#eadbsqzdho











#fvnuqvzjzc














































#pnahuvqidz












































#cuvbdsduyr























































































































































#Should not be removed to change the comments to restart the server

