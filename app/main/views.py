from django.shortcuts import render

from main.models import Hakaton, Hakaton2


# Create your views here.
def index(request):
    hakatons = Hakaton.objects.all().order_by('start_date')[:3]
    context = {
        'hakatons': hakatons,

    }
    return render(request, 'main/index.html', context)

# hakatons = Hakaton.objects.all().order_by('start_date')

def hakatons(request):
    hakatons2 = Hakaton2.objects.all().order_by('start_date')[:3]
    context = {
        'hakatons2': hakatons2,

    }
    return render(request, 'main/FurureHacatons.html', context)


def about_hackathon(request):
    hakatons = Hakaton.objects.all().order_by('start_date')
    context = {
        'hakatons': hakatons,

    }
    return render(request, 'main/HatatonPage.html')

def about(request):

    return render(request, 'main/abaout.html')