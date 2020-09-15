def intersection(arrays):
    cache = {}

    # get the length of the arrays
    num_arrays = len(arrays)

    # This is a list to store the intersection values
    result = []

    # Then want to count the occurrences and save to cache
    # for each list in arrays
    for lst in arrays:
        # The we want to loop through each element in list
        for element in lst:
            # add the element to the cache 
            # if it's not there as the key 
            if element not in cache:
                cache[element] = 1
            else:
                # if the element is already in cache, icrement it's count by 1
                cache[element] += 1
                # check if the element count reach the total number of lists 
                # if the answer is yes, then add the number in the result list 
                if cache[element] == num_arrays:
                    result.append(element)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
