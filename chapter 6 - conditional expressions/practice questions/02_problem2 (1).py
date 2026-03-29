a1=int(input("Enter Marks of Subject 1: "))
a2=int(input("Enter Marks of Subject 2: "))
a3=int(input("Enter Marks of Subject 3: "))
a4=int(input("Enter the maximum marks of each subject: "))
a5=3*a4  #Total maximum marks that can be obtained by all adding all three subjects
a1p=(a1/a4)*100
a2p=(a2/a4)*100
a3p=(a3/a4)*100
atp=(a1+a2+a3)/a5*100

if(a1p>=33 and a2p>=33 and a3p>=33 and atp>=40):
    print("Congratulations! You have succesfully the exam")
else:
    print("You Are Failed")

