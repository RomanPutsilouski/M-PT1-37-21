# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse('Привет первый проект')
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Art
from django.urls import reverse

def index(request):
    latest_art_s = Art.objects.order_by('-art_date_pub')[:5]
    return render(request, 'art_s/list.html', {'latest_art_s':  latest_art_s})


def detail(request, Art_id):
    try:
        a = Art.objects.get(id=Art_id)
    except:
        raise Http404("НЕТ СТАТЬИ")
    l_c_l = a.comment_set.order_by('-id')[:10]
    return render(request, 'art_s/detail.html', {"Art": a, 'l_c_l': l_c_l})



def l_c(request, Art_id):
    try:
        a = Art.objects.get(id=Art_id)
    except:
        raise Http404("НЕТ СТАТЬИ")
    a.comment_set.create(сom_autor=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('art_s:detail', args=a.id, ))
