from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
#改良简单版
from django.views import generic
from .models import Question, Choice
from django.utils import timezone
# from django.http import Http404
#以下这是使用HttpResponse方式返回
# from django.http import HttpResponse
# from django.template import RequestContext,loader
# Create your views here.

#---------通过Django generic改进版
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
                'question': p,
                'error_message': 'you did not select a choice.',
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))



#-------------原生版
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#     #------------------
#     # template = loader.get_template('polls/index.html')
#     # context = RequestContext(request, {
#     #     'latest_question_list': latest_question_list,
#     # })
#     # return HttpResponse(template.render(context))
#     #--------------
#     # output = ', '.join([p.question_text for p in latest_question_list])
#     # return HttpResponse(output)
#     #--------------
#     # return HttpResponse("Hello, world. You're at the polls index.")
#
# def detail(request,question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     #-----------------------
#     # try:
#     #     question = Question.objects.get(pk = question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist')
#     # return render(request, 'polls/detail.html', {'question': question})
#     #-----------------------
#     # return HttpResponse('you are looking at question %s.' % question_id)
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     #---------------------
#     # results_response = 'you are looking at the results of question %s.' % question_id
#     # return render(request,results_response)
#     #---------------------
#     # response = 'you are looking at the results of question %s.'
#     # return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     p = get_object_or_404(Question, pk = question_id)
#     try:
#         selected_choice = p.choice_set.get(pk = request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': p,
#             'error_message': 'you did not select a choice.',
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    #--------------------
    # vote_result = 'you are voting on question %s.' % question_id
    # return render(request, vote_result)
    #-------------------
    # return HttpResponse('you are voting on question %s.' % question_id)

# from django.core.mail import send_mail
# from  mysite.settings import *
#
# @shared_task
# def levemessage(message):
#     email_title = 'django邮件测试'
#     email_body = 'django邮件测试django邮件测试django邮件测试django邮件测试django邮件测试django邮件测试django邮件测试'
#     email = 'xubojoy1112@163.com'  # 对方的邮箱
#     send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
#     print('mail sent')