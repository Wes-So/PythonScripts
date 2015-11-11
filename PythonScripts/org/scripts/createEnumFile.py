import os

enumFile = open('C:/ScriptTesting/testFile2.java', 'w')
enumFile.write('public enum Common {' + os.linesep)
enumFile.write('}')
enumFile.close()

