from django.shortcuts import render
from webapp.models import Article


def index_view(request):
    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data,
    })


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, text=text, author=author)
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
