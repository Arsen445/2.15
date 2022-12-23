#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    
    with open("text.txt", "r", encoding="utf-8") as test:
        

        while True:
            s1 = test.readline()
            k = 0
            for i in s1:
                if i == "\"":
                    k = k + 1
            if k == 2:    
                print(s1)
            if not s1:
                break
            
     
