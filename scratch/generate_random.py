import random
import sys

def main():
    random_list = generate_random_list(int(sys.argv[1]))
    #print(random_list)
    #largest_value, index_pos = largest_position(random_list)
    #print(f'The largest value in the list is {largest_value} and it is at index position {index_pos}')

# Generates a list of random unique numbers within a given range limit
def generate_random_list(n):
    result = list(range(0, n))
    random.shuffle(result)
    return result

# returns the index position of the largest element in the list
def largest_position(input_list):
    largest_pos = 0

    for i in range (1, len(input_list)):
        if input_list[i] > input_list[largest_pos]:
            largest_pos = i
    return input_list[largest_pos], largest_pos

if __name__ == "__main__":
     main()