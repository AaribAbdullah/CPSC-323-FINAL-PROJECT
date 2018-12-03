
def RemoveWhiteSpaces(string):
    result = ''
    previous_Char = " "

    for i in string:
        if not (previous_Char == ' ' and i == previous_Char ):
            result += i
        previous_Char = i

    return result

def Space_Out(string):
    result = ''
    # previous_Char = " "
    k = 0
    length = len(string)
    needs_another_look = True
    while needs_another_look:
        needs_another_look = False
        for i in range(1,length):
            if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' or string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/') and string[i -1] != ' ':
                # result =+ (string[k:i]+' '+string[i])
                #  result = result + string[k:i] + ' ' +string[i]
                string = string[k:i]+' '+string[i]+' '+string[i+1:len(string)]
                length = len(string)
                needs_another_look = True
                # k = i + 1
        length = len(string)
        for i in range(1,length-1):
            if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' or string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/') and string[i +1] != ' ':
                # result =+ (string[k:i]+' '+string[i])
                #  result = result + string[k:i] + ' ' +string[i]
                string = string[k:i]+' '+string[i]+' '+string[i+1:len(string)]
                length = len(string)
                needs_another_look = True

    # length = len(string)
    # for i in range(1, length):
    #     if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' or string[i] == '(' or string[
    #         i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/') and string[
    #         i - 1] != ' ':
    #         # result =+ (string[k:i]+' '+string[i])
    #         #  result = result + string[k:i] + ' ' +string[i]
    #         string = string[k:i] + ' ' + string[i] + ' ' + string[i + 1:len(string)]
    #         length = len(string)
    #         # k = i + 1
    #
    # length = len(string)
    # for i in range(1, length - 1):
    #     if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' or string[i] == '(' or string[
    #         i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/') and string[
    #         i + 1] != ' ':
    #         # result =+ (string[k:i]+' '+string[i])
    #         #  result = result + string[k:i] + ' ' +string[i]
    #         string = string[k:i] + ' ' + string[i] + ' ' + string[i + 1:len(string)]
    #         length = len(string)

    return  string

# s = 'd18=ab1*(cd)'
# s = Space_Out(s)


file1 = open('finalp1.txt', 'r')
output_to_file2 = open('finalp2.txt', 'w')

read_line = ''
# read_line = file1.readline()                #1
# read_line = read_line.strip()
# read_line = read_line.replace('\t', '')
#
# read_line = RemoveWhiteSpaces(read_line)
# read_line = Space_Out(read_line)
# read_line = RemoveWhiteSpaces(read_line)
# # for i in range(len(read_line)):
# #     if read_line[i] == ';' and read_line[i-1] == ' ':
# #         read_line = read_line[0:i-1] + ';'
# #         break
# # read_line = RemoveWhiteSpaces(read_line)    # 1 - is to check what is the first line
#
#
# while read_line == '':                      #2 - if first line is empty will continue to go down the file to look for string
#     read_line = file1.readline()
#     read_line = read_line.strip()
#     read_line = read_line.replace('\t', '')
#
#     read_line = RemoveWhiteSpaces(read_line)
#     read_line = Space_Out(read_line)
#     read_line = RemoveWhiteSpaces(read_line)
#
#     # for i in len(read_line):
#     #     if read_line[i] == ';':
#     #         temp = read_line[i]
#     #         read_line[i] = read_line[i - 1]
#     #         read_line[i - 1] = temp
#     #         break
#     # read_line = RemoveWhiteSpaces(read_line)
#
# output_to_file2.write(read_line + '\n')

# once the first line has been found, we will expect different lines other than
while read_line != 'end':
    # while (read_line[0:2] != '/*' and read_line[len(read_line)-2:] != '*/') or read_line[0:2] != '//':

    read_line = file1.readline()
    read_line = read_line.strip()
    read_line = read_line.replace('\t', '')

    # read_line = RemoveWhiteSpaces(read_line)            ##NEED A PART TO GIVE INT VARIABLES SPACES
    read_line = RemoveWhiteSpaces(read_line)
    # read_line = Space_Out(read_line)
    # read_line = RemoveWhiteSpaces(read_line)

    index_where_semicolon_is = 0
    is_there_a_semicolon = False

    are_there_comments = False
    comments_start_index = 0

    # i = 0
    # for i in range(len(read_line)):
    #     if read_line[i] == ';':
    #         index_where_semicolon_is = i
    #         is_there_a_semicolon = True
    #     if read_line [i-2:i] == '//':
    #         are_there_comments = True
    #         comments_start_index = i-2

    read_line = RemoveWhiteSpaces(read_line)
    if read_line[0:2] !='/*' and read_line[len(read_line)-2:] != '*/' and read_line[0:2] !='//' and read_line != '':
        read_line = Space_Out(read_line)
        read_line = RemoveWhiteSpaces(read_line)
        for i in range(len(read_line)):
            if read_line[i] == ';':
                index_where_semicolon_is = i
                is_there_a_semicolon = True
            if read_line[i - 2:i] == '//':
                are_there_comments = True
                comments_start_index = i - 2
        if is_there_a_semicolon:
            # output_to_file2.write('\t'+read_line[0:index_where_semicolon_is+1]+'\n')
            read_line = read_line[0:index_where_semicolon_is + 1]
            output_to_file2.write(read_line + '\n')
        else:
            if are_there_comments:
                read_line = read_line[0:comments_start_index]
                output_to_file2.write(read_line + '\n')
            else:
                output_to_file2.write(read_line + '\n')


    # begin_WN = 0
    # end_WN = 0
    # temp_string = ''
    # start_of_Word_or_Number = False
    # end_of_Word_or_Number = False
    # for i in len(read_line):
    #     if read_line[i] != ' ':


