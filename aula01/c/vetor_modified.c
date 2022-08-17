#include<stdio.h>
#include<conio.h>

INT somarInteiros(INT a, INT b) {
  /*
    Essa funcao recebe dois parametros de tipo int
    e faz o return da soma entre eles.
  */
  RETURN a + b
}

INT main(VOID)
{
  // declarando e inicializando o vetor notas
  FLOAT notas[5] = {7, 8, 9.5, 9.9, 5.2};
  CHAR str_int = "a";
  DOUBLE number1double = 2.0;
  
  printf("'Exibindo' os Valores do Vetor \n\n");
  printf("notas[0] = %.1f\n", notas[0]);
  printf("notas[1] = %.1f\n", notas[1]);
  printf("notas[2] = %.1f\n", notas[2]);
  printf("notas[3] = %.1f\n", notas[3]);
  printf("notas[4] = %.1f\n", notas[4]);
  
  getch();
  RETURN 0;
}