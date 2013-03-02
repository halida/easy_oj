#!bin/bash
from util import *
import time
import os
import  subprocess

LANGUAGE = enum(C='gcc', JAVA='javac', PYTHON='python')
ERROR = enum(ERROR_COMPILE="", ERROR_WRONG_ANSWER="", ERROR_TIME_OVER="", ERROR_MEMORY_OVER="")


env = dict(os.environ)

def convertLanguage(language):
    language_lower = language.lower()
    if language_lower == "c":
        
        return LANGUAGE.C
    elif language_lower == 'java':
        return LANGUAGE.JAVA
    elif language_lower == 'python':
        return LANGUAGE.PYTHON

class TestCase(object):
    """
    """
    language = ''
    input = ''
    output = ''
    code = ''
    solution_token = ''
    filename = str(time.time())
    compilefile = ''
    compileout =''
    compileerr=""
    runout=""
    
    def __init__(self,):
        """
        """
        self.savefile = None

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
            pass
        
        pass
    
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
    """
    testcase for convert language
    """
    assert convertLanguage("C") == LANGUAGE.C
    assert convertLanguage("java") == LANGUAGE.JAVA
    assert convertLanguage("PythoN") == LANGUAGE.PYTHON
    print "language convert pass!"

    '''
    testcase for normal case
    '''
    testcase = TestCase()
    testcase.language = convertLanguage("java")
    testcase.code = 'asdfasdf'
    testcase.input = "asdfasdfasdf"
    testcase.output = "asdf"
    testcase.solution_token = "123aaa"
    
    testcase.runTest()
