#include <stdio.h>

/* print binary value */
int main(void)
{
    unsigned long long n;
    
    while (scanf("%llu", &n) == 1) {
	
	long double bin = 0;
	int i = 1;
	
	do {
	    bin += n & 1; /* ~(0xffffffff << 1); */
	    bin /= 10; /* keep bit ordering */
	    i *= 10;
	}
	while (n >>= 1); /* shift till zero -> false */

	printf("%.0Lf\n", bin * i);
    }
}
