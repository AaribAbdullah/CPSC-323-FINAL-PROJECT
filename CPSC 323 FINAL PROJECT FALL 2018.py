
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
            if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' or string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or (string[i] == '/')) and (string[i -1] != ' ' and string[i -1] != '/'):
                string = string[:i]+' '+string[i]+string[i+1:len(string)]
                needs_another_look = True

        for i in range(0,len(string)-1):
            if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' or string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or (string[i] == '/')) and (string[i +1] != ' ' and string[i +1] != '/'):
                string = string[:i] + string[i] + ' ' + string[i + 1:len(string)]
                needs_another_look = True

    return  string


file1 = open('finalp1.txt', 'r')
output_to_file2 = open('finalp2.txt', 'w')

read_line = ''

while read_line != 'end':
    # while (read_line[0:2] != '/*' and read_line[len(read_line)-2:] != '*/') or read_line[0:2] != '//':

    read_line = file1.readline()            #This will read a line from the .txt file
    read_line = read_line.strip()              # This will strip whitespaces, \t s, and \n s from both sides of the string in variable
    read_line = read_line.replace('\t', '')  #It will remove any \t characters that still exist in the string

    read_line = RemoveWhiteSpaces(read_line) # will remove any excess whitespaces

    index_where_semicolon_is = 0
    is_there_a_semicolon = False

    are_there_comments = False
    comments_start_index = 0

    if read_line[0:2] !='/*' and read_line[len(read_line)-2:] != '*/' and read_line[0:2] !='//' and read_line != '':

        read_line = Space_Out(read_line)
        read_line = RemoveWhiteSpaces(read_line)

        for i in range(len(read_line)):

            # if read_line[i] == ';':
            #     index_where_semicolon_is = i
            #     is_there_a_semicolon = True

            if read_line[i - 2:i] == '//':
                are_there_comments = True
                comments_start_index = i - 2

        # if is_there_a_semicolon:
        #         #     read_line = read_line[0:index_where_semicolon_is + 1]
        #         #     output_to_file2.write(read_line + '\n')
        #         # else:
        #         #     if are_there_comments:
        #         #         read_line = read_line[0:comments_start_index]
        #         #         output_to_file2.write(read_line + '\n')
        #         #     else:
        #         #         output_to_file2.write(read_line + '\n')
        if are_there_comments:
            read_line = read_line[0:comments_start_index]
            output_to_file2.write(read_line + '\n')
        else:
            output_to_file2.write(read_line + '\n')