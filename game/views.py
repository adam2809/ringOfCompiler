from django.shortcuts import render
from game.models import Task
from random import randint

from game.models import Task, Test

from frameworkTest import test as testCode

#TODO these are debug messages change them for something fun at the end
consequenceMsgs = {0:'No consequences! The ouput was correct.',
                   1:'Wrong output! Consequence 1',
                   2:'Error! Consequence 2',
                   }

def homePage(request):
    return render(request,'index.htm')


def gamePage(request):
    if request.method == 'POST':
        userCode = request.POST['codemirror-textarea']
        tests = Test.objects.filter(task=request.session['currTaskID'])
        taskToServe = Task.objects.get(pk=request.session['currTaskID'])
        taskDescription = (f'INPUT:\n{taskToServe.inputDesription}\n\nOUTPUT:\n{taskToServe.outputDescription}')
        for test in tests:
            testReturn = testCode(userCode,test.input,test.output)
            if testReturn:
                # return response filled with old code consequenceMsgs[1] and
                # message that output was wrong
                return render(request,'game.html',{'taskName':taskToServe.problemName,'taskDescription':taskToServe.problemDesciption,'taskIO':taskDescription,'consequence':consequenceMsgs[testReturn],'code':userCode})
        # return response with blank code consequenceMsgs[0] update request.session['currTaskID']
        chosenTaskID = randint(1,Task.objects.count())
        request.session['currTaskID']=chosenTaskID
        taskToServe = Task.objects.get(pk=chosenTaskID)
        taskDescription = (f'INPUT:\n{taskToServe.inputDesription}\n\nOUTPUT:\n{taskToServe.outputDescription}')
        return render(request,'game.html',{'taskName':taskToServe.problemName,'taskDescription':taskToServe.problemDesciption,'taskIO':taskDescription,'consequence':consequenceMsgs[0],'code':''})

    taskCount = Task.objects.count()

    chosenTaskID = randint(1,taskCount)
    request.session['currTaskID']=chosenTaskID

    taskToServe = Task.objects.get(pk=chosenTaskID)
    taskDescription = (f'INPUT:\n{taskToServe.inputDesription}\n\nOUTPUT:\n{taskToServe.outputDescription}')
    return render(request,'game.html',{'taskName':taskToServe.problemName,'taskDescription':taskToServe.problemDesciption,'taskIO':taskDescription,'consequence':''})
