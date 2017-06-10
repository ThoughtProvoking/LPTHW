# create a class called Song
class Song(object):

    # constructor, receives a list of strings
    def __init__(self, lyrics):
        # set self.lyrics to given lyrics
        self.lyrics = lyrics

    # class method, no arguments
    def sing_me_a_song(self):
        # print every string in the lyrics list
        for line in self.lyrics:
            print(line)

    def update_lyrics(self, index, lyrics):
        self.lyrics[index] = lyrics

# create Song object with three lines
happy_bday = Song(['Happy birthday to you',
"I don't want to get sued",
"So I'll stop right there"])

# create Song object with two lines
bulls_on_parade = Song(['They rally around tha family',
'With pockets full of shells'])

# call class method sing_me_a_song of happy_bday
happy_bday.sing_me_a_song()

# call class method sing_me_a_song of bulls_on_parade
bulls_on_parade.sing_me_a_song()

# create Song object with four lines
# secrets = Song(['Tell me what you want to hear',
# 'Something that will light those ears',
# "I'm sick of all the insincere",
# "So I'm going to give all my secrets away"
# ])

# store song lyrics into variable
secrets_lyrics = ['Tell me what you want to hear',
'Something that will light those ears',
"I'm sik of all tha insinseer",
"So I'm going to give all my secrets away"]

# create Song object with list variable
secrets = Song(secrets_lyrics)

# call class method sing_me_a_song of secrets
secrets.sing_me_a_song()

# replace third line with correct line
secrets.update_lyrics(2, "I'm sick of all the insincere")

# call sing_me_a_song after update
secrets.sing_me_a_song()
