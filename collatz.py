def collatz(number):
    collatz_list=list() #list to store the values of sequence
    
    while (number!=1) :
        collatz_list.append(number) 
        #if number is even
        if (number%2==0) :
            number=number//2
        else:
          #if number is odd
            number=(3*number)+1
    collatz_list.append(1)  #print 1 in the end   
    l=len(collatz_list)

    print("The length of collatz sequence is", l)
    print("The sequence is :")
    for i in range(0,l):
      print(collatz_list[i])

#driver code  
collatz(20)
