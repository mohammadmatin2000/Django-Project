from django.shortcuts import render

def index(request):
    context = {'title': 'Django | Project','name':'MATIN','job':'Django Backend Developer','about':"""it's matin.
I'm a Professional technical fields learner. I'm sixteen And I have been working in this field for two years. 
And for now, I'm working on Django."""}
    return render(request, 'blog/index.html', context)
