from util import *
import datetime
import subprocess
import time
import threading

SERVER = "192.168.1.107:3000"

TOKEN = "asdfrewq"

LANGUAGE = enum(C='gcc', JAVA='javac', PYTHON='python')

ERROR = enum( ERROR_COMPILE = "COMPILE_ERROR", ERROR_WRONG_ANSWER = "WRONG_ANSWER", ERROR_TIME_OVER = "TIME_OVER", ERROR_MEMORY_OVER = "MEMORY_OVER")


def convertLanguage(language):
    language_lower = language.lower()
    if language_lower == "c":
        return LANGUAGE.C
    elif language_lower == 'java':
        return LANGUAGE.JAVA
    elif language_lower == 'python':
        return LANGUAGE.PYTHON

def timeMonitor(timeLimit, monitorProcess):
    time.sleep(timeLimit)
    if monitorProcess.is_alive():
        return ERROR_TIME_OVER


class TestCase(object):
    """
    """
    language = ''
    input = ''
    correctOutput = ''
    code = ''
    solution_token = ''
    output = ''
    timeLimit = ''
    memoryLimit = 0
    
    def __init__(self, dataOfDict):
        """
        """
        self.timeLimit = dataOfDict['time_limit']
        self.code = dataOfDict['code']
        self.language = convertLanguage(dataOfDict['language'])
        self.memoryLimit = dataOfDict['memory_limit']
        self.solution_token = dataOfDict['solution_token']
        self.input = dataOfDict['input']
        self.correctOutput = dataOfDict['output']

    def saveToDisk(self, ):
        """
        """
        pass

    def compile(self, ):
        """
        """
        pass
    
    def runScript(self, ):
        
        """
        """

        pass
    
    def compareResult(self,):
        """
        """
        pass

    def runTest(self, ):
        """
        1. save the data to a file in tmp folder (when finish run  be deleted)
        2. run the test
        3. monitor the memory and time
        4. if memory || time over, return result
        5. compare the output, return result
        """
        error = 0
        self.saveToDisk()
        error = self.compile()
        if error:
            return 0
        error = self.runScript()
        error = self.compareResult()

               
if __name__ == '__main__':
    """
    code: "...", // source code
    language: "..", // python/java/...
    input: "...", // stdin
    output: "...", // expected stdout
    solution_token: "...", // used to identify solution
    """
    url = "http://" + SERVER +"/solutions/tester_get?token=" + TOKEN
    while True:
        data = post(url, {})
        if data != '{}':
            dataOfDict = parseJSON(data)
            testcase = TestCase(dataOfDict)
            testcase.runTest()
        time.sleep(2)






    """
    testcase for convert language
    """
    assert convertLanguage("C") ==  LANGUAGE.C
    assert convertLanguage("java") ==  LANGUAGE.JAVA
    assert convertLanguage("PythoN") ==  LANGUAGE.PYTHON
    print "language convert pass."


    """
    testcase for string compare
    """
    assert compareText("asdf", "asdf") == 0
    assert compareText("asdf", "sad") == -1
    assert compareText("asdf\n1234", "asdf\n1234") == 0
    assert compareText("asdf\n1234\n\n", "asdf\n1234") == 0
    assert compareText("asdf\n123", "asdf\n1234") == -1
    print "compareText pass."

    """
    testcase for getNetworkData
    """
    url = "http://" + SERVER +"/solutions/tester_get?token=" + TOKEN
    print url
    postData = {}
    data = post(url,postData)
    print data
    print "getNetworkData pass."
    assert data != {}


    """
    testcase for setNetworkData
    """
    url = "http://" + SERVER +"/solutions/tester_set?token=" + TOKEN
    print url
    postData = {"solution_token": "256d3f5124ee", "status":"Accepted" }
    data = post(url,postData)
    mydict = ast.literal_eval( data)
    print mydict
    assert mydict['result'] == "OK"
    print "setNetworkData pass."

"""
    '''
    testcase for normal case
    '''
    testcase = TestCase()
    testcase.language = convertLanguage("C")
    testcase.code = 'asdfasdf'
    testcase.input = "asdfasdfasdf"
    testcase.correctOutput = "asdf"
    testcase.solution_token = "123aaa"
    testcase.timeLimit = "5"  #5 seconds
    testcase.memoryLimit = 10240 # 10M
    testcase.runTest()
"""
