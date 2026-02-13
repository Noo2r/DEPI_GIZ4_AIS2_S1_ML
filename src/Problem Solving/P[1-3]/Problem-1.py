"""Reverses the vocabulary of the given string.

    Args: string
    returns: string but reversed word by word
    """
def reverse_vocab(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == "__main__":
    print("Enter a string to reverse its vocabulary:")
    input_string = input()
    reversed_string = reverse_vocab(input_string)
    print(reversed_string)  