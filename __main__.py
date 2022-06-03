def retrieve_list() -> list:
    '''Requests user input for a list of numbers and returns it.'''
    list_input = input('Enter list of numbers (format as "[100,4,200,1,3,2]"): ')
    nums = [int(x.strip()) for x in list_input[1:-1].split(',')]
    return nums

def longestConsecutive(nums: int) -> int:
    '''Takes in a list of numbers and returns the length of the longest
    consecutive sequence.'''
    print('Finding longest consecutive sequence')
    if not nums: return 0
    sequences = []

    x: int
    for x in nums:
        nearest_greater_value_index = -1

        added_to_sequence = False
        prepended = False
        appended = False
        print(f'Inserting {x}...')
        for seq_i in range(len(sequences)):
            if prepended and appended: break
            B, E, L = sequences[seq_i]

            if x < B and nearest_greater_value_index == -1:
                nearest_greater_value_index = seq_i
                break

            if x == (B-1):
                sequences[seq_i] = (x, E, L+1) # update beginning and length
                added_to_sequence = True
                prepended = True
            elif x == (E+1):
                sequences[seq_i] = (B, x, L+1) # update ending and length
                added_to_sequence = True
                appended = True
            elif B <= x <= E:
                # sequences[seq_i] = (B, E, L+1) # update length only
                added_to_sequence = True

        if not added_to_sequence:
            if nearest_greater_value_index == -1: nearest_greater_value_index = len(sequences)
            sequences.insert(nearest_greater_value_index, (x, x, 1)) # push new sequence

        # check if need to merge any sequences
        found = False
        seqs_len = len(sequences)
        for i in range(seqs_len-1):
            if found: break
            for j in range(i+1, seqs_len):
                # print(sequences[i], sequences[j])
                Bi, Ei, Li = sequences[i]
                Bj, Ej, Lj = sequences[j]

                if Ei == Bj-1:
                    sequences[i] = (Bi,Ej,Li+Lj)
                    sequences.pop(j)
                    found = True
                    break
                elif Ei == Bj:
                    sequences[i] = (Bi,Ej,Li+Lj-1)
                    sequences.pop(j)
                    found = True
                    break
                elif Ej == Bi-1:
                    sequences[i] = (Bj,Ei,Li+Lj)
                    sequences.pop(j)
                    found = True
                    break
                elif Ej == Bi:
                    sequences[i] = (Bj,Ei,Li+Lj-1)
                    sequences.pop(j)
                    found = True
                    break
        print(sequences)
    
    # find the longest sequence from the bucket of sequences
    longest_sequence = max(sequences, key=lambda item: item[2])
    print(longest_sequence)
    return longest_sequence[2]

def main():
    nums = retrieve_list()
    longest_seq_length = longestConsecutive(nums)
    print(longest_seq_length)
if __name__ == '__main__':
    main()