from django.shortcuts import render,redirect
from .models import Users




def index(request):
    
    
    return render(request, 'index.html')

def download_image(request):
    users = Users.objects.all()
    return render(request, 'image.html' , {'users': users})

def uploadImage(request):
    print("Request Handling...")
    p = request.FILES['image']
    from .models import Users
    user = Users(pic =p)
    user.save()
    return redirect(index)

 