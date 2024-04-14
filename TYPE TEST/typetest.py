from time import time

def tperror(prompt):
    global inwords
    
    words = prompt.split()
    error = 0
    
    for i in range(len(inwords)):
        if i in (0,len(inwords)-1):
            if inwords[i] == words[i]:
               continue
            else:
               error = error + 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1] == words[i+1])  & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    error += 1
            else:
                error += 1
        return error

def speed(inprompt, stime , etime):
    global time
    global inwords
    
    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time
    
    return speed

def elapsedtime(stime,etime):    
    time = etime - stime
    return time

if __name__== '__main__':
       prompt ="hello my name is himanshu singh"   
       # in the prompt section enter the paragraph u want to test your type test on
       print("Type this :-",prompt," ")      
       input("Press Enter when you are ready to check your speed !!") 
       
       stime = time()
       inprompt = input()
       etime = time()
       
       time = round(elapsedtime(stime,etime),2)
       speed = speed(inprompt,stime,etime)
       errors = tperror(prompt)
       
       print("Total time elapsed :",time, "seconds")
       print("Your Average Typing Speed was",speed,"words per minute(w/m)")
       print("with a total of ",errors,"errors")
       
       
       
       
       
       
                     