from . import views
from django.urls import path


app_name = 'drive'

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.Login,name="login"),
    path('logout/',views.Logout,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('folder/<int:folderid>/',views.folder,name="folder"),
    path('delete/folder/<int:folderid>/',views.deleteFolder,name="delete-folder"),
    path('delete/file/<int:fileid>/',views.deleteFile,name="delete-file"),
    path('addFolder/',views.addFolder,name="addFolder"),
   
]
