from typing import List

def sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        idx_min = None 
        for j in range(i, len(arr)):
            if idx_min is None or arr[j] < arr[idx_min]:
                idx_min = j
        
        arr[i], arr[idx_min] = arr[idx_min], arr[i]
