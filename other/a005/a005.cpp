#include<iostream>

main(){
	int times;
	scanf("%d", &times);
	for(int i=0; i<times; i++){
		int ans[5];
		scanf("%d%d%d%d", &ans[0],&ans[1],&ans[2],&ans[3]);
		
		if (ans[1]-ans[0] == ans[2]-ans[1])
			printf("%d %d %d %d %d",ans[0],ans[1],ans[2],ans[3],ans[3]+(ans[1]-ans[0]));
		else
			printf("%d %d %d %d %d",ans[0],ans[1],ans[2],ans[3],ans[3]*(ans[1]/ans[0]));
		printf("\n");
	}
}
