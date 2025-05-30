#include<iostream>

main(){
	int row, column;
	while(scanf("%d %d",&row, &column) != EOF){
		int matrix[row][column];
		for(int i=0; i < row; i++){
			for(int j=0; j < column; j++){
				scanf("%d",&matrix[i][j]);
			}
		}
		
		for(int i=0; i < column; i++){
			for(int j=0; j < row; j++){
				printf("%d ",matrix[j][i]);
			}
			printf("\n");
		}
	}
}
