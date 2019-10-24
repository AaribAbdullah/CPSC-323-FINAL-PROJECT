
def RemoveWhiteSpaces(string):
    result = ''
    previous_Char = " "

    for i in string:
        if not (previous_Char == ' ' and i == previous_Char ):
            result += i
        previous_Char = i

    return result

def Space_Out(string):

    needs_another_look = True

    while needs_another_look:

        needs_another_look = False

        for i in range(1,len(string)):
            if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' or string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/' or string[i] == '<') and (string[i -1] != ' ' and string[i -1] != '/' ):
                string = string[:i]+' '+string[i]+string[i+1:len(string)]
                needs_another_look = True

        for i in range(0,len(string)-1):
            if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' or string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/' or string[i] == '>') and (string[i +1] != ' ' and string[i +1] != '/' ):
                string = string[:i] + string[i] + ' ' + string[i + 1:len(string)]
                needs_another_look = True

    return  string

def Words_From_Strings_Into_List(string):

    List = []
    non_space_char = 0
    is_non_space_char_assigned = False
    for i in range(len(string)):
        if(string[i] != ' ' and is_non_space_char_assigned == False):
            non_space_char = i
            is_non_space_char_assigned = True
        elif(string[i] == ' '):
            List.append(string[non_space_char:i])
            is_non_space_char_assigned = False
    List.append(string[non_space_char:])
    return List

def If_Is_Reserved_Word(string):
    if(string == 'program' or string == 'var' or string == 'begin' or string == 'end' or string == 'integer' or string == 'show'):
        return True
    return False