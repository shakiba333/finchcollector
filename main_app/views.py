from django.shortcuts import render

finches = [
    {'name': 'Blue', 'gender': 'male',
        'species': 'Gouldian finch', 'age': 2},
    {'name': 'Sachi', 'gender': 'female',
        'species': 'House Finch', 'age': 2},
]

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finch_index(request):
    # We pass data to a template very much like we did in Express!
    return render(request, 'finches/index.html', {
        'finches': finches
    })
