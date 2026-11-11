data={
    'praveen':{'status':True,'python':96,'mysql':95,'fastapi':93},
    'krishna':{'status':True,'python':86,'mysql':75,'fastapi':73},
    'eshwar':{'status':True,'python':56,'mysql':65,'fastapi':63},
    'surya':{'status':True,'python':46,'mysql':45,'fastapi':43},
    'raghu':{'status':True,'python':26,'mysql':25,'fastapi':33},
    'abdul':{'status':False,'python':None,'mysql':None,'fastapi':None},

}
name=input("Enter the name: ")
if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['mysql']+data[name]['fastapi']
        avg=total/3
        if avg>80:
            print(f'{name}, congrats you got first grade')
        elif avg>60:
            print(f'{name}, Good workhard')
        elif avg>40:
            print(f'{name},better luck for the next time')
        elif avg>35:
            print(f'{name}, you just passed')
        else:
            print(f'{name},you failed in exam,bring your parents')
    else:
        print(f"{name},didn't attend the exam.Bring your parents")
        
else:
    print(f'{name} not found in data')
