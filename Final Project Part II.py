
RAID ={'<prog>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','Program':'program<id>;var<dec-list>begin<stat-list>end','var':'','begin':'','end':'','integer':'','show':''},
       '<id>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<letter>X','b':'<letter>X','c':'<letter>X','d':'<letter>X','e':'<letter>X','Program':'','var':'','begin':'','end':'','integer':'','show':''},
       'X': {',':'λ', ':':'', ';':'λ', '(':'', '=':'λ', ')':'λ', '+':'', '-':'','*':'','/':'', '0':'<digit>X','1':'<digit>X','2':'<digit>X','3':'<digit>X','4':'<digit>X','5':'<digit>X','6':'<digit>X','7':'<digit>X','8':'','9':'<digit>X','a':'<letter>X','b':'<letter>X','c':'<letter>X','d':'<letter>X','e':'<letter>X','Program':'','var':'','begin':'','end':'','integer':'','show':''},
       '<dec-list>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<dec>:<type>;','b':'<dec>:<type>;','c':'<dec>:<type>;','d':'<dec>:<type>;','e':'<dec>:<type>;','Program':'','var':'','begin':'','end':'','integer':'','show':''},
       '<dec>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<id>,<dec>','b':'<id>,<dec>','c':'<id>,<dec>','d':'<id>,<dec>','e':'<id>,<dec>','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<type>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','Program':'','var':'','begin':'','end':'','integer':'integer','show':''},
        '<stat-list>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<stat><stat-list>','b':'<stat><stat-list>','c':'<stat><stat-list>','d':'<stat><stat-list>','e':'<stat><stat-list>','Program':'','var':'','begin':'','end':'','integer':'','show':'<stat><stat-list>'},
        '<stat>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<assign>','b':'<assign>','c':'<assign>','d':'<assign>','e':'<assign>','Program':'','var':'','begin':'','end':'','integer':'','show':'<write>'},
        '<write>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','Program':'','var':'','begin':'','end':'','integer':'','show':'show(<id>);'},
        '<assign>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'<id>=<expr>;','b':'<id>=<expr>;','c':'<id>=<expr>;','d':'<id>=<expr>;','e':'<id>=<expr>;','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<expr>': {',':'', ':':'', ';':'', '(':'<term>Q', '=':'', ')':'', '+':'<term>Q', '-':'<term>Q','*':'','/':'', '0':'<term>Q','1':'<term>Q','2':'<term>Q','3':'<term>Q','4':'<term>Q','5':'<term>Q','6':'<term>Q','7':'<term>Q','8':'<term>Q','9':'<term>Q','a':'<term>Q','b':'<term>Q','c':'<term>Q','d':'<term>Q','e':'<term>Q','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        'Q': {',':'', ':':'', ';':'λ', '(':'', '=':'', ')':'λ', '+':'+<term>Q', '-':'-<term>Q','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Term>': {',':'', ':':'', ';':'', '(':'<factor>R', '=':'', ')':'', '+':'<factor>R', '-':'<factor>R','*':'','/':'', '0':'<factor>R','1':'<factor>R','2':'<factor>R','3':'<factor>R','4':'<factor>R','5':'<factor>R','6':'<factor>R','7':'<factor>R','8':'<factor>R','9':'<factor>R','a':'<factor>R','b':'<factor>R','c':'<factor>R','d':'<factor>R','e':'<factor>R','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        'R': {',':'', ':':'', ';':'λ', '(':'', '=':'', ')':'λ', '+':'λ', '-':'λ','*':'*<factor>R','/':'/<factor>R', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Factor>': {',':'', ':':'', ';':'', '(':'(<expr>)', '=':'', ')':'', '+':'<number>', '-':'<number>','*':'','/':'', '0':'<number>','1':'<number>','2':'<number>','3':'<number>','4':'<number>','5':'<number>','6':'<number>','7':'<number>','8':'<number>','9':'<number>','a':'<id>','b':'<id>','c':'<id>','d':'<id>','e':'<id>','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Number>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'<sign><digit>B', '-':'<sign><digit>B','*':'','/':'', '0':'<sign><digit>B','1':'<sign><digit>B','2':'<sign><digit>B','3':'<sign><digit>B','4':'<sign><digit>B','5':'<sign><digit>B','6':'<sign><digit>B','7':'<sign><digit>B','8':'<sign><digit>B','9':'<sign><digit>B','a':'','b':'','c':'','d':'','e':'','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        'B': {',':'', ':':'', ';':'λ', '(':'', '=':'', ')':'λ', '+':'λ', '-':'λ','*':'λ','/':'λ', '0':'<digit>B','1':'<digit>B','2':'<digit>B','3':'<digit>B','4':'<digit>B','5':'<digit>B','6':'<digit>B','7':'<digit>B','8':'<digit>B','9':'<digit>B','a':'','b':'','c':'','d':'','e':'','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Sign>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'+', '-':'-','*':'','/':'', '0':'λ','1':'λ','2':'λ','3':'λ','4':'λ','5':'λ','6':'λ','7':'λ','8':'λ','9':'λ','a':'','b':'','c':'','d':'','e':'','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Digit>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','a':'','b':'','c':'','d':'','e':'','Program':'','var':'','begin':'','end':'','integer':'','show':''},
        '<Letter>': {',':'', ':':'', ';':'', '(':'', '=':'', ')':'', '+':'', '-':'','*':'','/':'', '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'a','b':'b','c':'c','d':'d','e':'e','Program':'','var':'','begin':'','end':'','integer':'','show':''}
       }

while True:
    lang = input("Enter the string: ")
    index = 0
    next = 0
    accepted = True
    match = False
    strung =''
    the_terminal = '' # This is the temporary variable for terminals with < and > formateed as <name>
    thestack = []
    thestack.append('end')
    print('\npush: end')


    for k in RAID.keys():
        print('push:' + k+'\n')
        thestack.append(k)
        break



    while(accepted and index < len(lang)):

        if match == True:
            match = False
        else:
            if strung != 'λ':
                print(thestack)

        tmp = thestack.pop()
        if tmp != 'λ':
            print('pop: ' + tmp)

        if tmp == 'end':
            break
        if tmp == lang[index]:
            print('match')
            match = True
            index += 1

        elif tmp != 'λ':
            if(index == next):
                next += 1
                print("reading:" + lang[index])


            strung = RAID[tmp][lang[index]]


            if RAID[tmp][lang[index]] == '':
                accepted =False
                print('[' + tmp + ', ' + lang[index] + "]   is a box that's empty")
                break
            else:
                print('[' + tmp + ', ' + lang[index] + '] = ' + strung)
            push = []

            if strung != 'λ':
                for i in range(len(strung)-1,-1,-1):
                    thestack.append(strung[i])
                    push.append(strung[i])
                print('push: ', end='')
                print(push)
                print('\n')



    if(accepted):
        print("\naccepted\n")
    else:
        print('\nrejected\n')
    cont = input('Y to cont. and N to stop\n')
    if cont == 'N':
        break
