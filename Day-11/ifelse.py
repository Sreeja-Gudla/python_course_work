"""data=('sri@gmail.com','sri23')
gmail=input("Enter the mail:")
password=input("Enter the password:")
if(gmail,password)==data:
    print("Login Successfull")
else:
    print("Invalid Login")"""


"""seats={
    "s1":"Booked",
    "s2":"Available",
    "s3":"Booked",
    "s4":"Available",
    "s5":"Available",
    "s6":"Available"
}
seatno=input("Enter the seat no: ")
if seatno in seats and seats[seatno]=="Available":
    seats[seatno]="Booked"
    print(f'{seatno} is booked successfully')
    print(seats)
else:
    print(f'{seatno} is already booked')"""



products={
    'laptop':{'price':40000,'stock':10},
    'mouse':{'price':400,'stock':0},
    'keyboard':{'price':2000,'stock':3},
    'tab':{'price':20000,'stock':5},
    'mobile':{'price':60000,'stock':7}
}
search=input("Enter the product: ")
if search in products and products[search]['stock']:
    print(f"you can buy {search} at the price: Rs{products[search]['price']}")
else:
    print(f'{search} is not available')