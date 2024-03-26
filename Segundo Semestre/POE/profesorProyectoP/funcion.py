import time
def hora():
    tt= (time.strftime("%H:%M:%S",time.localtime()))     
    return tt



def vrut(rut):
    r=rut
    r=r.replace(".","")
    r=r.replace("-","")
    dv=r[-1]
    r=r[0:len(r)-1]
    r=list(r)
    print(r,dv)
    s=0
    c=2
    for x in reversed(r):      
     if c==8:
       c=2
     s=s+(int(x) * c)
     print(x,c,s)
     c+=1
     
    s=11-(s%11)
    print(s,type(s))    
    if s==10:
        
       if dv.upper()=="K":
           return 1
       else:
           return 0
         
    if int(s)==11:
        print(dv,s)  
        if int(dv)==0:
           return 1
        else:
           return 0
       
    if s!=10 and s!=11:
        #print("entro",s,dv)
        if s==int(dv):
            return 1
        else:
            return 0