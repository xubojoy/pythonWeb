from django.shortcuts import render, get_object_or_404
from .models import Question
# from django.http import Http404
#以下这是使用HttpResponse方式返回
# from django.http import HttpResponse
# from django.template import RequestContext,loader
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    #------------------
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    # return HttpResponse(template.render(context))
    #--------------
    # output = ', '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(output)
    #--------------
    # return HttpResponse("Hello, world. You're at the polls index.")

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    #-----------------------
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    # return render(request, 'polls/detail.html', {'question': question})
    #-----------------------
    # return HttpResponse('you are looking at question %s.' % question_id)

def results(request, question_id):
    results_response = 'you are looking at the results of question %s.' % question_id
    return render(request,results_response)
    # response = 'you are looking at the results of question %s.'
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    vote_result = 'you are voting on question %s.' % question_id
    return render(request, vote_result)
    # return HttpResponse('you are voting on question %s.' % question_id)