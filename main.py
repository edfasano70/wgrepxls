import pandas as pd

clients = {'first_name': ['Oralie', 'Imojean', 'Michele', 'Ailbert', 'Stevy'],
           'last_name': ['Fidgeon', 'Benet', 'Woodlands', 'Risdale', 'MacGorman'],
           'age': [30, 21, 29, 22, 24]}

clients = pd.DataFrame(clients, columns=['first_name', 'last_name', 'age'])

# print(clients)

invoices = {'invoice_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'client_id': [3, 2, 7, 2, 7, 3, 1, 4, 2, 3, 6, 2],
            'amount': [77.91, 24.36, 74.65, 19.75, 27.46, 17.13, 45.77, 81.7, 14.41, 52.69, 32.03, 12.78]}

invoices = pd.DataFrame(
    invoices, columns=['invoice_id', 'client_id', 'amount'])

print(invoices)

new_clients = pd.DataFrame({'first_name': ['Rebe'],
                            'last_name': ['MacCrossan'],
                            'age': [21]},
                           columns=['first_name', 'last_name', 'age'])

clients = pd.concat([clients, new_clients])

clients.index = range(clients.shape[0])

ids = pd.DataFrame({'client_id': [1, 2, 3, 4, 5, 6]}, columns = ['client_id'])
clients = pd.concat([ids, clients], axis=1,)

print(clients)


