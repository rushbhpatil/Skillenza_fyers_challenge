import sys
import json
import os


def open_csv(filename):
    '''
    The csv file is just like a txt file with comma separated line.
    here we are using same logic, just open csv file as normal text file and separate the lines by comma.
    '''

    unique_airport = {}

    with open(filename, mode='r') as csv_file:
        count = 0
        for row in csv_file:
            lines = row.split(",")
            if count == 0:
                # increasing the counter
                count += 1
                continue
            #
            airpt_name = lines[1] + "," + lines[2]
            #now we should remove the extra quotes
            airpt_name = airpt_name.strip('"')
            # Add values in dict
            # If value is already present in dict then +1.
            if airpt_name not in unique_airport:
                unique_airport[airpt_name] = 1
            else:
                unique_airport[airpt_name] += 1

            count += 1

    # Convert dictionary to json.

    dict_json = json.dumps(unique_airport, indent=2)
    print("\nOutput 1 : List of unique airport names, number of times in a json format\n")
    print(dict_json + "\n")
    return unique_airport

def max_min_occurence(uniq_dictionary):
    #Prints the MAX (Name and count)

    max_occurence = max(uniq_dictionary, key=uniq_dictionary.get)


    # Prints the MIN (Name and count)

    min_occurence = min(uniq_dictionary, key=uniq_dictionary.get)
    min_max = [max_occurence, min_occurence, uniq_dictionary]

    return min_max


def source_path(path):
    '''
    Get absolute path to source . Used here to check if the file exists.
    '''

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path,path)
filename = "airlines.csv"
def output(filename):

    # file = source_path('airlines.csv')
    file = source_path(filename)
    try:

        uniq_airp = open_csv(file)
        min_max = max_min_occurence(uniq_airp)
        '''
        min_max = [max_occurence, min_occurence, uniq_dictionary] in max_min_occurence method
        '''
        print("Output 2 : Airport is mentioned highest number of times and its count")
        print(f'\t{min_max[0]}: {min_max[2][min_max[0]]} \n')#for maximum occurence
        print("Output 3 : Airport is mentioned lowest number of times and its count")
        print(f'\t{min_max[1]}: {min_max[2][min_max[1]]}')#for minimum occurence

    except FileNotFoundError:
        '''
        Prints this error if the file doesn't exists
        '''

        print("\nFile does not exists, Do you want to give path?(Y/N) \n")
        ask = input("ans: ").lower()
        if ask == 'y' or ask == 'yes':
            filename = input("Enter path to csv file here: ")
            output(filename)

output(filename)
