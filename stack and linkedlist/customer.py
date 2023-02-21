import datetime

class Customer:
    def __init__(self, id, name, date, amount):
        self.id = id
        self.name = name
        self.date = datetime.datetime.strptime(date, '%d/%m/%y')
        self.amount = amount
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None

    def add_customer(self, id, name, date, amount):
        new_customer = Customer(id, name, date, amount)
        if self.head is None:
            self.head = new_customer
        else:
            current = self.head
            while current:
                if current.amount >= new_customer.amount:
                    if current == self.head:
                        new_customer.next = self.head
                        self.head = new_customer
                    else:
                        new_customer.next = current
                        previous.next = new_customer
                    break
                elif current.next is None:
                    current.next = new_customer
                    break
                previous = current
                current = current.next


    def view_all_customers(self):
        current = self.head
        while current:
            print(f'Customer ID: {current.id}')
            print(f'Customer Name: {current.name}')
            print(f'Purchase Date: {current.date.strftime("%d/%m/%y")}')
            print(f'Bill Amount: {current.amount}')
            print()
            current = current.next

    def view_total_amount(self, year):
        current = self.head
        total_amount = 0
        while current:
            if current.date.year == year:
                total_amount += current.amount
            current = current.next
        print(f'Total Purchase Amount for {year}: {total_amount}')

    def view_customer_details(self, name):
        current = self.head
        while current:
            if current.name == name:
                print(f'Customer ID: {current.id}')
                print(f'Purchase Date: {current.date.strftime("%d/%m/%y")}')
                print(f'Bill Amount: {current.amount}')
                break
            current = current.next
        else:
            print(f'{name} not found in customer list')


customer_list = LinkedList()


while True:
    print('Enter customer details (or "done" to finish):')
    id = input('Customer ID: ')
    if id == 'done':
        break
    name = input('Customer Name: ')
    date = input('Purchase Date (dd/mm/yy): ')
    amount = float(input('Bill Amount: '))
    customer_list.add_customer(int(id), name, date, amount)


customer_list.view_all_customers()


year = int(input('Enter year to view total purchase amount: '))
customer_list.view_total_amount(year)


name = input('Enter customer name to view details: ')
customer_list.view_customer_details(name)
