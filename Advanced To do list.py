def add():
    inpadd=input('Enter your value to Add: ')
    tasks.append(inpadd)
    print('Added!')
def display():
    if tasks==[]:
        print('There is nothing to Display!')
    else:
        print('Your tasks: ')
        for i in tasks:
           print(i)
def remove():
    if tasks==[]:
        print('There is nothing to Remove!')
    else:
        print('Tasks you can Remove: ')
        for i in tasks:
           print(i)
        inpremove=input('Enter a task to Remove: ')
        if inpremove not in tasks:
            print(f'There is no {inpremove}!')
        else:
            tasks.remove(inpremove)
            print('Removed!')
            print('Updated list: ')
            for i in tasks:
               print(i)
def edit():
    if tasks==[]:
        print('There is nothing to Edit!')
    else:
        print('Tasks you can Edit: ')
        for i in tasks:
           print(i)
        inpeditw=input('Enter a task to Edit: ')
        if inpeditw not in tasks:
            print(f'There is no {inpeditw}!')
        else:
            inpedit=input('Enter new value: ')
            tasks.remove(inpeditw)
            tasks.append(inpedit)
            print('Edited!')
            print('Updated list: ')
            for i in tasks:
                print(i)
def search():
    if tasks==[]:
        print('There is nothing to Search!')
    else:    
        inpsearch=input('Enter a value to search: ')
        if inpsearch in tasks:
            print(f'{inpsearch} is in list!')
        else:
            print(f'{inpsearch} is not in list!')
def helpp():
    print('\n','choose one of below options to help:','\n','1-Add','\n','2-Display','\n','3-Remove','\n','4-Edit','\n','5-Search')
    choose=int(input('Enter opration number for help: '))
    if choose==1:
        print('Adds input value to list.')
    elif choose==2:
        print('Displays the list.')
    elif choose==3:
        print('Removes input value from list.')
    elif choose==4:
        print('Edits input value in list.')
    elif choose==5:
        print('if input was in list prints it is and if not prints its not')
    else:
        print('Enter correct number!')
tasks=[]
print('welcome','\n','author:Youna afshar')
while True:
    print('\n','choose one of below oprations:','\n','1-Add','\n','2-Display','\n','3-Remove','\n','4-Edit','\n','5-Search','\n','6-Help','\n','0-Exit')
    choise=int(input('Enter Opration Number: '))
    if choise==1:
        add()
    elif choise==2:
        display()
    elif choise==3:
        remove()
    elif choise==4:
        edit()
    elif choise==5:
        search()
    elif choise==6:
        helpp()
    elif choise==0:
        if tasks==[]:
            print('you have no task in your list.')
        else:
            print('Your tasks: ')
            for i in tasks:
               print(i)
        break
    else:
        print('Enter correct number!')
print('see you next time!')
print('@youna afshar')