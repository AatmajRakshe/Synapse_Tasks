request_spending = {
    "Mahek": {
    "balance": 3000.00,
    "transactions": [
        {"amount": -9000.00, "category": "Creatives"},
        {"amount": 7000.00, "category": "Sponsor"},
        {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },
    
    "Arham": {
    "balance": 5000.00,
    "transactions": [
        {"amount": 8000.00, "category": "Stalls"},
        {"amount": 7500.00, "category": "Seminars"}
        ]
    },
    
    "Unnati": {
    "balance": 3500.00,
    "transactions": [
        {"amount": -5000.00, "category": "Attraction"},
        {"amount": 2500.00, "category": "Promo"},
        {"amount": -900.00, "category": "Lighting"}, 
        {"amount":-3000.00, "category": "Games"}
        ]
    },
    
    "Gaurang": {
    "balance": 2000.00,
    "transactions": [
        {"amount": 1500.00, "category": "Website"},
        {"amount": 1000.00, "category": "C2C"},
        {"amount": -500.00, "category": "Posters"}
        ]
    }
}
def total_spending(request_spending,account_id,category):
    if(account_id == "Gaurang"):
        if(category == 'Website'):
            cat = 0
        elif(category == 'C2C'):
            cat = 1
        elif(category == 'Posters'):
            cat = 2
        else:
            print('Invalid category')
    elif(account_id == "Unnati"):
        if(category == 'Attraction'):
            cat = 0
        elif(category == 'Seminars'):
            cat = 1
        elif(category == 'Lighting'):
            cat = 2
        elif(category == 'Games'):
            cat = 3
        else:
            print('Invalid category')
    elif(account_id == "Arham"):
        if(category == 'Stalls'):
            cat = 0
        elif(category == 'Seminars'):
            cat = 1
        else:
            print('Invalid category')
    elif(account_id == "Mahek"):
        if(category == 'Creatives'):
            cat = 0
        elif(category == 'Sponsor'):
            cat = 1
        elif(category == 'Prize-Money'):
            cat = 2
        else:
            print('Invalid category')
    print(request_spending[account_id]['transactions'][cat]['amount'])

def account_balance(request_spending, account_id):
    print(request_spending[account_id]['balance'])


def money_owed(request_spending, account_id):
    transac = request_spending[account_id]['transactions']
    # print(type(transac))
    total =0
    for i in range(len(transac)):
        total += transac[i]['amount']
    print(total)
    
total_spending(request_spending,'Gaurang','C2C')
money_owed(request_spending,"Gaurang")
