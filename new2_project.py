import random
import matplotlib.pyplot as plt
import copy

#importent comment: 'a' needs to be an odd matrix
FluInfectionProbability=0.2
#functions
def printMatrix(a):
    '''the function gets a matrix and prints the matrix's rows'''
    for i in range(len(a)):
        print(a[i])

def getNew_matrix(n):
    '''the function gets a matrix and returns a new matrix in the selected size (n*n).
    getNew_matrix(5) -->
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]'''
    a=[]
    for i in range(n):
        b=[]
        for j in range(n):
            b.append(0)
        a.append(b)
    return a

def getFirstVirus_plusPerson(a):  #not necessary
    '''the function gets a matrix, chooses one sick person place and one healthy person place and put them in the matrix.
    getFirstVirus_plusPerson(matrix) -->
    [0, 0, 0, 0, 0]
    [0, 0, 2, 0, 0]
    [0, 0, 1, 0, 0]
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]'''
    xhp,yhp=random.randint(0,len(a)-1),random.randint(0,len(a)-1)  #healthy person place
    xr,yr=random.randint(0,len(a)-1),random.randint(0,len(a)-1)    #sick person place
    while(xr==xhp and yr==yhp):   #while the sick person place is equal to the healthy person place, the function raffles for the sick person new place in the matrix
         xr,yr=random.randint(0,len(a)-1),random.randint(0,len(a)-1)  #new sick person place
    a[xr][yr]=2   #put sick person in the matrix(2)
    a[xhp][yhp]=1  #put healthy person in the matrix(1)
    return a

def no_healthy_people(a):
    '''the function gets a matrix and returns false if there is at least one healthy person and returns true if there is no healthy person in the matrix.
    no_healthy_people(matrix)
    [0, 0, 0, 0, 0]
    [0, 0, 2, 0, 0]
    [0, 0, 1, 0, 0]
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]
    --> false  '''

    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i][j]!=2 and a[i][j]!=0 and a[i][j]!=3):  #check if there is a healthy person
                return False
    return True

def number_of_sicks(a):
    '''the function gets a matrix, counts and returns how many sick persons there are'''
    count=0
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i][j]==2):
                count+=1
    return count


def sickLocation(a):
    '''the function gets a matrix and returns a list of the positions x,y of each sick person in the matrix'''
    lsxy=[] #list of the locations of sick people
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i][j]==2): #check if it is a sick person
                cx,cy=j,i   #save the positions x,y in cx,cy
                lsxy.append((cx,cy))   #append to the list lsxy
    #print("x: "+str(cx),", y: "+str(cy))
    return lsxy

def vaccinatedLocation(a):
    '''the function gets a matrix and returns a list of the positions x,y of each vaccinated person in the matrix'''
    lsxy=[] #list of the locations of sick people
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i][j]==3): #check if it is a vaccinated person
                cx,cy=j,i   #save the positions x,y in cx,cy
                lsxy.append((cx,cy))   #append to the list lsxy
    #print("x: "+str(cx),", y: "+str(cy))
    return lsxy

def healthyLocation(a):
    '''the function gets a matrix and returns a list of the positions x,y of each healthy person in the matrix'''
    lsxy=[] #list of the locations of healthy people
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i][j]==1): #check if it is a healthy person
                cx,cy=j,i   #save the positions x,y in cx,cy
                lsxy.append((cx,cy))   #append to the list lsxy
    #print("x: "+str(cx),", y: "+str(cy))
    return lsxy

def get_the_number_of_Options_for_Moving(a,cx,cy):
    '''the function gets matrix and the position of x and y and returns the number of options for moving for each person and for each situation'''
    f=0     #extreme position in the matrix
    l=len(a)-1  #extreme position in the matrix
    moves=0
    if((cx==f or cx==l)and(cy==f or cy==l)): #if the positions of x and y are extreme positions, there are 3 options for moving
        moves=3
    else:
        if((cx==f or cx==l)or(cy==f or cy==l)): #if the position of x or y is extreme position, there are 5 options for moving
            moves=5
        else:
            moves=8  #for all the other positions of x and y there are 8 options for moving
    return moves


