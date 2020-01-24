from django.shortcuts import render
from .  models import Lyrics 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
 
 #create yours views here.
def search(request):
    if request.method == "POST":
        music = request.POST['srh']

        if music:
            match = Lyrics.objects.filter(SongName__istartswith=music)
                                          
            if match:
                return render(request, 'Search.html', {'sr':match})

            else:
                return HttpResponse('<H1> No result found</H1>')

        else:
            return HttpResponse('<H1>Type the Song Name</H1>')

    else:
        return render(request,'Search.html')


