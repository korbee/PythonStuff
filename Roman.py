sym_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
value_list = [1,5,10,50,100,500,1000]
def transform_roman_to_values(roman_string):
    this_value_list = []
    for symbol in roman_string:
        if symbol not in sym_list:
            raise Exception('Roman symbol does not exist')
        this_value = value_list[sym_list.index(symbol)]
        this_value_list.append(this_value)
    return this_value_list
    
def transform_values_to_total(roman_values):

    accum_list = [roman_values[0]]
    last_val = roman_values[0]
    total_value = 0
    equal_count = 1
    i = 1
    while i < len(roman_values):
        print('Current index', i)
        print('Last value:', last_val)
        if len(accum_list) > 3:
            raise Exception('More than 3 same letters in a row')
        if last_val == roman_values[i]:
            accum_list.append(roman_values[i])
            print('Same as last, appending', accum_list, total_value)
            print(accum_list)
        else:
            print('Not same')
            if last_val < roman_values[i]:
                print('Current is greater, subtracting list from current ', end='')
                if len(accum_list) > 1:
                    raise Exception('More than 2 letters in a row before a greater letter')
                total_value += roman_values[i] - sum(accum_list)
                print(roman_values[i],'-', sum(accum_list), '=', total_value)
            else:
                print('Current is lower, adding total of accumulated')
                total_value += sum(accum_list) + roman_values[i]
            accum_list=list()
            remaining_elements = len(roman_values) - (i+1)
            if remaining_elements >= 1:
                if remaining_elements >= 2:
                    last_val = roman_values[i+1]
                    accum_list.append(last_val)
                    i += 1
                else:
                    total_value += roman_values[i+1]
                    break
            else:
                break
        i += 1
    total_value += sum(accum_list)
    accum_list = list()
    return total_value

input_roman = 'INSERT ROMAN NUMERALS HERE'
roman_values = transform_roman_to_values(input_roman)
print(roman_values)
final_result = transform_values_to_total(roman_values)
print(final_result)