from itertools import product

def generate_permutations_with_repetition(input_string, repetition):
    # Generate all permutations with repetition
    permutations = product(input_string, repeat=repetition)
    print(permutations)

    # Print each permutation
    for p in permutations:
        print(''.join(p), end = ' ')

# Example usage
input_str = "abc"
repetition_num = 2
generate_permutations_with_repetition(input_str, repetition_num)
