#!bin/bash
from util import *
import time
import os
import  subprocess

import datetime
import threading

SERVER = "192.168.1.107:3000"

TOKEN = "asdfrewq"

LANGUAGE = enum(C='gcc', JAVA='javac', PYTHON='python')

STATUS = enum( COMPILE_ERROR = "Compilation error", WRONG_ANSWER = "Wrong answer", TIME_LIMIT_EXCEEDED = "Time limit exceeded", MEMORY_LIMIT_EXCEEDED = "Memory limit exceeded", ACCEPTED = "Accepted")


env = dict(os.environ)

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
        return STATUS.TIME_LIMIT_EXCEEDED


class TestCase(object):
    """
    """
    language = ''
    input = ''
    correctOutput = ''
    code = ''
    solution_token = ''
    filename = str(time.time())
    compilefile = ''
    compileout =''
    compileerr=""
    runout=""
    output = ''
    timeLimit = ''
    memoryLimit = 0
    status = ""
    
    def __init__(self, dataOfDict):
        """
        """
        self.status = STATUS.ACCEPTED
        self.timeLimit = dataOfDict['time_limit']
        self.code = dataOfDict['code']
        self.language = convertLanguage(dataOfDict['language'])
        self.memoryLimit = dataOfDict['memory_limit']
        self.solution_token = dataOfDict['solution_token']
        self.input = dataOfDict['input']
        self.correctOutput = dataOfDict['output']

    def saveToDisk(self,):
        """
        """
    
        if self.language == LANGUAGE.C:
            self.filename = self.filename + ".c"
        if self.language == LANGUAGE.JAVA:
            self.filename = self.filename + '.java'
        if self.language == LANGUAGE.PYTHON:
            self.filename = self.filename + ".py"
        
        savefile = open(self.filename, 'w')
        savefile.write(self.code);
        savefile.close()
        
        pass

    def compile(self,):
        """
        """
        if self.language == LANGUAGE.C:
            
            self.compileout = subprocess.Popen('gcc -o '+self.filename+" "+self.compilefile);
            print self.compileout
        if self.language == LANGUAGE.JAVA:
            
            p = subprocess.Popen('javac '+self.filename,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE);
            self.compilefile= self.filename[0:-4]+".class"
            stdout,stderr = p.communicate()
            print stdout+"     out"
            print stderr+"       err"
        if self.language == LANGUAGE.PYTHON:
            self.compilefile = self.filename
            print "I'm Python not need Compile"
        pass
    
    def runScript(self,):
        """
        """
        if self.language == LANGUAGE.C:
            pass
        if self.language == LANGUAGE.JAVA:
            pass
        if self.language == LANGUAGE.PYTHON:
            p = subprocess.Popen(["python",self.compilefile]);
    
    def compareResult(self,):
        """
        """
        pass

    def runTest(self,):
        """
        1. save the data to a file in tmp folder (when finish run  be deleted)
        2. run the test
        3. monitor the memory and time
        4. if memory || time over, return result
        5. compare the output, return result
        """
        self.saveToDisk()
        
        self.compile()
        self.checkStaus()
        self.runScript()
        self.checkStaus()
        self.compareResult()
        
        self.postStatus()
        
    def checkStaus(self,):
        if self.status != STATUS.ACCEPTED:
            self.postStatus()

    def postStatus(self,):
        url = "http://" + SERVER +"/solutions/tester_set?token=" + TOKEN
        print "post status " + url
        postData = {"solution_token": self.solution_token, "status": self.status}
        data = post(url,postData)
            
        
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

