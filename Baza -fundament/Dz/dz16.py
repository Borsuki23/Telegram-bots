transactions = {
    '1': {
        "id": "1",
        "date": "2023-08-18 15:30:00",
        "amount": 150.75,
        "status": "completed",
        "customer": {
            "name": "John Smith",
            "email": "john@example.com",
            "phone": "123-456-7890"
        }
    },
    '2': {
        "id": "2",
        "date": "2023-08-18 10:15:00",
        "amount": 50.20,
        "status": "failed",
        "customer": {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "phone": "987-654-3210"
        }
    },
    '3': {
        "id": "3",
        "date": "2023-08-17 18:45:00",
        "amount": 200.00,
        "status": "pending",
        "customer": {
            "name": "John Smith",
            "email": "alice@example.com",
            "phone": "555-123-4567"
        }
    },
    '4': {
        "id": "4",
        "date": "2023-08-19 09:00:00",
        "amount": 75.50,
        "status": "completed",
        "customer": {
            "name": "Jane Doe",
            "email": "robert@example.com",
            "phone": "222-333-4444"
        }
    },
    '5': {
        "id": "5",
        "date": "2023-08-20 14:20:00",
        "amount": 300.25,
        "status": "completed",
        "customer": {
            "name": "John Smith",
            "email": "emily@example.com",
            "phone": "777-888-9999"
        }
    },
    '6': {
        "id": "6",
        "date": "2023-08-20 14:20:00",
        "amount": 300.25,
        "status": "completed",
        "customer": {
            "name": "John Smith",
            "email": "dasdasd@fasd.com",
            "phone": "777-888-9999"
        },
    }
}

new_transaction_data = {
    "id": "1",
    "date": "2023-08-18 15:30:00",
    "amount": 150.75,
    "status": "новий_статус",
    "customer": {
        "name": "John Smith",
        "email": "john@example.com",
        "phone": "123-456-7890"
    }
}

transactions['1'].update(new_transaction_data)
print(transactions)
for key, transaction in transactions.items():
    print(key, transaction)
transactions['3']['status'] = 'completed'
del transactions['3']
for transaction in transactions.values():
    print(transaction['id'], transaction['status'])
all_customers = {}
for transaction in transactions.values():
    if transaction['customer']['name'] not in all_customers:
        all_customers[transaction['customer']['name']] = []
    all_customers[transaction['customer']['name']].append(transaction['id'])
print(all_customers)

for customer, transactions in all_customers.items():
    print(customer, transactions)






