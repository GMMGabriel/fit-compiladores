rules = {
  0:{'a':1,'b':2},
  1:{'a':0,'b':3},
  2:{'a':3,'b':0},
  3:{'a':2,'b':1},
}

finalState = (0,)

def readLetter(currentState, letter):
  return rules[currentState][letter]

def validate(word):
  currentState = 0
  for w in word:
    currentState = readLetter(currentState, w)
  return currentState in finalState

word = input('Informe a palavra: ')
print(validate(word))