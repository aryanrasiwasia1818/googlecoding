print "Hello World !"
i=0 
j=12

for i in range(1,13):
   for  j in range ( 1, 10 ):
      print str(i) + " X " + str(j) + " = " , i*j

if j * 12 > 100:
   print "12 X j is greater than 100"
else:
   print "12*j is less than 100"


print i+j
