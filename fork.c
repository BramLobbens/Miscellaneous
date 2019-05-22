#include <unistd.h>
#include <stdio.h>

// compile with: gcc -Wall -Werror -o fork fork.c
int main() {
    int x = 1;
    int returnVal = fork();

    if (returnVal == 0) {
        // only child process executes this
        printf("child, x = %d\n", ++x);
    } else {
        // only parent executes this
        printf("parent, x = %d\n", --x);
    }
    // parent and child execute this
    printf("Exiting with x = %d\n", x);
    return 0;
}
    
