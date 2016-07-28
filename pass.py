def passwordGenerator(str1,n):
	    lent=len(str1)	
            
            
	    
	    if(lent==n):
                    print str1 
		    
            
	    if(lent<n):
		    for each in alphalist:
			    passwordGenerator(str1+each,n)
                    
			
	



alphalist=[]
for each in range(97,123):
    alphalist.append(str(chr(each)))

for each in range(0,10):
    alphalist.append(str((each)))
    
password=[]
for each in alphalist:
    passwordGenerator(each ,4) # number of charachters here 4
    



