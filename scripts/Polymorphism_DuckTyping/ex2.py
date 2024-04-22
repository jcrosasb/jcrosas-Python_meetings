class  Tokenizer:
    '''Class to instantiate a Tokenizer object'''

    def process_text(self, text:str)->list:
        '''Method to process a text and return a list of its words.
           Parameters:
                * text: (String) the text to be processed
           Returns:
                * A list with words from the text'''
        return text.split(' ')


class Stemer:
    '''Class to instantiate a Stemer object'''
    
    def process_text(self, text:str)->list:
        '''Method to stem a text.
           Parameters:
                * text: (String) the text to be processed
           Returns:
                * A list with words up to their fourth character from the text'''
        return [word[:4] for word in text.split(' ')]

class PostTagger:
    '''Class to instantiate a PostTagger object'''
    
    def process_text(self, text:str)->list:
        '''Method to place a tag to each word in the text.
           Parameters:
                * text: (String) the text to be processed
           Returns:
                * A list with tuples consisting if the words from the text and their tag'''
        return [(word, 'NN') for word in text.split(' ')]


if __name__ == '__main__':

    # Text to be analyzed
    string = 'This is a sample sentence.'

    # Instantiate Tokenizer and use 'process_text'
    tokenizer = Tokenizer()
    print(tokenizer.process_text(text=string))

    # Instantiate Stemer and use 'process_text'
    stemer = Stemer()
    print(stemer.process_text(text=string))

    # Instantiate PostTagger and use 'process_text'
    post_tagger = PostTagger()
    print(post_tagger.process_text(text=string))
