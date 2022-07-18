from django.shortcuts import render

def read_f(my_file):
    with my_file as f:
        return [(word if isinstance(word, str) else word.decode()) for line in f for word in line.split() if word.isalpha()]  # составление списка слов из файла

def home(request):
    tmp_list = []
    if request.method == 'POST':
        tmp_list = read_f(request.FILES['file'])
        with open("mydata.txt", "a") as myfile:
            myfile.write(' '.join(tmp_list))
        tmp_list = read_f(open("mydata.txt", "r"))
    else:
        tmp_list = read_f(open("mydata.txt", "r"))
    return render(request, 'home.html', {'my_list': tmp_list, 'word': ''})

def clean_data(request):
    open('mydata.txt', 'w').close()
    tmp_list = []
    return render(request, 'home.html', {'my_list': tmp_list, 'word': ''})

def find_word(request):
    tmp_list = read_f(open("mydata.txt", "r"))
    if request.method == 'POST':
        word = request.POST.get('text1')
        word_text = f'Слово {word} встречается в загруженных файлах {tmp_list.count(word)} раз(а).'
    return render(request, 'home.html', {'my_list': tmp_list, 'word': word_text})