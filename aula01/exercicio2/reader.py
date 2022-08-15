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

reservedWords = ["asm","auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned","void","volatile","while",]

filePath = './aula01/c/'

with open(filePath+'vetor.c', 'r') as f:
  lines = f.readlines()

  or_s = '|'.join(reservedWords)

  finalStr = ''
  for l in lines:
    arr = re.findall(r'(?:{})(?![a-zA-Z])'.format(or_s), l)
    temp = l

    if len(arr) > 0: # não achou nenhuma palavra reservada
      # Retira os textos e comentários
      temp = re.sub(r'\".*\"', '', temp)
      temp = re.sub(r'\/\/.*', '', temp)
      arrConfirm = re.findall(r'(?:{})(?![a-zA-Z])'.format(or_s), temp)

      # Verifica se continua com a mesma quantidade de palavras reservadas
      if len(arr) == len(arrConfirm):
        # Nenhuma palara reservada estava em um texto ou em um comentário
        for a in arr:
          if a in reservedWords:
            temp = temp.replace(a, a.upper())
      else:
        # Houve diferença
        if len(arrConfirm) > 0: # as palavras não estão em textos ou comentários
          temp = 'AQUI TEVE DIFERENCA ' + temp
        else: # as palavras ESTÃO em textos ou comentários, então não conta
          temp = l

    finalStr += temp

  with open(filePath+'vetor_modified.c', 'w') as f:
    f.write(finalStr)