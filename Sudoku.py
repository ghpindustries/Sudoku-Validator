'''
Quick Input===>
123456789
234567891
345678912
456789123
567891234
678912345
789123456
891234567
912345678

'''
try:a = input(),input(),input(),input(),input(),input(),input(),input(),input()
except:print('You must enter a 9x9 input')
def vert(a,num):
	x=[]
	for i in range(9):
		x+=(a[i][num])
	return ''.join(x)
b=[]
for i in range(9): b+=list(vert(a,i))+[' ']
b = ''.join(b).split()

c=[]
box1,box2,box3,box4,box5,box6,box7,box8,box9=[],[],[],[],[],[],[],[],[]
for i in range(3):box1+=(a[i][:3])
box1=''.join(box1)

for i in range(3,6):box2+=(a[i][:3])
box2=''.join(box2)

for i in range(6,9):box3+=(a[i][:3])
box3=''.join(box3)

for i in range(3):box4+=(a[i][3:6])
box4=''.join(box4)

for i in range(3,6):box5+=(a[i][3:6])
box5=''.join(box5)

for i in range(6,9):box6+=(a[i][3:6])
box6=''.join(box6)

for i in range(3):box7+=(a[i][6:])
box7=''.join(box7)

for i in range(3,6):box8+=(a[i][6:])
box8=''.join(box8)

for i in range(6,9):box9+=(a[i][6:])
box9=''.join(box9)


hc,vc,bc = 0,0,0
def horcheck(a):
    hc= 0
    for i in a:
        for j in i:
            if i.count(j)>1:
                hc = 1
                return False
                break
        if hc==1:break
    if hc==0:return True
def vercheck(a):
    vc= 0
    for i in a:
        for j in i:
            if i.count(j)>1:
                vc = 1
                return False
                break
        if vc==1:break
    if vc==0:return True
def boxcheck(a,b,c,d,e,f,g,h,j):
    bc =0
	for i in a:
		if a.count(i)>1:
           bc =1
		   return False
    if  bc ==0:
		for i in b:
			if b.count(i)>1:
	           bc =1
			   return False
    if  bc ==0:
		for i in c:
			if c.count(i)>1:
	           bc =1
			   return False
	if  bc ==0:
		for i in d:
			if d.count(i)>1:
	           bc =1
			   return False
    if  bc ==0:
		for i in e:
			if e.count(i)>1:
	           bc =1
			   return False
	if  bc ==0:
		for i in f:
			if f.count(i)>1:
	           bc =1
			   return False
    if  bc ==0:
		for i in g:
			if g.count(i)>1:
	           bc =1
			   return False
	if  bc ==0:
		for i in h:
			if h.count(i)>1:
	           bc =1
			   return False
    if  bc ==0:
		for i in j:
			if j.count(i)>1:
	           c =1
			   return False
if horcheck(a) and vercheck(b) and boxcheck(box1,box2,box3,box4,box5,box6,box7,box8,box9):
    print(True)
else:
    print(False)
