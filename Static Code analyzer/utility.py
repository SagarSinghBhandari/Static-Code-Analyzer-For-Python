import re
from collections import defaultdict
import keyword
import builtins


def removeSpecialCharacters(docx):
  str = re.sub(r"\W+"," ",docx)
  return str

def getKeywordsCount(docx):
  cleanedStr = removeSpecialCharacters(docx)
  keyDic = defaultdict(int)
  identifierDic = defaultdict(int)
  builtinsDic = defaultdict(int)
  for i in cleanedStr.split(): # to tokenize source code
    if i in keyword.kwlist:  #If found in keyword list then add to keyword dictionary
      keyDic[i] += 1
    elif i in list(dir(builtins)): #else it can be a builtin
      builtinsDic[i] += 1
    else:  #if not any of the above case then it is a identifier
      identifierDic[i] += 1

  result = {"Keywords": keyDic,"Identifiers":identifierDic,"Builtins":builtinsDic} 
  return result

