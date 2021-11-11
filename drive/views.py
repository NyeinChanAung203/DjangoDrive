from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import MyUserCreationForm
from .models import Folder,File
from django.urls import reverse
# Create your views here.

@login_required
def index(request):
    folders = Folder.objects.filter(folderuser=request.user)
    context = {
        'folders':folders
    }
    return render(request,'drive/index.html',context)

@login_required
def folder(request,folderid=1):
    
    folder = get_object_or_404(Folder,id=folderid)
    files = File.objects.filter(folder=folder)
    if request.method == 'POST':
        file = request.FILES.get('uploadfile')
        filename = request.POST.get('filename')
        if file and filename:
            File.objects.create(filename=filename,file=file,folder=folder)
            return redirect(reverse('drive:folder',kwargs={'folderid':folderid}))
    context = {
        'folder':folder,
        'files':files
    }
    return render(request,'drive/folder.html',context)


@login_required
def deleteFolder(request,folderid):
    folder = get_object_or_404(Folder,id=folderid)
    folder.delete()
    messages.success(request,'Deleted successfully')
    return redirect('drive:index')

@login_required
def deleteFile(request,fileid):
    file = get_object_or_404(File,id=fileid)
    if request.user == file.folder.folderuser:
        print(file.folder.foldername,file.folder.folderuser)
        file.delete()
        messages.success(request,'Deleted successfully')
        return redirect(reverse('drive:folder',kwargs={'folderid':file.folder.id}))
    else:
        print('worng user')
    # messages.success(request,'Deleted successfully')
    return redirect('drive:index')

@login_required
def addFolder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('addfolder')
        description = request.POST.get('description')
        folder = Folder.objects.create(foldername=folder_name,folderuser=request.user,description=description)
        if folder:
            return redirect('drive:index')
        else:
            messages.warning(request,'Folder is not created!')
            return redirect('drive:index')

def signup(request):
    if not request.user.is_authenticated:
        form = MyUserCreationForm()
        if request.method == 'POST':
            form = MyUserCreationForm(request.POST)  
            if form.is_valid():
                form.save()
                messages.success(request,'User Account Created')
                return redirect('drive:login')
            else:
                messages.warning(request,'Invalid Singup Try Again!!!')
    else:
        return redirect('drive:index')
    context = {'form':form}
    return render(request,'drive/signup.html',context)


def Login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('drive:index')
                else:
                    messages.warning(request,'Username or Password is incorrect')
    else:
        return redirect('drive:index')
    context = {}
    return render(request,'drive/login.html',context)

def Logout(request):
    logout(request)
    return redirect('drive:login')