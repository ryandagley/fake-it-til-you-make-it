#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{ 
    string names[4] = {"JIM", "JACK", "JOHNNY", "JOSE"};

    for (int i = 0; i < 4; i++)
    {
        if (strcmp(names[i], "JACK") == 0)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
