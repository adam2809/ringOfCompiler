import os

class ProgramTest():
    programFilename = 'game/testingSystem/tempProgram.py'
    errorLogFilename = 'game/testingSystem/tempErrorLog.txt'
    outLogFilename = 'game/testingSystem/tempOutLog.txt'
    #Fix this shitty hack as quick as possible
    inputFilename = 'game/testingSystem/tempInput.txt'

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
        print('DEBUG:')
        print(outString.strip())
        print(self.output.strip())
        if outString.strip() != self.output.strip():
            return 1
        return 0
