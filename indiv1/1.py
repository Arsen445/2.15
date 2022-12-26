#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    
    with open("text.txt", "r", encoding="utf-8") as test:
        s1 = test.readlines()
    for i in s1:
        k = 0
        for m in i:
            if m == "\"":
                k = k + 1
        if k == 2:
            print(i)
                
             

     
