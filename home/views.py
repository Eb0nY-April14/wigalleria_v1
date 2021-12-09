from django.shortcuts import render

# Create your views here. The index.html/index view are 
# same as store.html/store view used in the Django 
# tutorial on YouTube
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
