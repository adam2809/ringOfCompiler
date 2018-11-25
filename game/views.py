from django.shortcuts import render
from game.models import Task
from random import choice

from game.models import Task, Test

from frameworkTest import test as testCode

consequenceMsgs = {0:'No consequences! The ouput was correct.',
                   1:'Error! Consequence 1',
                   2:'Wrong output! Consequence 2',
                   }

def homePage(request):
    return render(request,'index.htm')

taskIDsNotVisited = []
def gamePage(request):
    if request.method == 'POST':
        userCode = request.POST['codemirror-textarea']
        tests = Test.objects.filter(task=request.session['currTaskID'])
        for test in tests:
            testReturn = testCode(userCode,test.input,test.output)
            if testReturn == 1:
                # return response filled with old code consequenceMsgs[1] and
                # message that output was wrong
                taskToServe = Task.objects.get(pk=request.session['currTaskID'])
                taskDescription = (f'INPUT:\n{taskToServe.inputDesription}\n\nOUTPUT:\n{taskToServe.outputDescription}')
                return render(request,'game.html',{'taskName':taskToServe.problemName,'taskDescription':taskToServe.problemDesciption,'taskIO':taskDescription,'consequence':consequenceMsgs[1]})
            if testReturn == 2:
                # return response filled with old code consequenceMsgs[2] and
                # the error message
                taskToServe = Task.objects.get(pk=request.session['currTaskID'])
                taskDescription = (f'INPUT:\n{taskToServe.inputDesription}\n\nOUTPUT:\n{taskToServe.outputDescription}')
                return render(request,'game.html',{'taskName':taskToServe.problemName,'taskDescription':taskToServe.problemDesciption,'taskIO':taskDescription,'consequence':consequenceMsgs[2]})
        # return response with blank code consequenceMsgs[0] update request.session['currTaskID']
        chosenTaskID = choice(taskIDsNotVisited)
        request.session['currTaskID']=chosenTaskID
        taskIDsNotVisited.remove(chosenTaskID)
        taskToServe = Task.objects.get(pk=chosenTaskID)
        taskDescription = (f'INPUT:\n{taskToServe.inputDesription}\n\nOUTPUT:\n{taskToServe.outputDescription}')
        return render(request,'game.html',{'taskName':taskToServe.problemName,'taskDescription':taskToServe.problemDesciption,'taskIO':taskDescription,'consequence':consequenceMsgs[0]})

    taskCount = Task.objects.count()
    taskIDsNotVisited = list(range(1,taskCount+1))

    chosenTaskID = choice(taskIDsNotVisited)
    request.session['currTaskID']=chosenTaskID
    taskIDsNotVisited.remove(chosenTaskID)

    taskToServe = Task.objects.get(pk=chosenTaskID)
    taskDescription = (f'INPUT:\n{taskToServe.inputDesription}\n\nOUTPUT:\n{taskToServe.outputDescription}')
    return render(request,'game.html',{'taskName':taskToServe.problemName,'taskDescription':taskToServe.problemDesciption,'taskIO':taskDescription,'consequence':''})
