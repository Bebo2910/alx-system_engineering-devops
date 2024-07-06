#!/usr/bin/python3

def find_peak(lst):
    start = 0 
    end = len(lst) - 1
    while start <= end:
        mid = int(start + (end - start) /2)
        if mid == 0 or mid == len(lst) - 1:
            return lst[mid]
        elif lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return lst[mid]
        elif lst[mid] <= lst[mid + 1]:
            start = mid + 1
        elif lst[mid] >= lst[mid + 1]:
            end = mid - 1