def chance_for_move_Situations(moves):
    '''return the chances for moving for each place
    chance_for_move_Situations(4) -->25.0'''
    return (100/moves)

def get_List_Of_Options_For_Next_Moving(a,x,y):
    '''the function gets matrix and the positions of x and y and returns a list for all the next positions
    of x and y'''
    #comment: the examples in the parenthesis are for a matrix in size(5*5)
    #3 moves
    op1=[(x+1,y),(x,y+1),(x+1,y+1)] #start_position(0,0)
    op2=[(x-1,y),(x-1,y+1),(x,y+1)] #start_position(4,0)
    op3=[(x+1,y),(x,y-1),(x+1,y-1)] #start_position(0,4)
    op4=[(x-1,y),(x,y-1),(x-1,y-1)] #start_position(4,4)

    #5 moves
    op5=[(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1)] #start_position(x=0 , y!=0,4)
    op6=[(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1)] #start_position(x=4 , y!=0,4)
    op7=[(x-1,y),(x-1,y+1),(x,y+1),(x+1,y),(x+1,y+1)] #start_position(y=0 , x!=0,4)
    op8=[(x-1,y-1),(x-1,y),(x,y-1),(x+1,y-1),(x+1,y)] #start_position(y=4 , x!=0,4)

    #8 moves
    op9=[(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y)] #start_position(all the other positions)

    f=0  #extreme position in the matrix
    l=len(a)-1  #extreme position in the matrix
    moves=get_the_number_of_Options_for_Moving(a,x,y) #the number of options for moving, using the function "get_the_number_of_Options_for_Moving"
    #for each person by his "moves" and his positions x and y, the function returns a list of the his next positions
    if(moves==3):
        if(x==f and y==f):
            return op1
        if(x==l and y==f):
            return op2
        if(x==f and y==l):
            return op3
        if(x==l and y==l):
            return op4
    if(moves==5):
        if(x==f):
            return op5
        if(x==l):
            return op6
        if(y==f):
            return op7
        if(y==l):
            return op8
    return op9

def check_And_return_the_new_position_for_sick(list_of_options,a,cx,cy):
    '''the function gets matrix and list which is for the options for moving for a sick person, the function chooses free place to move and checks if there     is no sick person there and returns the next position'''
    i=0
    length=len(list_of_options)  #the length of the list
    choice=random.randint(0,length-1)  #random choice from "list_of_options"
    x,y=list_of_options[choice]   #x,y from "list_of_options"
    nextx, nexty = x, y
    while(a[y][x]==2):  #check if there is no sick person there
        i+=1  #counts all the wrong choices
        list_of_options.remove(list_of_options[choice])  #remove the current random choice because sick person can't move to a place where another sick person existing
        length = len(list_of_options)  #new value for the length of the list
        if (length == 0):  # if no place was found keep the same place
            return cx, cy
        choice=random.randint(0,length-1)  #random choice from "list_of_options"
        x,y=list_of_options[choice]   #x,y from "list_of_options"
        nextx, nexty = x, y

    return nextx,nexty

def check_And_return_the_new_position_for_vaccinated(list_of_options,a,cx,cy):
    '''the function gets matrix and list which is for the options for moving for a vaccinated person, the function chooses free place to move and checks if there is no vaccinated person there and returns the next position'''
    i=0
    length=len(list_of_options)  #the length of the list
    choice=random.randint(0,length-1)  #random choice from "list_of_options"
    x,y=list_of_options[choice]   #x,y from "list_of_options"
    nextx, nexty = x, y
    while(a[y][x]==3):  #check if there is no vaccinated person there
        i+=1  #counts all the wrong choices
        list_of_options.remove(list_of_options[choice])  #remove the current random choice because vaccinated person can't move to a place where another vaccinated person existing
        length = len(list_of_options)  #new value for the length of the list
        if (length == 0):  # if no place was found keep the same place
            return cx, cy
        choice=random.randint(0,length-1)  #random choice from "list_of_options"
        x,y=list_of_options[choice]   #x,y from "list_of_options"
        nextx, nexty = x, y

    return nextx,nexty

