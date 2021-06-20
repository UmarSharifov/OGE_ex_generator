from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .utils import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


def task1(request):
    task1 = ex1(1)
    sentence = task1.sentence
    word = task1.word
    size_of_word = task1.size_of_word
    ctx = {
        'sentence': sentence,
        'word': word,
        'size_of_word': size_of_word,
    }
    return render(request, 'task1.html', context=ctx)

def task2(request):
    task2 = ex2(1)
    ctx = {
        'code': task2.code,
        'task2_word': task2.word,
        'task2_char_dict': task2.char_dict,
    }
    return render(request, 'task2.html', context=ctx)

def task3(request):
    task3 = ex3(1)
    ctx ={
        'task_string': task3.EX_TEXT,
        'task_answer': task3.ANSWER,
        'min_or_max': task3.MIN_OR_MAX,
    }
    return render(request, 'task3.html', context=ctx)

def task4(request):
    task4 = ex4(1)
    ctx = {
        'task_graph': task4.graph,
        'task_answer': task4.answer,
    }
    return render(request, 'task4.html', context=ctx)


def task5(request):
    task5 = ex5(1)
    flag = False
    while(flag != True):
        task5 = ex5(1)
        if clean_ex5(task5):
            flag = True

    ctx = {
        'question1': task5.question1,
        'question2': task5.question2,
        'number': task5.number,
        'algoritm': task5.algoritm,
        'answer': task5.answer,
        'open_type':task5.type1,
        'close_type': task5.type2,
        'number_open_type': task5.number_open_type,
        'number_close_type': task5.number_close_type,
    }
    return render(request, 'task5.html', context=ctx)

def task6(request):
    task6 = ex6(1)
    ctx = {
        'task6': task6,
        'alg_lang': task6.alg,
        'pascal_lang': task6.pascel,
        'pairs': task6.pairs,
        'sum': task6.sum,
    }
    return render(request, 'task6.html', context=ctx)

def task7(request):
    task7 = ex7()
    ctx = {
        'option':task7.sentence_list,
        'combination':task7.combination,
    }
    return render(request, 'task7.html', context=ctx)

def task8(request):
    task8 = ex8(1)
    ctx = {
    'numbers':task8.list_of_numbers,
    'types': task8.list_of_types,
    'answer': task8.answer,
    'answer_type': task8.type,
    }
    return render(request, 'task8.html', context=ctx)

def task10(request):
    task10 = ex10(1)
    answer = task10.max_number
    ctx = {
        'hex': convert_base(task10.first_number, 16,10),
        'oct': convert_base(task10.second_number, 8, 10),
        'bin': convert_base(task10.third_number, 2, 10),
        'answer': answer,
    }
    return render(request, 'task10.html', context=ctx)


def constructor_options(request):
    return render(request, 'constructor_options.html')

def constructor(request):
    question_numbers = request.GET.getlist('question_number')
    lvl = request.GET.get('lvl')
    quantity = request.GET.get('quantity')
    options_list = list()
    for i in range(0, int(quantity)):
        temp = all_ex(question_numbers,int(lvl))
        options_list.append(temp)

    return render(request, 'constructor.html', context={
        'options': options_list,
        'lvl':lvl,
    })


def constructor_options_for_pass(request):
    if request.user.is_authenticated:
        return render(request, 'constructor_options_for_pass.html')
    else:
        return redirect('index')

def passing(request):
    if request.user.is_authenticated:
        question_numbers = request.GET.getlist('question_number')
        lvl = request.GET.get('lvl')
        quantity = request.GET.get('quantity')
        options_list = list()
        for i in range(0, int(quantity)):
            temp = all_ex(question_numbers, int(lvl))
            options_list.append(temp)
        answers = list()
        question_type = list()
        for i in range(0, int(quantity)):
            for i in options_list:
                if i.ex1_:
                    answers.append(str(i.ex1_.word))
                    question_type.append('1')
                if i.ex2_:
                    answers.append(i.ex2_.word)
                    question_type.append('2')
                if i.ex3_:
                    answers.append(i.ex3_.ANSWER)
                    question_type.append('3')
                if i.ex4_:
                    answers.append(i.ex4_.answer)
                    question_type.append('4')
                if i.ex5_:
                    answers.append(i.ex5_.answer)
                    question_type.append('5')
                if i.ex6_:
                    answers.append(i.ex6_.sum)
                    question_type.append('6')
                if i.ex7_:
                    answers.append(i.ex7_.combination)
                    question_type.append('7')
                if i.ex8_:
                    answers.append(i.ex8_.answer)
                    question_type.append('8')
                if i.ex10_:
                    answers.append(i.ex10_.max_number)
                    question_type.append('10')
        return render(request, 'passing.html', context={
            'options': options_list,
            'lvl': lvl,
            'answers': answers,
            'question_type': question_type,
        })
    else:
        return redirect('index')

def History_results(request):
    results_history = Results.objects.filter(Owner=request.user)
    return render(request, 'history_of_results.html', context={
        'history': results_history,
    })


def results(request):
    if request.method == 'POST':
        user_answers = request.POST.getlist('ans')
        correct_answers = request.POST.getlist('answers')
        question_type = request.POST.getlist('question_type')
        lvl = request.POST.getlist('level_for')
        question_type = set(question_type)

        points = 0
        counter = 0
        table_list = list()
        for i in user_answers:
            temp = ""
            if str(user_answers[counter]) == str(correct_answers[counter]):
                points = points + 1
                temp += '<tr class="table-success">'
                temp += '<td> {0} </td> <td>{1}</td> <td>{2}</td>'.format(counter + 1, str(user_answers[counter]), str(correct_answers[counter]))
            else:
                temp += '<tr class="table-danger">'
                temp += '<td> {0} </td> <td>{1}</td> <td>{2}</td>'.format(counter + 1, str(user_answers[counter]), str(correct_answers[counter]))
            table_list.append(temp)
            counter = counter + 1
        current_result = Results(Owner=request.user, Correct_answers=points, Answers_quantity=counter, Lvl=int(lvl[0]))
        current_result.save()
        ctx = {
            'points': points,
            'quantity': counter,
            'table_list': table_list,
            'question_type': question_type,
            'lvl': lvl,
        }
        return render(request, 'results.html', context=ctx)