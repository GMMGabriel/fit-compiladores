'''
Exercício 1
Escreva um programa que leia um arquivo fonte de um
programa escrito na linguagem C e conte a quantidade de
letras a..zA..Z, digitos 0..9 e espaços em brancos, ao final o
seu prorama deve imprimir uma listagem da quantidade de
letras e dígitos em ordem, quantidade de espaços em branco
e o número de linhas no arquivo fonte. Caso para
determinado símbolo não tenha ocorrência não é necessário
imprimir a quantidade igual a zero. Além disso, apresente o
tamanho do arquivo em bytes.
'''

import os
import re

filePath = './aula01/c/'
fileFont = filePath+'vetor.c'

with open(fileFont, 'r') as f:
  content = f.readlines()
  fullStr = ''.join(content)

  # Pega o número de linhas do arquivo
  lines = len(content) + (1 if content[-1][-1] == '\n' else 0)

  # Conta o número de espaços
  spaces = fullStr.count(' ')

  # Cria uma lista para todos os caracteres do arquivo
  allCharacters = []

  # Localiza todos os caracteres
  characters = ''.join(re.findall(r'\w', fullStr)).replace('_', '')

  # Faz a contagem de todos os caracteres
  while characters != '':
    c, cCount = characters[0], characters.count(characters[0])
    allCharacters.append([c, cCount])
    characters = characters.replace(c, '')
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