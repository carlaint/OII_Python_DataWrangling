#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 11:21:16 2018

@author: carla
"""

### intro and EXTENSIONS ##########
import random
import time
import sys

fruits = ["Dragon Fruit","Durian","Rambutan","Mangosteen", "Papaya", "Cherimoya","Star Fruit", "Passion Fruit", "Jack Fruit", "Soursop", "Kumquat", "Sapodilla"]
pricelist=[]
todaysfruits=[]
random.shuffle(fruits)


for i in range(0,5):
    todaysfruits.append(fruits[i])
    price=round(random.uniform(0, 2),2)
    pricelist.append(price)

#zip them together in one dict
menu = dict(zip(todaysfruits,pricelist))

print("WELCOME TO THE EXOTIC FRUIT STORE!!!")

def Start():
    print("\nOur offerings for today:")
    
    for key,val in menu.items():
        print(key, ": $", val)

    
#######
class ShoppingCart():

    def __init__(self):
        self.fruit = ''
        self.item = ''
        self.runtotal = 0
        self.runquant = 0
        self.buymore_or_checkout =''
        self.shoplist = dict()
        
    def selectItem(self,fruit):
        while True:
            try:
                self.item = menu[fruit]
                self.fruit = str(fruit)
                return
            except KeyError:
                print("Sorry, I didn't understand that")
                return False
        return
            
    def cartTotal(self,quantity):
        tot = round(self.item*int(quantity),2)
        print(quantity, self.fruit, "@ $", self.item, "= $", "%.2f" %tot)
        self.shoplist[self.fruit]=quantity, tot
        self.runtotal = round(self.runtotal+tot, 2)
        self.runquant = self.runquant+int(quantity)
        print("\nYour shopping basket:")
        for key,val in self.shoplist.items():
            print(val[0], key,": $", val[1])
        print("You have", self.runquant, "items in your basket for $", self.runtotal)
        
    def buyMore(self,buymore_or_checkout):
        while True:
            try:
                buymore_or_checkout = buymore_or_checkout.upper()
            except ValueError:
                print("Sorry, I didn't get that.")
                continue
            
            if buymore_or_checkout == "B":
                return buymore_or_checkout
            elif buymore_or_checkout == "C":
                return buymore_or_checkout
            else:
                print("Sorry, please input B or C.")
                continue
        return
            

########## defining Yes and No Functions
def YesNo(prompt):
    while True:
        try:
            value = input(prompt)
            value = value.upper()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue #in the loop#

        if value == "Y":
            return True
        elif value == "N":
            return False
        else:
            print("Sorry, please input Y or N.")
            continue #in the loop#
    return value

    
#######ASKING SELECTIONS
def Ask():
    fruit = input("What would you like to buy? ")
    fruit = sc.selectItem(fruit)
    
    while fruit==False:
        fruit = input("What would you like to buy? ")
        fruit = sc.selectItem(fruit)

########ADDING MORE ITEMS OR CHECKING OUT?
def BuyMore():    
    buymore_or_checkout = input("Would you like to [B]uy more or [C]heckout [B/C]?")
    buymore_or_checkout = sc.buyMore(buymore_or_checkout)
    if buymore_or_checkout == "B":
        Start()
        Ask()
        Add()
        return
############ EXTENSION no.2 #####################
    elif buymore_or_checkout == "C":
        print("\n\n************** Checkout counter ******************")
        name = input("Please input your name: ")
        address = input("Please input your address: ")
        print("\nWe will deliver to ", name, "with address ",address, "in 2-3 days")
        print("Thank you for shopping at the Exotic Fruitstore. Have a nice day!")
        return
        
        

#######ADDING TO BUY?
def Add():        
    addCart = YesNo("Would you like to add to shopping cart? [Y/N]")
    
    if addCart==True:
        quantity = input("How many would you like to buy? ")
        quantity = sc.cartTotal(quantity)
        BuyMore()
        
    elif addCart==False:
        exitProg= YesNo("Would you like to exit? [Y/N]")        
        if exitProg ==True:
            print("Thank you for visiting the Exotic Superstore. Good bye!")
            print("Please wait, Python is restarting....")
            time.sleep(2)
            exit()
            
        elif exitProg == False:
            Start()
            Ask()
            Add()
    else:
        print("")




    
######  SHOPPING CART PROPER ######################          
sc = ShoppingCart()

######STARTING
Start()
Ask()
Add()






        
