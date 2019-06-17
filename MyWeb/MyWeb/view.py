from django.shortcuts import render
from TestModel.models import Test
 
def User_Information(request):
    context          = {}
    context['sname'] = '李钻'
    context['sno'] = '16219111329'
    context['sclass'] = '16计算机科学与技术三'
    return render(request, 'User.html', context)

def index(request):
    return render(request, 'index.html', locals())