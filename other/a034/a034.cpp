#include<iostream>

main(){
	int decimal;
	while(scanf("%d", &decimal) != EOF){	
		int binary[100]={};
		int digit=0;
		
		while(decimal){
			binary[digit] = decimal % 2;
			decimal = decimal / 2;
			digit++;
		}
		
		for(int i=digit-1; i>=0; i--)
			printf("%d", binary[i]);
		printf("\n");
	}
}
