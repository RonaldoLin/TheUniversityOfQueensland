'''
Created on 1 May 2020

@author: shree
'''

from book import book as bk


def csv_loader_book1():
    try:

        with open('../data/Book1.csv', 'r') as f:
            lines = f.read().splitlines()
        if lines is None:
            print("no file.")
            return
        books = []
        for line in lines:
            line = line.replace("'", " ")
            line = line.split(',')
            book = bk()
            book.set_id(line[0])
            book.set_title(line[1])
            books.append(book)
            # print(restaurant.get_id(),',',restaurant.get_name(),',',restaurant.get_address(),',',restaurant.get_city())
        return books

    except:
        print("Error occurred. Check if file exists.")

# res_list1 = csv_loader_book1()
# print(res_list1[0].get_name())
