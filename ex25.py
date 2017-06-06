def break_words(stuff):
    ''' This function will break up words for us. '''
    # split string by whitespace
    words = stuff.split(' ')
    # return list
    return words

def sort_words(words):
    ''' Sort the words. '''
    # sort list and return it
    return sorted(words)

def print_first_word(words):
    ''' Prints the first word after popping it off. '''
    # pop and return first item in list
    word = words.pop(0)
    # print popped word
    print(word)

def print_last_word(words):
    ''' Prints the last word after popping it off. '''
    # pop and return the last item in list
    word = words.pop(-1)
    # print popped word
    print(word)

def sort_sentence(sentence):
    ''' Takes in a full sentence and returns the sorted words. '''
    # call break_words functio and store returned value
    words = break_words(sentence)
    # call sort_words function and return returned value
    return sort_words(words)

def print_first_and_last(sentence):
    ''' Prints the first and last word of the sentence. '''
    # call break_words function and store returned value
    words = break_words(sentence)
    # call print_first_word function with words variable
    print_first_word(words)
    # call print_last_word function with words variable
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    ''' Sorts the words then prints the first and last one. '''
    # call sort_sentence function and store returned value
    words = sort_sentence(sentence)
    # call print_first_word function with words variable
    print_first_word(words)
    # call print_last_word function with words variable
    print_last_word(words)
