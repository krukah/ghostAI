'''
Using trie structures to implement a program for GHOST
'''
#%%

class LetterNode(object):
    
    def __init__(self, char:str):
        self.char = char
        self.parent = None
        self.children = []
        self.win = 0
        # The 'length' attribute doubles as an Boolean indicator of if a word is terminated
        self.length = 0

#%%

class Game(object):
    
    def __init__(self, num):
        self.word = ''
        self.node = root
        # Number of players
        self.n = num
        self.players = [Player(1), Player(2)]
        self.used_words = []
        self.index = 0

#%%
        
class Player(object):

    def __init__(self, arg):
        self.cpu = True
        self.id = arg - 1
        self.score = 0

    def end_round(self):
        self.score += 1
        # End the game if someone gets 'GHOST'
        if self.score == 5:
            print('Player ', self.id + 1, end = ' ')
            print('has won!')
            # Reset scores
            for player in game.players:
                player.score = 0
            return
        # Display the scores
        print('-' * 15)
        print('P1: ' + 'G H O S T'[:game.players[0].score * 2])
        print('P2: ' + 'G H O S T'[:game.players[1].score * 2])
        print('-' * 15)
        
        # New round
        game.word = ''
        game.node = root
        return

    def go(self, node):

        while True:
            inpt = input('P' + str(self.id + 1) + ':').lower()
            # Validate the input
            if len(inpt) == 1 and inpt.isalpha():
            
                for child in node.children:
                    
                    # Valid letter, end of word
                    if inpt == child.char and child.length:
                        game.word += child.char
                        print('\n' + game.word.upper() + '\n')
                        self.end_round()
                        return
                        
                    # Valid letter, next turn
                    elif inpt == child.char:
                        game.word += child.char
                        game.node = child
                        print(game.word.upper(), end = '')
                        return
                
                # Invalid letter
                print('Unregistered word')
            
            elif inpt == 'quit': quit()
            
            else:
                print('Invalid input')
        
    # Return a LetterNode that the game is currently on
    def play(self, node):
        
        pass

#%%

def add(word:str):
    node = root
    
    # Words three or fewer letters long need not be added
    if len(word) < 4:
        return
    
    # Iterate through each letter in the word to be added
    for char in word:
        # Check if the beginning letters of the word are already added
        in_child = False
        for child in node.children:
            if child.char == char:
                # If there is a complete word within the new word, don't bother
                # adding it because these words can't be played
                if child.length:
                    return
                else:
                    # Move to the next node in the trie
                    node = child
                    in_child = True
                    break
        
        if not in_child:
            next_node = LetterNode(char)
            next_node.parent = node
            # Add to the trie the new LetterNode
            node.children.append(next_node)
            # Move to the new node in the trie
            node = next_node
    
    # Nodes representing ends of words have length
    node.length = len(word)

#%%
def dictionary():
    with open('english_words.txt') as word_file:
        dictionary = set(word.strip().lower() for word in word_file)
    
    for word in dictionary:
        add(word)

#%%

def __main__():
    dictionary()
    
    print('-' * 15)
    print('G H O S T')
    print('-' * 15)
    
    
    while True:
        for player in game.players:
            player.go(game.node)
#%%
        
root = LetterNode('')
game = Game(2)

    
if __name__ == '__main__': __main__()