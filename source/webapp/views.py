from django.shortcuts import render


def index_view(request):
    print(request.GET.getlist('author'))
    return render(request, 'calc.html')


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        print(request.POST)
        context = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author')
        }
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
