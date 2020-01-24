from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseForbidden
from django.template import Template,Context
from .models import *
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def view_Lyrics_page(request):
    return render(request,'Lyrics.html')

def view_Lyrics_lists(request):
    list_of_lyrics= Lyrics.objects.all()
    print(list_of_lyrics)
    context_variable = {
        'lyrics':list_of_lyrics
    }
    return render(request,'Lyrics.html',context_variable)

def view_Lyrics_form(request):
    return render(request,'Lyricsform.html')

def view_Lyricsdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_UserName = request.POST['Lyrics_UserName']
        print(type(get_UserName))
        get_SongName = request.POST['Lyrics_SongName']
        get_Lyric = request.POST['Lyrics_Lyric']
        print(type(get_UserName))
        Lyrics_obj = Lyrics(UserName=get_UserName,SongName=get_SongName,Lyric=get_Lyric)
        Lyrics_obj.save()
        return HttpResponse("Saved")
        #return redirect('Harmonyapp/Lyricsdata')
    else:
        return HttpResponse("Error record saving")

def view_Lyricsdata_updateform(request,ID):
    print(ID)
    Lyrics_obj = Lyrics.objects.get(id=ID)
    print(Lyrics_obj)
    context_varible = {
        'lyrics':Lyrics_obj
    }
    return render(request,'LyricsUpdateForm.html',context_varible)

def view_update_form_data_in_db(request,ID):
    Lyrics_obj = Lyrics.objects.get(id=ID)
    print(Lyrics_obj)
    Lyrics_form_data = request.POST
    print(Lyrics_form_data)
    Lyrics_obj.UserName = request.POST['Lyrics_UserName']
    Lyrics_obj.SongName =request.POST['Lyrics_SongName']
    Lyrics_obj.Lyric = request.POST['Lyrics_Lyric']
    
    return HttpResponse("Record Is Succesfully Updated!")     

def view_register_user(request):
    if request.method =="GET":
        return render(request,'register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_Username'],password=request.POST['input_Password'],email=request.POST['input_Email'])
        user.save()
        return HttpResponse("Signup Successful")


def view_login_user(request):
    if request.method =="GET":
        return render (request,'login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_Username'],password=request.POST['input_Password'])
        print(user)
        if user is not None:
            login(request,user)
            return render(request,"page.html")
        else:
            return redirect("login") 

def view_logout(request):
    if (not request.user.is_authenticated):
        return HttpResponseForbidden('Please LogIn for Logging out!')
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'home.html')


