from typing import Dict

def word_frequency(phrase: str) -> Dict:
    '''Function to count the number of words in a phrase
       Parameters:
            phrase: (string) phrase to be analyzed 
       Returns:
            Dictionary with each word of the phrase as a key. The value is the number
            of times that words appears in the phrase
    '''
    # For this function, I split the words of the phrase into a list
    #
    #       words = phrase.split(' ')
    #
    # After this, I iterate over each word in words in a dict comprehension, using the word
    # as a key, and then using count() in the list words to count the ocurrences as a value.
    words = phrase.split(' ')  # Split the phrase into a list of words
    return {word: words.count(word) for word in words}


if __name__ == '__main__':

    string = "the quick brown fox jumps over the lazy dog"

    print(word_frequency(phrase=string))