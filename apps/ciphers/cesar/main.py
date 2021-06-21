####################### NE RIEN CHANGER ICI ################################
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
KEY = 4

# Fonction pour trouver la position des lettres de l'alphabet
def getIndex(letter):
    for i in range(len(ALPHABET)):
        if letter.upper() == ALPHABET[i]:
            return i
####################### NE RIEN CHANGER ICI ################################


# Fonction pour chiffrer les message à implémenter
def encode(message, key):
  pass

# Fonction pour dechiffer à implémenter
def decode(message, key):
  pass



####################### NE RIEN CHANGER ICI ################################

def test(m):
    print(encode(m, KEY))
    print(decode(m, KEY))

test("HELLO", KEY)

####################### NE RIEN CHANGER ICI ################################
