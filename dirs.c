#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h> // For rmdir
#include <limits.h> // For PATH_MAX

void list_directory(const char *dirname)
{
    DIR *pDir;
    struct dirent *dp;

    pDir = opendir(dirname);
    if (pDir == NULL)
    {
        perror("opendir");
        return;
    }

    printf("Contents of %s:\n", dirname);
    while ((dp = readdir(pDir)) != NULL)
    {
        printf("%s\n", dp->d_name);
    }

    closedir(pDir);
}

void create_directory(const char *dirname)
{
    if (mkdir(dirname, 0755) != 0)
    {
        perror("mkdir");
    }
    else
    {
        printf("Directory '%s' created successfully.\n", dirname);
    }
}

void remove_directory(const char *dirname)
{
    if (rmdir(dirname) != 0)
    {
        perror("rmdir");
    }
    else
    {
        printf("Directory '%s' removed successfully.\n", dirname);
    }
}

void open_directory(const char *dirname)
{
    if (chdir(dirname) != 0)
    {
        perror("chdir");
    }
    else
    {
        printf("Changed directory to '%s'.\n", dirname);
    }
}

int main()
{
    char command[256];
    char dirname[256];

    while (1)
    {
        printf("Enter a command (ld, md, rd, cd, exit): ");
        scanf("%s", command);

        if (strcmp(command, "ld") == 0)
        {
            list_directory(".");
        }
        else if (strcmp(command, "md") == 0)
        {
            printf("Enter the name of the directory to create: ");
            scanf("%s", dirname);
            create_directory(dirname);
        }
        else if (strcmp(command, "rd") == 0)
        {
            printf("Enter the name of the directory to remove: ");
            scanf("%s", dirname);
            remove_directory(dirname);
        }
        else if (strcmp(command, "cd") == 0)
        {
            printf("Enter the name of the directory to change to: ");
            scanf("%s", dirname);
            open_directory(dirname);
        }
        else if (strcmp(command, "exit") == 0)
        {
            break;
        }
        else
        {
            printf("\"%s\": unknown command\n", command);
        }
    }

    return 0;
}
