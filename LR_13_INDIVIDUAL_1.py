from datetime import datetime
from datetime import date
import pickle
import unittest
from unittest import TestCase, main

class Department():
    def __init__(self, department_name, num_of_counters, num_of_sellers, hall_num):
        self.department_name = department_name
        self.num_of_counters = num_of_counters
        self.num_of_sellers = num_of_sellers
        self.hall_num = hall_num
        self.dep_hist = []
        
    def hire_a_new_saller(self):
        self.num_of_sellers += 1
        self.dep_hist.append('{datetime.now()} Кол-во сотрудников стало: {self.num_of_sellers}')
        
    def fire_the_seller(self):
        self.num_of_sellers -= 1
        self.dep_hist.append('{datetime.now()} Кол-во сотрудников стало: {self.num_of_sellers}')
        
    def __del__(self):
        with open('department.txt', 'a') as f:
            f.write('department_name {0} : num_of_counters {1} : num_of_sellers {2} : hall_num {3} \n'.format(self.department_name, self.num_of_counters, self.num_of_sellers, self.hall_num))
            self.dep_hist.append(f'{datetime.now()} объект удалён')
        
class Customers():
    def __init__(self, customer_name,  customer_address, customer_payment_type):
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.payment_type = customer_payment_type
        self.cust_hist = []
        
    def change_customer_payment_type(self):
        self.customer_payment_type = input()
        self.cust_hist.append('{datetime.now()} Способ оплаты клиента стал: {self.customer_payment_type}')
        
    def __del__(self):
        with open('customers.txt', 'a') as s:
            s.write('customer_name {0} :  customer_address {1} : customer_payment_type {2} \n'.format(self.customer_name,  self.customer_address, self.customer_payment_type))
            self.cust_hist.append('{datetime.now()} объект удалён')

class Provider():
    def __init__(self, provider_name, provider_address, country, transport_type, provider_payment_type):
        self.provider_name = provider_name
        self.provider_address = provider_address
        self.country = country
        self.transport_type = transport_type
        self.provider_payment_type = provider_payment_type
        self.provider_hist = []
        
    def change_povider_transport_type(self):
        self.transport_type = str(input())
        self.provider_hist.append('{datetime.now()} Вид транспорта поставщика стал: {self.transport_type}')
        
    def __del__(self):
        with open('provider.txt', 'a') as h:
            s.write('provider_name {0} :  provider_address {1} : country {2} : transport_type {3} : provider_payment_type {4} \n'.format(self.provider_name, self.provider_address, self.country, self.transport_type, self.provider_payment_type))
            self.provider_hist.append('{datetime.now} объект удалён')
            
class Product():
    def __init__(self, product_name, department, provider, storage_conditions, storage_periods):
        self.product_name = product_name
        self.department = department
        self.provider = provider
        self.storage_conditions = storage_conditions
        self.storage_periods = storage_periods
        self.product_hist = []
        
    def change_povider(self):
        self.provider = str(input())
        self.product_hist.append('{datetime.now()} Поставщиком стал: {self.provider}')
        
    def __del__(self):
        with open('product.txt', 'a') as h:
            h.write('product_name {0} :  department {1} : provider {2} : storage_conditions {3} : storage_periods {4} \n'.format(self.product_name, self.department, self.provider, self.storage_conditions, self.storage_periods))
            self.product_hist.append('{datetime.now()} объект удалён')

class PerishableProduct(Product):
    def __init__(self, product_name, department, provider, storage_conditions, storage_periods, prod_date, best_before_date):
        super(PerishableProduct, self).__init__(product_name, department, provider, storage_conditions, storage_periods)
        self.prod_date = prod_date
        self.best_before_date = best_before_date
    
    def expired(self):
        d = date.today()
        if d == self.best_before_date:
            print('У товара истёк срок годности!!!')
            
    def del_expired(self, __del__):
        x = input('Списать товар с истёкшим сроком годности? Введите 1, если да, 0 если нет')
        if x == 1:
            pass

class ExcisableProduct(Product):
    def __init__(self, product_name, department, provider, storage_conditions, storage_periods, excise_num, customer_age):
        super(ExcisableProduct).__init__(product_name, department, provider, storage_conditions, storage_periods)
        self.excise_num = excise_num
        self.customer_age = customer_age
        
    def ExcisableProductSell(self):
        if int(self.customer_age) < 18:
            print('Продажа запрещена, покупатель несовершеннолетний!')

class Product_Sell():
    def __init__(self, customer, product, date, time, amount, price, summa):
        self.customer = customer
        self.product = product
        self.date = date
        self.time = time
        self.amount = amount
        self.price = price
        self.summa = summa
        self.product_sell_hist = []
        
    def __del__(self):
        with open('product_sell.txt', 'a') as h:
            s.write('customer {0} :  product {1} : date {2} : time {3} : amount {4} : price {5} : summa {6} \n'.format(self.customer, self.product, self.date, self.time, self.amount, self.price, self.summa))
            self.product_hist.append('{datetime.now()} объект удалён')
        
    def add_sale(self, price, amount ):
        sale = int(input())
        self.price = price - ((price / 100) * sale)
        self.summa = amount * self.price
        print(self.price, self.summa)
        self.product_hist.append('{datetime.now()} Скидка составила {sale}, Цена со скидкой стала {self.price}, Сумма всего купленного товара со скидкой составила {self.summa}')

class ser(object):
    @staticmethod
    def serialize(departmen):
        with open('departmen.pkl', 'wb') as f:
            pickle.dump(departmen, f)
        f.closed

    @staticmethod
    def deserialize():
        with open('departmen.pkl', 'rb') as f:
            departmen = pickle.load(f)
        f.closed
        return departmen
