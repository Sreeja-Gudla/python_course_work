"""l=[12,9,3,4,5,10,3,2,4,5,2,4,5]
i=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1"""

"""bill=0
while True:
    product=input("Enter the product name(STOP): ")
    if product=='STOP':
        print("Total bill: ",bill)
        break
    price=int(input("Enter the price: "))
    quan=int(input("Enter the quantity: "))
    bill+=price*quan"""

"""bill=0
products={'sugar':20,"milk":30,"bread":40,"shampoo":100,"panner":100,"icecream":150,"chocolate":50,"curd":50,"flowers":100,"oil":200}
#it display the menu 
print("Welcome to the store".center(50,'-'))
print("Product Name",'price')
for i in products:
    print(i.ljust(12,' '),':',products[i])
#it give list of selected items and total bill
carts={}
while True:
    cart=input("Enter the product name(exit): ").lower()

    if cart=="exit":
        break
    qua=int(input("Enter the quantity: "))
    carts[cart]=qua
print("Bill".center(50,'-'))
print("Product Name Quantity (Rs)Price")
bill=0
for i in carts:
    print(i.ljust(12,' '),str(carts[i]).ljust(12,' '),products[i])
    bill+=carts[i]*products[i]
print(f'total bill: Rs{bill}')
print("Thanks for shopping")"""

##example programs from material

#E-commerce cart billing

"""l=list(map(int,input().split()))
i=0
sum=0
while i<len(l):
    sum+=l[i]
    i+=1
print(f'Total Bill = {sum}')"""

#Password Security Analyzer

"""n=input()
upper=0
lower=0
digit=0
spl_char=0
for i in n:
    if 'a'<=i<='z':
        lower+=1
    elif 'A'<=i<='Z':
        upper+=1
    elif '0'<=i<='9':
        digit+=1
    else:
        spl_char+=1
print("Uppercase: ",upper)
print("Lowercase: ",lower)
print("Digits: ",digit)
print("Special Characters: ",spl_char)"""

#Netflix Watch History

l=list(map(str,input().split()))
i=0
while i<len(l):
    print(l[i])
    i+=1
