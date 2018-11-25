import os

def printFile(file):
    for line in file:
        print(line)

def test(code,input,desiredOutput):
    programFilename = 'temp.py'
    errorLogFilename = 'tempErrorLog.txt'
    outLogFilename = 'tempOutLog.txt'
    #Fix this shitty hack as quick as possible
    inputFilename = 'tempInput.txt'

    print(f'code:\n{code}\ninput:\n{input}\ndesi:\n{desiredOutput}')

    inputFile = open(inputFilename,'w+')
    inputFile.write(input)
    inputFile.close()

    tempProgramFile = open(programFilename,'w+')
    tempProgramFile.write(code)
    tempProgramFile.close()

    cmd  = f'python3 {programFilename} < {inputFilename} > {outLogFilename} 2> {errorLogFilename}'
    os.system(cmd)

    tempOutLogFile = open(outLogFilename,'r')
    tempErrorLogFile = open(errorLogFilename,'r')

    if os.stat(errorLogFilename).st_size:
        return 2

    outputString = ''
    for line in tempOutLogFile:
        outputString += line
    outputString = outputString[:-1]
    # TODO sripping desired output is not a premanent solution as it is probably
    # a bun in loader.py which will be scrapped anyways maybe probably
    if outputString != desiredOutput.strip():
        return 1

    tempOutLogFile.close()
    tempErrorLogFile.close()

    return 0
