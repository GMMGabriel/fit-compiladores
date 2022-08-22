import os

filePath = './ACs/AC1/'
fileCName = 'ex03'
fileExtension = '.c'
fileFont = filePath+fileCName+fileExtension

with open(fileFont, 'r') as f:
  content = f.readlines()
  fullStr = ''.join(content)

  # Pega o número de linhas do arquivo
  lines = len(content) + (1 if content[-1][-1] == '\n' else 0)

  # Conta o número de espaços
  spaces = fullStr.count(' ')

  # Cria uma lista para todos os caracteres do arquivo
  allCharacters = []

  # Retira os espaços em  branco
  fullStr = fullStr.replace(' ', '')

  # Faz a contagem de todos os caracteres
  while fullStr != '':
    c, cCount = fullStr[0], fullStr.count(fullStr[0])
    if c not in ('\n', '\t', '\r', ):
      allCharacters.append([c, cCount])
    fullStr = fullStr.replace(c, '')
  # Organiza a lista em ordem
  allCharacters = sorted(allCharacters, key=lambda item: item[1], reverse=True)

  # Mostra todos os caracteres encontrados e a quantidade de cada um
  i = 1
  for c in allCharacters:
    print("%s => %i" %(c[0], c[1]))
    i += 1

  print("Espaços em branco =>", spaces)
  print("Linhas =>", lines)
  print("Tamanho do arquivo => %.1f bytes" %os.path.getsize(fileFont))