# -*- coding: utf-8 -*-
"""Paccomerce.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NqM9alyPV9viL0qOUhfkYeglTzNQ4Wan
"""

# membuat tabel
from tabulate import tabulate

# square root,  digunakan di euclidean distance
from math import sqrt

from typing_extensions import dataclass_transform
class Membership:
    database_user = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }

    table_membership = {
        'Platinum' : ['Platinum', 15, 'Voucher Makan + Voucher Ojek Online + Voucher Liburan + Cashback 30%'],
        'Gold' : ['Gold', 10, 'Voucher Makan + Voucher Ojek Online'],
        'Silver' : ['Silver', 8, 'Voucher Makan']
    }

    table_requirement = {
        'Platinum' : ['Platinum', 8, 15],
        'Gold' : ['Gold', 6, 10],
        'Silver' : ['Silver', 5, 7]
    }

    def __init__(self, username):
        self.username = username
        self.database_user[username] = ""

    def check_all_membership(self):
        table = [value for key, value in self.table_membership.items()]
        header = ['Kategori', 'Diskon', 'Benefit']
        print(tabulate(table, headers=header))

    def check_requirement(self):
        table = [ value for key, value in self.table_requirement.items()]
        header = ['Kategori', 'Monthly Expense', 'Montly Income']
        print(tabulate(table, headers=header))

    def show_membership(self, username):
        if username in self.database_user.keys():
            return self.database_user[username]

    def predict_membership(self, username, monthly_expense, monthly_income):
        distance = {}

        for key, value in self.table_requirement.items():
            euclidean_distance = sqrt((monthly_expense - value[1])**2 + (monthly_income - value[2])**2)
            distance[key] = euclidean_distance

        print(f'Hasil perhitungan Euclidean Distance dari user adalah {distance}')

        # minimum

        for key, value in distance.items():
            if value == min(distance.values()):
                self.database_user[username] = key
                return key

    def calculate_bill(self, username, list_harga):
        try:
            if username in self.database_user.keys():
                member_type = self.database_user[username]
                if member_type != '':
                    diskon = self.table_membership[member_type][1]
                    calculate_bill = sum(list_harga) * (1 - diskon/100)
                    return calculate_bill
                else:
                    raise Exception(f"Silahkan melakukan predict untuk user {username}")
            else:
                raise Exception("Data user toidak ditemukan")
        except Exception as e:
            print(e)

peni = Membership("peni")
peni.predict_membership("peni",9,12)

rani = Membership("rani")
rani.calculate_bill("rani", [100_000, 120_000])

rani.show_membership("rani")

