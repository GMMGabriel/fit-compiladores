'''
Exercício 2

Escreva um programa que tenha como entrada um arquivo
fonte de um programa escrito na linguagem C, e tem como
saída um arquivo fonte modificado, com todas as palavras
reservadas no arquivo de entrada em MAIÚSCULO.
Abaixo a lista de palavras reservadas da linguagem C.

http://linguagemc.com.br/lista-de-palavras-reservadas-em-c/
'''

import re

# Palavras reservadas da linguagem C
reservedWords = ["asm","auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned","void","volatile","while",]

# Caminho da pasta onde está o arquivo .c
filePath = './aula01/c/'

with open(filePath+'vetor.c', 'r') as f:
  lines = ''.join(f.readlines()) # transforma a lista das linhas em uma string

  # Faz o replace para trocar qualquer comentário de uma linha por "__comment__"
  regexComments = r'//.*'
  comments = re.findall(regexComments, lines)
  lines = re.sub(regexComments, '__comment__', lines)

  # Faz o replace para trocar qualquer comentário de multiplas linhas por "__lineComment__"
  lineComments = [] # lista que guardará os comentários
  try: # try para não parar a execução quando não achar mais nenhum comentário de multiplas linhas
    while True:
      # Adiciona o comentário de multiplas linhas na lista
      lineComments.append(lines[lines.index('/*'):lines.index('*/')+2])
      # Pega o último elemento da lista para usar no replace
      lines = lines.replace(lineComments[-1], '__lineComment__')
  except ValueError as e:
    pass

  # Faz o replace para trocar qualquer string por "__string__"
  regexStrings = r'["\']+?.*["\']+?'
  strings = re.findall(regexStrings, lines)
  lines = re.sub(regexStrings, '__string__', lines)

  # Faz uma string com as palavras reservadas separando-as por "|" para usar essa string no regex
  or_s = '|'.join(reservedWords)
  regexReservedWords = r'\W(?:{})(?!\w)'.format(or_s)
  # Localiza e armazena as palavras reservadas
  reservedWordsFound = re.findall(regexReservedWords, lines)
  # Percorre a lista para fazer o replace pelas mesmas palavras, porém com .upper()
  for i in reservedWordsFound:
    lines = re.sub(regexReservedWords, i.upper(), lines, 1)

  # Recoloca os comentários de uma linha
  for i in comments:
    lines = re.sub(r'(?:__comment__)', i.replace('\\n', '\\\\n'), lines, 1)

  # Recoloca os comentários de multiplas linhas
  for i in lineComments:
    lines = re.sub(r'(?:__lineComment__)', i.replace('\\n', '\\\\n'), lines, 1)

  # Recoloca as strings
  for i in strings:
    lines = re.sub(r'(?:__string__)', i.replace('\\n', '\\\\n'), lines, 1)

  # print(lines)

  with open(filePath+'vetor_modified.c', 'w') as f:
    f.write(lines)