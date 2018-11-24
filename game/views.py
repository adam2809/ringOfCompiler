from django.shortcuts import render
from game.models import Task
from random import choice

from game.models import Task, Test

def homePage(request):
    return render(request,'index.htm')

taskIDsNotVisited = []
def gamePage(request):
    # if request == 'POST':
    #     # TODO code to test user input against test suite and
    #     # return approperiate response
    #     pass
    # taskCount = Task.objects.count()
    # taskIDsNotVisited = range(1,taskCount+1)
    #
    # chosenTaskID = choice(taskIDsNotVisited)
    # taskToServe = Task.objects.get(chosenTaskID)
    # taskIDsNotVisited.remove()
    # taskDescription = (f'{taskToServe.problemDesciption}\n\nINPUT:\n{taskToServe.inputDesription}\n\nOUTPUT:\n{taskToServe.outputDescription}')
    return render(request,'game.html')
