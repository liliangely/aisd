#include <stdio.h>

int main(){
	int a, b, c, d;
	scanf("%d %d", &a, &b);
	
	/*metoda1*/	
	c=a;
	d=b;
	c=c-d;
	d=d+c;
	c=d-c;
	printf("%d %d\n",c,d);
	
	/*metoda2*/
	c=a;
	d=b;	
	c=d-c+(d=c);
	printf("%d %d\n",c,d);

	/*metoda3*/	
	c=a;
	d=b;
	c=c*d;
	d=c/d;
	c=c/d;
	printf("%d %d\n",c,d);
	
	/*metoda4*/
	c=a;
	d=b;
	c=c^d;
	d=c^d;
	c=c^d;
	printf("%d %d\n",c,d);
	
	/*metoda5*/
	c=a;
	d=b;
	c=(c&d)+(c|d);
	d=c-d;
	c=c-d;
	printf("%d %d\n",c,d);
	
	/*metoda6*/
	c=a;
	d=b;
	c=c+d;
	d=-(d-c);
	c=c-d;
	printf("%d %d\n",c,d);
	
	/*metoda7*/
	c=a;
	d=b;
	c=~(c+d);
	d=~(c+d);
	c=~(c+d);
	printf("%d %d\n",c,d);
	
	/*metoda8*/
	c=a;
	d=b;
	c=c+d;
	d=c-d;
	c=c-d;
	printf("%d %d\n",c,d);
	
	
	return 0;
}
