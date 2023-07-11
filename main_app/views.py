from django.shortcuts import render
from .models import Finch
# finches = [
#     {'name': 'Blue', 'gender': 'male',
#         'species': 'Gouldian finch', 'age': 2},
#     {'name': 'Sachi', 'gender': 'female',
#         'species': 'House Finch', 'age': 2},
# ]

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    finches = Finch.objects.all()
    # We pass data to a template very much like we did in Express!
    return render(request, 'finches/index.html', {
        'finches': finches
    })


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})
