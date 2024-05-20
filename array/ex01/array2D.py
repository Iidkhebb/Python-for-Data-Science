def get_with(arr: list):
    max_with = 0
    for h in arr:
        max_with = len(h) if len(h) > max_with else max_with
    return max_with

def slice_me(family: list, start: int, end: int) -> list:
    max_with = get_with(family) 
    height = len(family)
    print(f'My sahpe is : ({height}, {max_with})')
    
    try:
        sliced_array = family[start:end]
        new_arr_with = get_with(sliced_array)
        new_arr_height = len(sliced_array)
        print(f'My new sahpe is : ({new_arr_height}, {new_arr_with})')
    
    except IndexError as e:
        print(e)
        return
    
    return sliced_array