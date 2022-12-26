#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":

    a = {1: "sova", 2 :"sich", 3: "mouse"}
    print(a)
    print(a[1])
    print(type(a[1]))
    
    print("Введите путь к файлу")
    
    f = input()
    
    with open(f, "r", encoding = "utf-8") as test:
        b = [f for line in test for f in line.split()]
        
    print(b)
    print(b[0])
    print(type(b[0]))
        
    i = 0
        
    while i < len(b):
        q = b[i]
        print(b[i])
        print(type(b[i]))
            
        if a[1] == q.lower() or a[2] == q.lower() or a[3] == q.lower():
            print("Слово не имеет ошибок")
        else:
            print("В слове ошибка или его нет в списке")
        i = i + 1
