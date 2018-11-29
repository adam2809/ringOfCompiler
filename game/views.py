from django.shortcuts import render

from random import choice

from game.models import Task, Test

from game.testingSystem.testingSystem import ProgramTest

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
        outputText = ''
        for i, test in enumerate(tests):
            progTest = ProgramTest(userCode,test.input,test.output)
            outputText += \
            f'''TEST {i} output:
            {progTest.run()}
            For input:
            {test.input}\n\n'''
            testReturn = test.test()
            if testReturn:
                request.session['currTemplateDict']['output'] = outputText
                request.session['currTemplateDict']['code'] = userCode
                request.session['currTemplateDict']['consequence'] = \
                                                    consequenceMsgs[testReturn]
                return render(request,'game.html', \
                                            request.session['currTemplateDict'])
        #TODO rapair code repetition
        chosenTaskID = choice(request.session['taskIDsNotChosen'])
        taskToServe = Task.objects.get(pk=chosenTaskID)
        request.session['taskIDsNotChosen'].remove(chosenTaskID)

        IODescription = (f'INPUT:\n{taskToServe.inputDesription}\n\n \
                           OUTPUT:\n{taskToServe.outputDescription}')
        request.session['currTemplateDict']['taskName'] = \
                                                         taskToServe.problemName
        request.session['currTemplateDict']['taskDescription'] = \
                                                   taskToServe.problemDesciption
        request.session['currTemplateDict']['taskIO'] = IODescription
        request.session['currTemplateDict']['code'] = ''
        request.session['currTemplateDict']['consequence'] = consequenceMsgs[0]
        request.session['currTemplateDict']['output'] = outputText
        return render(request,'game.html',request.session['currTemplateDict'])

    taskCount = Task.objects.count()
    request.session['taskIDsNotChosen'] = list(range(1, taskCount + 1))
    chosenTaskID = choice(request.session['taskIDsNotChosen'])
    request.session['currTaskID'] = chosenTaskID
    request.session['taskIDsNotChosen'].remove(chosenTaskID)

    taskToServe = Task.objects.get(pk=chosenTaskID)
    IODescription = (f'INPUT:\n{taskToServe.inputDesription}\n\n \
                       OUTPUT:\n{taskToServe.outputDescription}')
    templateDict = {}
    templateDict['taskName'] = taskToServe.problemName
    templateDict['taskDescription'] = taskToServe.problemDesciption
    templateDict['taskIO'] = IODescription
    templateDict['code'] = ''
    templateDict['consequence'] = ''
    templateDict['output'] = ''

    request.session['currTemplateDict'] = templateDict

    return render(request,'game.html',templateDict)








def shit(request):
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
