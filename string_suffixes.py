def distance(string=None, count=None, iteration=1):
    #calculate new substring with each iteration
    sub_string = string[iteration:] 
    if sub_string:
        for index, i in enumerate(sub_string):
            #check if same character exist at the same position of original string and new substring
            if sub_string[index] == string[index]: 
                count[string] += 1
            else:
                break
        if len(sub_string)>=1:
            #recursive call to distance() for each substring
            distance(string, count, iteration=iteration+1) 
    return count
    
if __name__ == "__main__":
    from collections import defaultdict
    bucket = []
    output = []
    count = defaultdict(int)
    total_cases = raw_input("Enter total number of testcase: ")

    try:
        #If number of testcases is not number, then will throw ValueError
        for i in range(int(total_cases)): 
            bucket.append(raw_input())

        for string in bucket:
            count[string] = len(string)
            result = distance(string, count)
        output.append(result)
    except ValueError:
        print "Please enter integer for number of testcases"
        exit

    for i in output:
        for index, length in enumerate(i.values()):
            print 'Similarity of string with all substrings is \'' + bucket[index] + '\' is: ' + str(length)
                
        
