def has_negatives(a):
    # result list
    result = []
    # setting up hash table dict
    my_dict = {}
    
    # for loop to loop through the list
    for p_number in a:
        # setting up p_number int in my dictionary
        my_dict[p_number] = p_number 
        
        #if number not 0 or in dictionary 
        if p_number != 0 and - p_number in my_dict:
            # retrun number as positive nymber by appending 
            result.append(abs(p_number))

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
