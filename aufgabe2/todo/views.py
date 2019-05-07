from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('todo/index2.html')
    # context = {'latest_question_list': latest_question_list}
    context = {}
    return HttpResponse(template.render(context, request))