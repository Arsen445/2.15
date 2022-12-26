#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":

    a = {1: "sova", 2 :"sich", 3: "mouse"}
    print(a)
    print(a[1])
    print(type(a[1]))
    
    print("Введите путь к файлу")
    
    file = input()
    
    with open(file, "r", encoding = "utf-8") as test:
        b = [f for line in test for f in line.split()]

           
    for i in b:
        if a[1] == i.lower() or a[2] == i.lower() or a[3] == i.lower():
            print("Слово не имеет ошибок")
        else:
            print("В слове ошибка или его нет в списке")


