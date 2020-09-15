def get_indices_of_item_weights(weights, length, limit):
     
    cache = {}
    
    for index in range(length):
        #store each weight as a key
        weight = weights[index]
        if weight in cache:
            # you want to store the weight index as the value
            value = cache[weight]
            # return tuple
            return (index, value)
        # calculate the difference
        diffrence = limit - weight
        # then, you can add to the cache 
        cache[diffrence] = index

    return None

weights = [4, 6, 10, 15, 16] 
length = 5 
limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
print(get_indices_of_item_weights(weights, length, limit))
