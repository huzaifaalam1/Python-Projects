'''
File: word_search.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: This program reads a file
        with information about Pokemons.
        It then goes over the data calculating
        the highest average of each stat in each 
        type of pokemon. It then returns the type
        and the pokeon based on user input.
'''
def create_dict(filename):
    '''
    The function reads a file and
    creates a 2-D dictionary based 
    on the data provided by the file
    Parameter: file containing the data
    returns: the 2-D dictionary
    '''

    # open file
    file = open(filename, "r")
    # create an empty dictionary
    pokemon_dict = {}
    # iterate over each line in the file
    for line in file:
        # checks if the line begins with a #
        if line[0] != "#":
            # makes a list of each line in the line
            line_list = line.strip("\n").split(',')
            # assigns the second item in the list as pokemon name
            pokemon_name = line_list[1]
            # assigns the third item in the list as pokemon type
            pokemon_type = line_list[2]
            # assigns the stats of the pokemon to pokemon stats
            pokemon_stats = line_list[4:11]
            # adds pokemon type in dictionary
            if pokemon_type not in pokemon_dict:
                # gives the pokemon type an empty dictionary for its value
                pokemon_dict[pokemon_type] = {}
                # makes pokemon name the key in inner dictionary 
                pokemon_dict[pokemon_type][pokemon_name] = []
            else:
                pokemon_dict[pokemon_type][pokemon_name] = []
            # iterates over the pokemon stats
            for i in pokemon_stats:
                # appends the stats to the inner dictionary value list
                pokemon_dict[pokemon_type][pokemon_name].append(int(i))
            
    return pokemon_dict

def user_input(pokemon_dict,user_queries):
    '''
    This function call another function
    that returns the answer to the user 
    query provided it is a valid query
    Parameters: 2-D dictionary of the data
                user queries
    Returns: Does not return anything
    '''

    # assigned values to stats to use as index
    st={'total':0, 'hp':1, 'attack':2, 'defense':3, 
       'specialattack':4, 'specialdefense':5, 'speed':6}
    # iterates over the user queries
    for user_query in user_queries:
        # check if user query in stats
        if user_query.lower() in st:
            # calls the print function with the
            # average function and user query
            print_results(get_average(pokemon_dict,st[user_query.lower()]))
        # terminates query if query has no length 
        elif user_query=='':
            print("Query Terminated")


def get_average(pokemon_dict,input_index):
    '''
    This function calculates the max average of each 
    type of pokemon for any specific stat.
    Parameters: 2D dictionary of data
                index of user query 
    Returns: a list of the type of pokemon
            and its max average for a stat 
    '''

    averages = {}
    # iterates over the pokemon types in dictionary
    for pokemon_type in pokemon_dict:
        total = 0
        count = 0
        # iterates over the names in pokemon type
        for pokemon_name in pokemon_dict[pokemon_type]:
            # adds the stat value for each name
            total += pokemon_dict[pokemon_type][pokemon_name][input_index]
            count += 1
        # calculates average
        averages[pokemon_type] = total/count
    
    query_return = {}
    result =[]
    # finds the maximum from the averages
    max_avg_value = max(averages.values()) 
    # iterates over averages
    for key,value in averages.items():
        # checks if average equals max value 
        if value==max_avg_value:
            # assigns max value to type in a new dictionary
            query_return[key]=value

    # sorts the new dictionary
    for item in sorted(query_return.keys()):
        # appends pokemon type and max average to result list 
        result.append([item,query_return[item]])
    
    return result

def print_results(result):
    '''
    This function prints the pokemon type
    and its max average for the respective
    stat provided by the user.
    Parameters: a result list 
    Returns: Prints in the right format
    '''
    # iterates over the list
    for index in result:
        # prints in format required
        print("{}:{}".format(index[0],index[1]))


def main():
    '''
    This function takes in user input and 
    calls other functions for user query 
    to be processed
    Parameters: None
    Returns: None
    '''

    # asks user input for file name
    filename = input()
    # calls create dictionary function using the file name
    pokemon_dict = create_dict(filename)

    # makes a list of all user queries
    user_queries = []
    # runs till user provides queries
    while True:
        user_query = input()
        if user_query == '':
            break
        # appends queries to the list
        user_queries.append(user_query)
    # calls the user input function giving it the parameters
    user_input(pokemon_dict, user_queries)
    
main()