from sys import argv

# unpack command line arguments
script, encoding, error = argv

def main(language_file, encoding, errors):
    # store a line from file
    line = language_file.readline()

    # if there is a line
    if line:
        # call print_line function on it
        print_line(line, encoding, errors)
        # repeat
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # remove '\n' from string
    next_lang = line.strip()
    # get bytes of string
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # get string from bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # print corresponding bytes and string
    print(raw_bytes, '<===>', cooked_string)
    

# open file
languages = open('languages.txt', encoding='utf-8')

# start byte-string conversion process
main(languages, encoding, error)

# close file
languages.close()