def check_And_return_the_new_position_for_healthy(list_of_options,a,cx,cy):
    '''the function gets matrix and list which is for the options for moving for a healthy person, the function chooses free place to move and checks if there is no healthy or sick person there and returns the next position'''
    i=0
    length=len(list_of_options)  #the length of the list
    choice=random.randint(0,length-1)  #random choice from "list_of_options"
    x,y=list_of_options[choice]   #x,y from "list_of_options"
    nextx,nexty=x,y
    while(a[y][x]==1 or a[y][x]==2):  #check if there is no healthy or sick person there
        i+=1  #counts all the wrong choices
        list_of_options.remove(list_of_options[choice])  #remove the current random choice because healthy person can't move to a place where another healthy person existing
        length = len(list_of_options)  #new value for the length of the list
        if (length == 0):  # if no place was found keep the same place
            return cx, cy
        choice=random.randint(0,length-1)  #random choice from "list_of_options"
        x,y=list_of_options[choice]   #x,y from "list_of_options"
        nextx, nexty = x, y

    return nextx,nexty

def do_Move_for_sick(list_of_options,a,cx,cy):  #just for sick persons
    '''the function gets list which is for the options for moving for a sick person, a matrix and the current positions of x and y, the function moves the sick people '''
    nextx,nexty=check_And_return_the_new_position_for_sick(list_of_options,a,cx,cy)  #find the next positions of x and y, using the function  "check_And_return_the_new_position"
    #cx,cy=sickLocation(a)[i]    #works just for the first sick person - need to be fixed
    rn=random.random()
    if(a[nexty][nextx]==1):  #if there is a healthy person in the next move
        if(rn<=FluInfectionProbability):  #check if the random number is lower than the flu infection probability
            a[nexty][nextx] = 2
    if(a[nexty][nextx]==0):  #if there is no one in the next move
        a[cy][cx]=0
        a[nexty][nextx]=2
    if(a[nexty][nextx]==3):  #if there is a vaccinated person in the next move
        a[cy][cx]=3
        a[nexty][nextx]=2

def do_Move_for_vaccinated(list_of_options,a,cx,cy):  #just for sick persons
    '''the function gets list which is for the options for moving for a vaccinated person, a matrix and the current positions of x and y, the function moves the vaccinated people '''
    nextx,nexty=check_And_return_the_new_position_for_vaccinated(list_of_options,a,cx,cy)  #find the next positions of x and y, using the function  "check_And_return_the_new_position"
    #cx,cy=sickLocation(a)[i]    #works just for the first sick person - need to be fixed
    if(a[nexty][nextx]==1):  #if there is a healthy person in the next move
        a[cy][cx]=1
        a[nexty][nextx]=3
    if(a[nexty][nextx]==0):  #if there is no one in the next move
        a[cy][cx]=0
        a[nexty][nextx]=3
    if(a[nexty][nextx]==2):  #if there is a sick person in the next move
        a[cy][cx]=2
        a[nexty][nextx]=3

def do_Move_for_healthy(list_of_options,a,cx,cy):  #just for sick persons
    '''the function gets list which is for the options for moving for a healthy person, a matrix and the current positions of x and y, the function moves the healthy people '''
    nextx,nexty=check_And_return_the_new_position_for_healthy(list_of_options,a,cx,cy)  #find the next positions of x and y, using the function  "check_And_return_the_new_position"
    #cx,cy=sickLocation(a)[i]    #works just for the first sick person - need to be fixed
    if(a[nexty][nextx]==3):  #if there is a vaccinated person in the next move
        a[cy][cx]=3
        a[nexty][nextx]=1
    if(a[nexty][nextx]==0):  #if there is no one in the next move
        a[cy][cx]=0
        a[nexty][nextx]=1

