import os,json

enumName = 'Common'
fileLoc = 'C:/ScriptTesting/' + enumName + '.java'
values_json = '{"Success":"SUCCESS", "Error":"ERROR"}'


def getEnumValues(values_json):
    enumValues =''
    output_json = json.loads(values_json)
    for val in output_json:
        valData = ''
        valData = val + '("' + output_json[val] + '"),'
        enumValues += valData
    
    return enumValues  
  
 
def getEnumHeader(enumName):
    return 'public enum ' + enumName + ' {' + os.linesep


def getEnumBody():
    return '''
    private String value;
    
    public String getValue() {
        return value;
    }
    
    '''
    
def getEnumConstructor(enumName):
    constructor = 'private ' +   enumName
    constructor += '''(String code) {
        value = code;
    }
    ''' 
    
    return constructor
    
def getEnumTerminator():
    return os.linesep + '}' 

def writeEnumFile(fileLoc,enumName):
    enumFile = open(fileLoc, 'w')
    enumFile.write(getEnumHeader(enumName))
    enumValues = (getEnumValues(values_json))[:-1] + ';' + os.linesep
    enumFile.write('\t' + enumValues)
    enumFile.write(getEnumBody())
    enumFile.write(getEnumConstructor(enumName))
    enumFile.write(getEnumTerminator())
    enumFile.close()

if(os.path.isfile(fileLoc)):
    os.remove(fileLoc)
    
writeEnumFile(fileLoc, enumName)
