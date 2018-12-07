from help import RemoveWhiteSpaces
from help import Space_Out
from help import Words_From_Strings_Into_List
from help import If_Is_Reserved_Word

# def RemoveWhiteSpaces(string):
#     result = ''
#     previous_Char = " "
#
#     for i in string:
#         if not (previous_Char == ' ' and i == previous_Char ):
#             result += i
#         previous_Char = i
#
#     return result
#
# def Space_Out(string):
#
#     needs_another_look = True
#
#     while needs_another_look:
#
#         needs_another_look = False
#
#         for i in range(1,len(string)):
#             if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' or string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/' or string[i] == '<') and (string[i -1] != ' ' and string[i -1] != '/' ):
#                 string = string[:i]+' '+string[i]+string[i+1:len(string)]
#                 needs_another_look = True
#
#         for i in range(0,len(string)-1):
#             if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' or string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/' or string[i] == '>') and (string[i +1] != ' ' and string[i +1] != '/' ):
#                 string = string[:i] + string[i] + ' ' + string[i + 1:len(string)]
#                 needs_another_look = True
#
#     return  string
#
# def Words_From_Strings_Into_List(string):
#
#     List = []
#     non_space_char = 0
#     is_non_space_char_assigned = False
#     for i in range(len(string)):
#         if(string[i] != ' ' and is_non_space_char_assigned == False):
#             non_space_char = i
#             is_non_space_char_assigned = True
#         elif(string[i] == ' '):
#             List.append(string[non_space_char:i])
#             is_non_space_char_assigned = False
#     List.append(string[non_space_char:])
#     return List
#
# def If_Is_Reserved_Word(string):
#     if(string == 'program' or string == 'var' or string == 'begin' or string == 'end' or string == 'integer' or string == 'show'):
#         return True
#     return False

# s = '1+2-A<Sign><abc>'
# s = Space_Out(s)
# s = RemoveWhiteSpaces(s)
# S = Words_From_Strings_Into_List(s)
print("\n\nWHITE SPACE AND COMMENT REMOVEAL\n\n")
file1_name = input("Which file will you read from ? : ")
file2_name = input("Which file will you write to ? : ")
file1 = open(file1_name, 'r')
output_to_file2 = open(file2_name, 'w')

read_line = ''

while read_line != 'end':

    read_line = file1.readline()            #This will read a line from the .txt file
    read_line = read_line.strip()              # This will strip whitespaces, \t s, and \n s from both sides of the string in variable
    read_line = read_line.replace('\t', '')  #It will remove any \t characters that still exist in the string

    read_line = RemoveWhiteSpaces(read_line) # will remove any excess whitespaces

    are_there_comments = False
    comments_start_index = 0

    if read_line[0:2] !='/*' and read_line[len(read_line)-2:] != '*/' and read_line[0:2] !='//' and read_line != '':

        read_line = Space_Out(read_line)
        read_line = RemoveWhiteSpaces(read_line)

        for i in range(len(read_line)):

            if read_line[i - 2:i] == '//':
                are_there_comments = True
                comments_start_index = i - 2

        if are_there_comments:
            read_line = read_line[0:comments_start_index]
            output_to_file2.write(read_line + '\n')
        else:
            output_to_file2.write(read_line + '\n')


file1.close()
output_to_file2.close()



