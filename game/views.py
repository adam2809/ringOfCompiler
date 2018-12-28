from django.shortcuts import render, redirect

from random import choice

from game.models import Task, Test

from game.testingSystem.testingSystem import ProgramTest

#TODO these are debug messages change them for something fun at the end
consequenceMsgs = {0:'No consequences! The ouput was correct.',
                   1:'Wrong output! Consequence 1',
                   2:'Error! Consequence 2',
                   }


def homePage(request):
    taskCount = Task.objects.count()
    request.session['taskIDsNotChosen'] = list(range(1, taskCount + 1))
    request.session['currTemplateDict'] = {}
    request.session['currTemplateDict']['consequence'] = ''
    return render(request,'index.htm')


def testCode(request):
    userCode = request.POST['codemirror-textarea']
    tests = Test.objects.filter(task=request.session['currTemplateDict']['currTaskID'])
    outputText = ''
    for i, test in enumerate(tests):
        progTest = ProgramTest(userCode,test.input,test.output)
        outputText += \
        f'''TEST {i} output:
        {progTest.run()}
        For input:
        {test.input}\n\n'''
        testReturn = progTest.test()
        if testReturn:
            request.session['currTemplateDict']['output'] = outputText
            request.session['currTemplateDict']['code'] = userCode
            request.session['currTemplateDict']['consequence'] = \
                                                     consequenceMsgs[testReturn]
            return redirect('/retry')
        return redirect('/new')


def newTask(request):
    chosenTaskID = choice(request.session['taskIDsNotChosen'])
    taskToServe = Task.objects.get(pk=chosenTaskID)
    request.session['taskIDsNotChosen'].remove(chosenTaskID)
    request.session['currTemplateDict']['currTaskID'] = chosenTaskID
    IODescription = (f'INPUT:\n{taskToServe.inputDesription}\n\n \
                       OUTPUT:\n{taskToServe.outputDescription}')
    request.session['currTemplateDict']['taskName'] = taskToServe.problemName
    request.session['currTemplateDict']['taskDescription'] = \
                                                   taskToServe.problemDesciption
    request.session['currTemplateDict']['taskIO'] = IODescription
    request.session['currTemplateDict']['code'] = ''
    request.session['currTemplateDict']['consequence'] = consequenceMsgs[0] \
                   if request.session['currTemplateDict']['consequence'] else ''
    request.session['currTemplateDict']['output'] = ''

    print(request.session['currTemplateDict'])

    return render(request,'game.html',request.session['currTemplateDict'])


def retryTask(request):
    return render(request,'game.html',request.session['currTemplateDict'])
