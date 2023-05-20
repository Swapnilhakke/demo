n=int(input())

proname=list(map(str,input().split()))
proprice=list(map(int,input().split()))

shop={}
for i in range(n):
    shop[proname[i]]=proprice[i]

cbuy=int(input())
cproname=list(map(str,input().split()))
cproq=list(map(int,input().split()))
buy={}
for i in range(cbuy):
    buy[cproname[i]]=cproq[i]

total=0
for key in buy.keys():
    total+=(buy[key]*shop[key])

if(total>500):
    print(total-total*(25/100))
else:
    print(total-500*(10/100))