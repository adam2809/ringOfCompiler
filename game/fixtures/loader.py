import json
import copy
taskSource = open(r'/home/adam/code/ringOfCompiler/dataLoaders/taskText.txt','r')
taskDest = open(r'/home/adam/code/ringOfCompiler/game/fixtures/tasks.json','w')

testSource = \
open(r'/home/adam/code/ringOfCompiler/dataLoaders/testText.txt','r')
testDest = open(r'/home/adam/code/ringOfCompiler/game/fixtures/tests.json','w')

taskEntries = []
taskEntry = {'model':'game.Task','pk':None,
'fields':{'problemName':None,'problemDesciption':None,'inputDesription':None,\
'outputDescription':None}}

testEntries = []
testEntry = {'model':'game.Task','pk':None,
'fields':{'input':None,'output':None,'task':None}}

currEntry=''
for line in taskSource:
    if(line == '#\n'):
        currEntryLines = currEntry.split('\n\n')
        currEntryDict = copy.deepcopy(taskEntry)

        currEntryDict['pk'] = len(taskEntries) + 1
        currEntryDict['fields']['problemName'] = currEntryLines[0]
        currEntryDict['fields']['problemDesciption'] = currEntryLines[1]
        currEntryDict['fields']['inputDesription'] = currEntryLines[2]
        currEntryDict['fields']['outputDescription'] = currEntryLines[3]

        taskEntries.append(currEntryDict)
    else:
        currEntry+=line

for line in testSource:
    pass

taskDest.write(json.dumps(taskEntries))
