#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Fri May 20 14:57:03 2016
@author: Tony
"""

import csv
import random

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Method using Class

class Book(object):

    def __init__(self):
        self.csvfile = r'C:\Users\Tony\Desktop\Data sets\Books.csv'
       

    def what_book(self):
        
      
      with open(r'C:\Users\Tony\Desktop\Data sets\Books.csv', 'rt') as f:
          reader = csv.DictReader(f)
          rows = [row for row in reader if row['status'] == 'to read'.lower()]
          x = ''        
          for row in rows:
              x = x + row['title']+ ' ' + 'by' + ' ' + row['author']+'\n'+'\n'
          return random.choice(x)          
          f.close()
      #def new_book(self, book):
          
          
# Initiating the Class
NextBook = Book()

if __name__ == '__main__':
  while True:
    user_input = input("Do you need a book recommendation? Yes or no: ").lower()
    if user_input == 'yes':  
        print(NextBook.what_book())
        
    elif user_input == 'no':
        break
    
    #if user_input in NextBook.day_dict.keys():
        #print(NextBook.what_book())
    elif user_input == 'end'.lower():
        break

    else:
      print()  
      print("Let's try something else, shall we?")
      print()
      
      
      
      