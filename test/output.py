'''
>>>  INFO  Created test/.testDB, as Database not exist                                                     09:57 AM
>>>  INFO  Using shop.json as default table                                                                09:57 AM
>>>  INFO  Created test/.testDB\shop.json as it does not exist                                             09:57 AM
>>>  DONE  Inserted spare1 sucessfully                                                                     09:57 AM
>>>  DONE  Inserted spare2 sucessfully                                                                     09:57 AM
>>>  DONE  Inserted spare3 sucessfully                                                                     09:57 AM
>>>  DONE  Inserted spare4 sucessfully                                                                     09:57 AM
>>>  DONE  Inserted spare5 sucessfully                                                                     09:57 AM
>>> test/.testDB 

>>> {'id': 'p1', 'name': 'Laptop', 'category': 'Electronics', 'price': 1200}

>>> Laptop

>>> {'spare1': {'id': 'p1', 'name': 'Laptop', 'category': 'Electronics', 'price': 1200}, 'spare2': {'id': 'p2', 'name': 'Smartphone', 'category': 'Electronics', 'price': 800}, 'spare3': {'id': 'p3', 'name': 'Chair', 'category': 'Furniture', 'price': 150}, 'spare4': {'id': 'p4', 'name': 'Desk', 'category': 'Furniture', 'price': 200}, 'spare5': {'id': 'p5', 'name': 'Headphones', 'category': 'Electronics', 'price': 150}}

>>>   DONE  Updated Value                                                                                   09:57 AM
>>> Updated spare1
>>>  {'id': 'p1', 'name': 'Gaming Laptop', 'category': 'Electronics', 'price': 2200}

>>>  DONE  spare1 deleted from test/.testDB\shop.json                                                      09:57 AM
>>> Deleted spare1
>>> None


>>> --------------------
>>> Query Operators

>>>  DONE  shop.json archived                                                                              09:57 AM
>>> Archived

>>>  DONE  shop.json unarchived                                                                            09:57 AM
>>> Unarchived

>>> Furniture Items:
>>>  [{'id': 'p3', 'name': 'Chair', 'category': 'Furniture', 'price': 150}, {'id': 'p4', 'name': 'Desk', 'category': 'Furniture', 'price': 200}]

>>> Electronics priced >= 500:
>>>  [{'id': 'p2', 'name': 'Smartphone', 'category': 'Electronics', 'price': 800}]

>>> Desk or priced 150:
>>>  [{'id': 'p3', 'name': 'Chair', 'category': 'Furniture', 'price': 150}, {'id': 'p5', 'name': 'Headphones', 'category': 'Electronics', 'price': 150}]

>>> Drop table? (y/n) n

'''