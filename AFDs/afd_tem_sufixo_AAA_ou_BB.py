rules = {
  0:{'a':1,'b':5},
  1:{'a':2,'b':5},
  2:{'a':3,'b':5},
  3:{'a':3,'b':5},
  4:{'a':1,'b':4},
  5:{'a':1,'b':4},
}

finalState = (3,4)

def readLetter(currentState, letter):
  return rules[currentState][letter]

def validate(word):
  currentState = 0
  for w in word:
    currentState = readLetter(currentState, w)
  return currentState in finalState

word = input('Informe a palavra: ')
print(validate(word))