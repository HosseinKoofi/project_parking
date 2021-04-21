# Function Vehicle type and validation for VEHICLE TYPE

def typofveh():
    
    while True:
        
        data['vehicle']= input('Enter type of vehicle? Car, Truck or Bus: ' ).lower()
        
        if data['vehicle'] in ('car', 'truck', 'bus'):
            break
        else:
            print('Invalid data. Try again')
        


# Function & validation for driving in HOUR

def drivingInHour():
    
    while True: 
        
        data['in_hour'] = int(input('Enter the hour vehicle entered lot: '))
        
        if data['in_hour'] >= 8 and data['in_hour'] <= 24:
            break
        else:
            print('The parking lot is closed between 24:00 to 08:00')

 
# Data validation for driving in MINUTE

def drivingInMin():
    
    while True:
        
        data['in_min']= int(input('Enter the minute vehicle entered lot: '))
        
        if data['in_min'] >= 0 and data['in_min'] <= 59:
            break
        else:
            print('Invalid time! Try again')

    
# Data validation for driving out HOUR

def drivingOutHour():
    
    while True:
    
        data['out_hour'] = int(input('Enter the hour vehicle left lot: '))
        
        if data['out_hour'] > 8 and data['out_hour'] <= 24 and data['out_hour'] > data['in_hour']:
            break
        else:
            print('Invalid time! Try again!')

    

# Data validation for driving out MINUTE

def drivingOutMin():
    
    while True:
        
        data['out_min'] = int(input('Enter the minute vehicle left lot: '))
        
        if  data['out_min'] >= 0 and data['out_min'] <= 59:
            break
        else:
            print('Invalid time! Try again')



################# Calculation of total time #################
    
def caculation():
    
    data['tot_Hours'] = data['out_hour'] - data['in_hour']
            
    data['tot_min'] = data['out_min'] - data['in_min']
            
    
    if data['tot_min'] < 0 :       
        
        data['tot_min'] =  60 - abs(data['tot_min'])
        data['tot_Hours'] = data['tot_Hours'] - 1
        data['round_total'] = data['tot_Hours'] + 1

    elif data['tot_min'] > 0:
        
        data['round_total'] = data['tot_Hours'] + 1
      
        
    elif data['tot_min'] == 0:
        data['round_total'] = data['tot_Hours']
    

################# End of total time calcultion #############    
    
    
################## Calculation of fee ######################

    
def fee():
    
# Fee calculation for car        
    if data['vehicle'] == 'car':
    
        if data['tot_Hours'] <= 3:
            data['fee'] = 0
    
        elif data['tot_Hours'] > 3:
            data['fee'] = (data['tot_Hours'] - 3) * 1.5               
# Fee calculation for truck

    elif data['vehicle'] == 'truck':
    
        if data['tot_Hours'] <= 2:
            data['fee'] = data['tot_Hours'] * 1
    
        elif data['tot_Hours'] > 2:
            data['fee'] = (data['tot_Hours'] - 2) * 2.3  + 2

# Fee calculation for bus

    elif data['vehicle'] == 'bus':
    
        if data['tot_Hours'] <= 1:
            data['fee'] = float(2)
    
        elif data['tot_Hours'] > 1:
            data['fee'] = ( (data['tot_Hours'] - 1) * 3.7 ) + 2
                   
        
                   
        
####################### PRINTING THE CHARGE############################
def print_bill():
    
    # local vari
    res = f'''
    
    \t\tPARKING LOT CHARGES
    
    Type of Vehicle: {data['vehicle']}
    TIME IN: {data['in_hour']}:{data['in_min']}
    TIME OUT:  {data['out_hour']}: {data['out_min']}
    PARKING TIME: {data['tot_Hours']}:{data['tot_min']}
    ROUNDED HOURS: {data['round_total']}
    TOTAL CHARGES: ${data['fee']}
    
    '''


    print(res)
    
    return res
        
######################################################################

def file(text):


    with open('info.txt', 'a') as f:
        
        f.write(text)
        




#############DATA VALIDATION TO TEMRMINATE OR NOT#################
    
 

flag ='yes'

while flag == 'yes':
    
    data = {}
################Fucntion calls
    typofveh()
    drivingInHour()
    drivingInMin()
    drivingOutHour()
    drivingOutMin()
    caculation()
    fee()
    
    con = print_bill()
    
    file(con)
    
    
    flag = input('Do you want to continue? Yes or No?').lower()
  
    
