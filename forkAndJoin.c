#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h> // exit()
#include <sys/wait.h> // wait()

int main(int argc, char* argv[]) {

    pid_t child = fork();
    if (child < 0) {
        perror("fork() error");
        exit(-1);
    }

    if (child != 0) {
        printf("I'm the parent %d, my child is %d\n", getpid(), child);
        wait(NULL); // wait for child process to join
    } else {
        printf("I'm the child %d, my parent is %d\n", getpid(), getppid());
        execl("/bin/echo", "echo", "Hello, world", NULL);
    }
    return 0;
}
