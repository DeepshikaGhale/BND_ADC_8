
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Harmonyapp.models import Lyrics
import json

@csrf_exempt
def view_get_post_lyrics(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        lyrics = Lyrics.objects.all()
        print("QuerySet objects => ",lyrics)
        list_of_lyrics = list(lyrics.values("UserName","SongName","Lyric"))
        print("List of lyrics objects => ",list_of_lyrics)
        dictionary_name = {
        "lyrics":list_of_lyrics
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['UserName'])
        print(python_dictionary_object['SongName'])
        print(python_dictionary_object['Lyric'])
        Lyrics.objects.create(UserName=python_dictionary_object['UserName'],
        SongName=python_dictionary_object['SongName'],
        Lyric=python_dictionary_object['Lyric'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        lyrics = Lyrics.objects.get(id = ID)
        print(type(lyrics.UserName))
        return JsonResponse({
            "UserName":lyrics.UserName,
            "SongName":lyrics.SongName,
            "Lyric":lyrics.Lyric
        })
    elif request.method == "PUT":
        print("What's the request =>",request.method)
        lyrics = Lyrics.objects.get(id=ID)
        print(type(lyrics.UserName))
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))

        lyrics.UserName = python_dictionary_object['UserName']
        lyrics.SongName = python_dictionary_object['SongName']
        lyrics.Lyric = python_dictionary_object['Lyric']
        lyrics.save()
        
        return JsonResponse({
            "Message":"Updated successfully"
        })
    elif request.method == "DELETE":
        lyrics=Lyrics.objects.get(id=ID)
        lyrics.delete()
        return JsonResponse({
          "message": "Deleted Successfully"
        })
        
    else:
        return JsonResponse({
        "message":" Other http verbs Testing"
        })

