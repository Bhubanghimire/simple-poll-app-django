from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Question
from django.template import loader

# Create your views here.
def index(request):
    output = Question.objects.order_by('pub_date')
    # output = ', '.join([q.question_text for q in output])
    template = loader.get_template('index.html')
    context = {
        'latest_question_list':output,
    }
    return render(request,'index.html',context)



def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise http404("question not found")
    


    #this is the eqivalent of above

    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question':question
    }

    return render(request,'detail.html',context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

