#include <stdio.h>
#include <math.h>

int main(){
	int n, L, i;
	float A, B, C, delta, x1, x2, pierwiastek_z_delty;
	
	scanf("%d", &n);
	
	for(i=0;i<n;i++){
		
		scanf("%g %g %g", &A, &B, &C);
	
		delta = (B*B)-(4*A*C);
		
		if (delta==0) {
			if (A!=0){
				if (B!=0){
					x1 = -B/(2*A);
					L = 1;
					printf("%d %g\n", L, x1);
					}
				else{
					x1 = 0;
					L = 1;
					printf("%d %g\n", L, x1);
					}
				
				}
			else{
				if (B!=0){
					if (C!=0){
						L = 1;
						x1 = -C/B;
						printf("%d %g\n", L, x1);
						}
					else{
						L = 1;
						x1 = 0;
						printf("%d %g\n", L, x1);
						}
					
					}
				else{
					if (C!=0){
						L = 0;
						printf("%d\n", L);
						}
					else{
						printf("R\n");
						}
					
					}
				
				}			
	
			}		
	
		else if (delta<0) {
			L = 0;
			printf("%d\n", L);
			}
		
		else{
			if (A!=0){
				pierwiastek_z_delty = sqrt(delta);
				x1 = (-B-pierwiastek_z_delty)/(2*A);
				x2 = (-B+pierwiastek_z_delty)/(2*A);
				L = 2;
				
				if (x1<x2){
					printf("%d %g %g\n", L, x1, x2);
					}
				else{
					printf("%d %g %g\n", L, x2, x1);
					}
				
				}
			else{
				if (B!=0){
					if (C!=0){
						L = 1;
						x1 = -C/B;
						printf("%d %g\n", L, x1);
						}
					else{
						L = 1;
						x1 = 0;
						printf("%d %g\n", L, x1);
						}
					
					}
				else{
					if (C!=0){
						L = 0;
						printf("%d\n", L);
						}
					else{
						printf("R\n");
						}
					}
				}
			
	
			}
		
	}
	
	
	
	
	
	return 0;
}
