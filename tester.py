from util import *

LANGUAGE = enum(C='gcc', JAVA='javac', PYTHON='python')
ERROR = enum( ERROR_COMPILE = "", ERROR_WRONG_ANSWER = "", ERROR_TIME_OVER = "", ERROR_MEMORY_OVER = "")


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
    
    
    def __init__(self, ):
        """
        """

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
    """
    testcase for convert language
    """
    assert convertLanguage("C") ==  LANGUAGE.C
    assert convertLanguage("java") ==  LANGUAGE.JAVA
    assert convertLanguage("PythoN") ==  LANGUAGE.PYTHON
    print "language convert pass!"

    '''
    testcase for normal case
    '''
    testcase = TestCase()
    testcase.language = convertLanguage("C")
    testcase.code = 'asdfasdf'
    testcase.input = "asdfasdfasdf"
    testcase.output = "asdf"
    testcase.solution_token = "123aaa"
    
    testcase.runTest()