def addSickPerson(a):
    '''the function puts a sick person in a random free place'''
    xr, yr = random.randint(0, len(a) - 1), random.randint(0, len(a) - 1)  #random choose for place
    while ((a[yr][xr]==1) or (a[yr][xr]==2) or (a[yr][xr]==3)):  #while somebody existing in the same place like the sick person, the function choose another random place    until this place is free
        xr, yr = random.randint(0, len(a) - 1), random.randint(0, len(a) - 1)  #random choose for place
    a[yr][xr] = 2  #puts a sick person in a random free place

def addHealthyPerson(a):
    '''the function puts a healthy person in a random free place'''
    xr, yr = random.randint(0, len(a) - 1), random.randint(0, len(a) - 1)   #random choose for place
    while ((a[yr][xr]==1) or (a[yr][xr]==2) or (a[yr][xr]==3)):  #while somebody existing in the same place like the healthy person, the function choose another random place until this place is free
        xr, yr = random.randint(0, len(a) - 1),random.randint(0, len(a) - 1)   #random choose for place
    a[yr][xr] = 1  #puts a healthy person in a random free place

def addVaccinatedPerson(a):
    '''the function puts a vaccinated person in a random free place'''
    xr, yr = random.randint(0, len(a) - 1), random.randint(0, len(a) - 1)   #random choose for place
    while ((a[yr][xr]==1) or (a[yr][xr]==2) or (a[yr][xr]==3)):  #while somebody existing in the same place like the healthy person, the function choose another random place until this place is free
        xr, yr = random.randint(0, len(a) - 1), random.randint(0, len(a) - 1)   #random choose for place
    a[yr][xr] = 3  #puts a healthy person in a random free place

movie_list=[]
xtimes=[]
ysicks=[]
xratio=[]
yratio=[]
times=0
m=getNew_matrix(5)
#printMatrix(getFirstVirus_plusPerson(m))
people_number=int(input("Enter people number"))
percent_vaccinated=0.3
viruses_number=int(input("Enter viruses number"))
for h in range(int(((people_number-viruses_number)*(1-percent_vaccinated)))):
    addHealthyPerson(m)

for s in range(viruses_number):
    addSickPerson(m)

for v in range(int((people_number-viruses_number)*percent_vaccinated)):
    addVaccinatedPerson(m)
printMatrix(m)
print()


sick_number_change=0  #for graph
start_number_of_sicks=number_of_sicks(m) #for graph
while(not(no_healthy_people(m))):
    before_sick_number=number_of_sicks(m) #for graph
    ms=copy.deepcopy(m) #for video
    movie_list.append(ms) #for video
    sicklist=sickLocation(m)
    xtimes.append(times) #for graph
    ysicks.append(number_of_sicks(m)) #for graph
    yratio.append(sick_number_change) #for graph
    print(sick_number_change)
    xratio.append(number_of_sicks(m)/(start_number_of_sicks+int(((people_number-viruses_number)*(1-percent_vaccinated))))) #for graph
    print(number_of_sicks(m)/(start_number_of_sicks+int(((people_number-viruses_number)*(1-percent_vaccinated)))))
    times+=1
    for i in range(len(sicklist)):
        x,y=sicklist[i]
        #print(chance_for_move_Situations(get_the_number_of_Options_for_Moving(m, x, y)))
        #print(x,y)
        opt=get_List_Of_Options_For_Next_Moving(m,x,y)
        #print(opt)
        do_Move_for_sick(opt,m,x,y)
    vaccinatedlist = vaccinatedLocation(m)
    for i in range(len(vaccinatedlist)):
        x,y=vaccinatedlist[i]
        #print(chance_for_move_Situations(get_the_number_of_Options_for_Moving(m, x, y)))
        #print(x,y)
        opt=get_List_Of_Options_For_Next_Moving(m,x,y)
        #print(opt)
        do_Move_for_vaccinated(opt,m,x,y)
    healthylist=healthyLocation(m)
    for i in range(len(healthylist)):
        x,y=healthylist[i]
        opt=get_List_Of_Options_For_Next_Moving(m,x,y)
        #print(opt)
        do_Move_for_healthy(opt,m,x,y)
    printMatrix(m)
    sick_number_change=number_of_sicks(m)-before_sick_number
    print()


ms=copy.deepcopy(m)
movie_list.append(ms)
print(times)
