import os

# def printFile(file):
#     for line in file:
#         print(line)
class ProgramTest():
    programFilename = 'tempProgram.txt'
    errorLogFilename = 'tempErrorLog.txt'
    outLogFilename = 'tempOutLog.txt'
    #Fix this shitty hack as quick as possible
    inputFilename = 'tempInput.txt'

    def __init__(self,code,input,output):
        self.code = code
        self.input = input
        self.output = output

        #state is 0 before running the program it flips to 1 after running
        self.state = 0


    def run(self):
        # print(f'code:\n{code}\ninput:\n{input}\ndesi:\n{desiredOutput}')
        inputFile = open(self.inputFilename,'w+')
        inputFile.write(self.input)
        inputFile.close()

        tempProgramFile = open(self.programFilename,'w+')
        tempProgramFile.write(self.code)
        tempProgramFile.close()

        cmd  = f'python3 {self.programFilename} < {self.inputFilename} \
         > {self.outLogFilename} 2> {self.errorLogFilename}'
        os.system(cmd)

        tempOutLogFile = open(self.outLogFilename,'r')
        tempErrorLogFile = open(self.errorLogFilename,'r')


        outString = tempOutLogFile.read()
        errorString = tempErrorLogFile.read()

        tempOutLogFile.close()
        tempErrorLogFile.close()
        self.state = 1

        if os.stat(self.errorLogFilename).st_size:
            return errorString
        else:
            return outString[:-1]


    def test(self):
        if self.state == 0:
            return None

        if os.stat(self.errorLogFilename).st_size:
            return 2

        tempOutLogFile = open(self.outLogFilename,'r')
        outString = tempOutLogFile.read()
        tempOutLogFile.close()
        if outString[:-1] != self.output:
            return 1
        return 0



# def test(code,input,desiredOutput):
#     programFilename = 'temp.py'
#     errorLogFilename = 'tempErrorLog.txt'
#     outLogFilename = 'tempOutLog.txt'
#     #Fix this shitty hack as quick as possible
#     inputFilename = 'tempInput.txt'
#
#     # print(f'code:\n{code}\ninput:\n{input}\ndesi:\n{desiredOutput}')
#
#     inputFile = open(inputFilename,'w+')
#     inputFile.write(input)
#     inputFile.close()
#
#     tempProgramFile = open(programFilename,'w+')
#     tempProgramFile.write(code)
#     tempProgramFile.close()
#
#     cmd  = f'python3 {programFilename} < {inputFilename} > {outLogFilename} 2> {errorLogFilename}'
#     os.system(cmd)
#
#
#     tempOutLogFile = open(outLogFilename,'r')
#     tempErrorLogFile = open(errorLogFilename,'r')
#
#
#     if os.stat(errorLogFilename).st_size:
#         return 2
#
#         #Copied until here
#     outputString = ''
#     for line in tempOutLogFile:
#         outputString += line
#     outputString = outputString[:-1]
#     # TODO sripping desired output is not a premanent solution as it is probably
#     # a bun in loader.py which will be scrapped anyways maybe probably
#     if outputString != desiredOutput.strip():
#         return 1
#
#     tempOutLogFile.close()
#     tempErrorLogFile.close()
#
#     return 0
