from django.shortcuts import render
from webapp.models import Article, STATUS_CHOICES


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Article.objects.all()
    else:
        data = Article.objects.filter(status='moderated')
    return render(request, 'index.html', context={
        'articles': data,
    })


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')
        status = request.POST.get('status')
        article = Article.objects.create(title=title, text=text, author=author, status=status)
        context = {'article': article}
        return render(request, 'article_view.html', context)


def calc_view(request):
    if request.method == 'GET':
        return render(request, 'calc.html')
    elif request.method == 'POST':
        print(request.POST)

        first_num = request.POST['FirstNumber']
        second_num = request.POST['SecondNumber']
        sign = request.POST['calc']

        result = 0
        if sign == '+':
            result = int(first_num) + int(second_num)
        elif sign == '-':
            result = int(first_num) - int(second_num)
        elif sign == '*':
            result = int(first_num) * int(second_num)
        elif sign == '/':
            result = int(first_num) / int(second_num)

        context = {
            'first': first_num,
            'second': second_num,
            'result': result,
            'sign': sign,
            'eq': '='
        }

        return render(request, 'calc.html', context)
