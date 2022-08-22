#include<stdio.h>
VOID imprimir(CHAR *);

INT main(){
	INT a = 10, i = 0;
	
	imprimir("Inicio do Programa\n");

	SWITCH (a) {
					CASE 5:
			printf("a = 5\n");
			BREAK;
					CASE 10:
			printf("a = 10\n");
			BREAK;
					DEFAULT:
			printf("a = 0\n");
			BREAK;
	}
	
	FOR (i = 0; i <= 10; i++) {
		printf("a + %d = %d\n", i, a + i);
	}

	imprimir("Fim do Programa\n");
	
	RETURN 0;
}
VOID imprimir(CHAR * msg) {
	printf(msg);
		
	RETURN;
}
