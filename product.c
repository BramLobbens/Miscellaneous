#include <stdio.h>
#include <stdint.h>

#define SIZEOFARRAY 10

uint64_t reduce(int *array_of_ints);

int main()
{
    int numbers[SIZEOFARRAY];
    int *pn = numbers;
    int n = 0;
   
    while (++n <= SIZEOFARRAY)
	*pn++ = n;  /*populate array*/

    printf("%lu\n", reduce(numbers));
    return 0;
}

/* reduce: reduce array of ints to its product */
uint64_t reduce(int *s)
{
    uint64_t product = 1;
    while (*s++ < SIZEOFARRAY)
	product *= *s;

    return product;
}

