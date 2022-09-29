def checkParenthesis(str):
    if len(str) == 0:
        ret = True
    elif (len(str) % 2) == 1:
        ret = False
    else:
        tmpStr = str
        while len(tmpStr) > 0:
            initialTmpStr = tmpStr
            tmpStr = tmpStr.replace('[]', '').replace('{}', '').replace('()', '')
            if initialTmpStr == tmpStr: break # nothing to replace
        ret = len(tmpStr) == 0
    print("checkParenthesis('%s') -> %s" % (str, ret))
    return ret

checkParenthesis("([)")
checkParenthesis("([])")
checkParenthesis("(()[]){}")
checkParenthesis("(()[]){)")
checkParenthesis("[{}({})]")
checkParenthesis("[{}({)}]")
