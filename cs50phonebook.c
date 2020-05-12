#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    person people[4];
    people[0].name = "JIM";
    people[0].number = "253-555-0100";
    
    people[1].name = "JACK";
    people[1].number = "253-555-0101";
    
    people[2].name = "JOHNNY";
    people[2].number = "253-555-0102";
    
    people[3].name = "JOHNNY";
    people[3].number = "253-555-0103";

    for (int i = 0; i < 4; i++)
    {
        if (strcmp(people[i].name, "JIM") == 0)
        {
            printf("%s\n", people[i].number);
            return 0;
        }
        printf("Not found\n");
        return 1;
    }
}
