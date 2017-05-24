from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.
from .forms import AddForm

def year_archive(request,year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year,'article_list': a_list}
    return render(request,'news/year_archive.html',context)

def index(request):
    if request.method == 'POST':
        # 当表单以 POST 方式提交的时候
        form = AddForm(request.POST)
        if form.is_valid():
            # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        # 正常方位时
        form = AddForm()

    return render(request, 'index.html', {'form': form})
