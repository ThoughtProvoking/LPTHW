import random
from urllib.request import urlopen
from sys import argv

# store website url
WORD_URL = 'http://learncodethehardway.com/words.txt'
# create empty list
WORDS = []

# create snippets and phrases dict
PHRASES = {
    'class %%%(%%%):': 'Make class named %%% that is-a %%%.',
    'class %%%(object):\n\tdef __init__(self, ***)':
        'class %%% has-a __init__ that takes self and *** params.',
    'class %%%(object):\n\tdef ***(self, @@@)':
        'class %%% has-a function named *** that takes self and @@@ params.',
    '*** = %%%()': 'Set *** to an instance of %%%.',
    '***.***(@@@)': 'From ***, get the *** function, call it with params self, @@@.',
    "***.*** = '***'": "From ***, get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
# check if 'english' was given as command line argument and set flag
if len(argv) == 2 and argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # append each word to WORDS list
    WORDS.append(str(word.strip(), encoding='utf-8'))


def convert(snippet, phrase):
    # create a list of random class names, with first letter capitalized, equal to number of '%%%'
    # equivalent to:
    # class_names = []
    # for w in random.sample(WORDS, snippet.count('%%%')):
    #     class_names.append(w.capitalize())
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count('%%%'))]
    # create a list of random other names
    other_names = random.sample(WORDS, snippet.count('***'))
    # create empty lists
    results = []
    param_names = []

    for i in range(0, snippet.count('@@@')):
        # determine random number of parameters
        param_count = random.randint(1, 3)
        # create same random number of parameter names
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        # copy the sentence list
        result = sentence[:]
        
        # fake class names
        for word in class_names:
            # replace '%%%' with random class name (only first occurrence)
            result = result.replace('%%%', word, 1)
        
        # fake other names
        for word in other_names:
            # replace '***' with random other name (only first occurrence)
            result = result.replace('***', word, 1)

        # fake parameter lists
        for word in param_names:
            # replace '@@@' with random parameter name (only first occurrence)
            result = result.replace('@@@', word, 1)

        # append modified sentence to results list
        results.append(result)

    # return results list
    return results


# keep going until they hit CTRL-D
# try code first
try:
    # infinite loop
    while True:
        # get the snippets, which are the keys of PHRASES dict
        snippets = list(PHRASES.keys())
        # shuffle the snippets
        random.shuffle(snippets)

        for snippet in snippets:
            # get corresponding phrase
            phrase = PHRASES[snippet]
            # replace the '%%%', '***', and '@@@' in the snippets and phrases
            question, answer = convert(snippet, phrase)
            # switch the question and answer if user wants phrase first
            if PHRASE_FIRST:
                question, answer = answer, question
            
            # print the question
            print(question)

            # receive user answer
            input('> ')
            # print the actual answer
            print(f'ANSWER: {answer}\n\n')

# handle possible End of File error
except EOFError:
    print('\nBye')