RULE ={'<prog>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','program':'program <id> ; var <dec-list> begin <stat-list> end','var':'','begin':'','end':'','integer':'','show':''},
       '<id>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<letter> X','b':'<letter> X','c':'<letter> X','d':'<letter> X','e':'<letter> X','program':'','var':'','begin':'','end':'','integer':'','show':''},
       'X': {',':'λ', ':':'', ';':'λ', '(':'', '=':'λ', ')':'λ', '+':'', '-':'','*':'','/':'', '0':'<digit> X','1':'<digit> X','2':'<digit> X','3':'<digit> X','4':'<digit> X','5':'<digit> X','6':'<digit> X','7':'<digit> X','8':'<digit> X','9':'<digit> X','a':'<letter> X','b':'<letter> X','c':'<letter> X','d':'<letter> X','e':'<letter> X','program':'','var':'','begin':'','end':'','integer':'','show':''},
       '<dec-list>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<dec> : <type> ;','b':'<dec> : <type> ;','c':'<dec> : <type> ;','d':'<dec> : <type> ;','e':'<dec> : <type> ;','program':'','var':'','begin':'','end':'','integer':'','show':''},
       '<dec>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<id> , <dec>','b':'<id> , <dec>','c':'<id> , <dec>','d':'<id> , <dec>','e':'<id> , <dec>','program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<type>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','program':'','var':'','begin':'','end':'','integer':'integer','show':''},
        '<stat-list>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<stat> <stat-list>','b':'<stat> <stat-list>','c':'<stat> <stat-list>','d':'<stat> <stat-list>','e':'<stat> <stat-list>','program':'','var':'','begin':'','end':'','integer':'','show':'<stat> <stat-list>'},
        '<stat>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<assign>','b':'<assign>','c':'<assign>','d':'<assign>','e':'<assign>','program':'','var':'','begin':'','end':'','integer':'','show':'<write>'},
        '<write>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','program':'','var':'','begin':'','end':'','integer':'','show':'show(<id>);'},
        '<assign>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<id> = <expr>;','b':'<id> = <expr>;','c':'<id> = <expr>;','d':'<id> = <expr>;','e':'<id> = <expr>;','program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<expr>': {',':'', ':':'', ';':'', '(':'<term> Q', '=':'', ')':'', '+':'<term> Q', '-':'<term> Q','*':'','/':'', '0':'<term> Q','1':'<term> Q','2':'<term> Q','3':'<term> Q','4':'<term> Q','5':'<term> Q','6':'<term> Q','7':'<term> Q','8':'<term> Q','9':'<term> Q','a':'<term> Q','b':'<term> Q','c':'<term> Q','d':'<term> Q','e':'<term> Q','program':'','var':'','begin':'','end':'','integer':'','show':''},
        'Q': {',':'', ':':'', ';':'λ', '(':'', '=':'', ')':'λ', '+':'+ <term> Q', '-':'- <term> Q','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Term>': {',':'', ':':'', ';':'', '(':'<factor> R', '=':'', ')':'', '+':'<factor> R', '-':'<factor> R','*':'','/':'', '0':'<factor> R','1':'<factor> R','2':'<factor> R','3':'<factor> R','4':'<factor> R','5':'<factor> R','6':'<factor> R','7':'<factor> R','8':'<factor> R','9':'<factor> R','a':'<factor> R','b':'<factor> R','c':'<factor> R','d':'<factor> R','e':'<factor> R','program':'','var':'','begin':'','end':'','integer':'','show':''},
        'R': {',':'', ':':'', ';':'λ', '(':'', '=':'', ')':'λ', '+':'λ', '-':'λ','*':'* <factor> R','/':'/ <factor> R', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Factor>': {',':'', ':':'', ';':'', '(':'( <expr> )', '=':'', ')':'', '+':'<number>', '-':'<number>','*':'','/':'', '0':'<number>','1':'<number>','2':'<number>','3':'<number>','4':'<number>','5':'<number>','6':'<number>','7':'<number>','8':'<number>','9':'<number>','a':'<id>','b':'<id>','c':'<id>','d':'<id>','e':'<id>','program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Number>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'<sign> <digit> B', '-':'<sign> <digit> B','*':'','/':'', '0':'<sign> <digit> B','1':'<sign> <digit> B','2':'<sign> <digit> B','3':'<sign> <digit> B','4':'<sign> <digit> B','5':'<sign> <digit> B','6':'<sign> <digit> B','7':'<sign> <digit> B','8':'<sign> <digit> B','9':'<sign> <digit> B','a':'','b':'','c':'','d':'','e':'','program':'','var':'','begin':'','end':'','integer':'','show':''},
        'B': {',':'', ':':'', ';':'λ', '(':'', '=':'', ')':'λ', '+':'λ', '-':'λ','*':'λ','/':'λ', '0':'<digit> B','1':'<digit> B','2':'<digit> B','3':'<digit> B','4':'<digit> B','5':'<digit> B','6':'<digit> B','7':'<digit> B','8':'<digit> B','9':'<digit> B','a':'','b':'','c':'','d':'','e':'','program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Sign>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'+', '-':'-','*':'','/':'', '0':'λ','1':'λ','2':'λ','3':'λ','4':'λ','5':'λ','6':'λ','7':'λ','8':'λ','9':'λ','a':'','b':'','c':'','d':'','e':'','program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Digit>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','a':'','b':'','c':'','d':'','e':'','program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Letter>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'a','b':'b','c':'c','d':'d','e':'e','program':'','var':'','begin':'','end':'','integer':'','show':''}
       }
print("\n\nSYNTAX ANALYSIS\n\n")
#The bottom from here will be a code from project 7 but modified
fileName = input("Which file will you read from ? : ")
file_to_be_analyzed = open(fileName, 'r')

# language = input("Enter a language: ")
language = input("Enter a language: ")

read_index = 0
read_next = 0

is_language_accepted = True
is_match = False

string = ''
stack = []
stack.append('end')  # append in this case is push
print('\nPush: end')
for first_key in RULE.keys():  # This is to push the starting symbol
    print('Push:' + first_key + '\n')
    stack.append(first_key)
    break

while (is_language_accepted and read_index < len(language)):

    if string != 'λ':
        print(stack)

    temp = stack.pop()
    if temp != 'λ':
        print('Pop: ' + temp)

    if temp == 'end':
        break

    if temp == language[read_index]:
        print('match')
        is_match = True
        read_index += 1

    elif temp != 'λ':

        if (read_index == read_next):
            read_next += 1
            print('-' * 10)
            print("Read:" + language[read_index])
            print('-' * 10)

        string = RULE[temp][language[read_index]]

        if RULE[temp][language[read_index]] == '':
            is_language_accepted = False
            print('[' + temp + ', ' + language[read_index] + ']   is an empty box/entry')
            break
        else:
            print('[' + temp + ', ' + language[read_index] + '] = ' + string)
        show_push_action = []

        if string != 'λ':
            for i in range(len(string) - 1, -1, -1):
                stack.append(string[i])
                show_push_action.append(string[i])
            print('Push: ', end='')
            print(show_push_action)
            print('\n')

# end result
if (is_language_accepted):
    print("\nACCPETED")
else:
    print('\nREJECTED')