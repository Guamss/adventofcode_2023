# include <stdio.h>
# include <string.h>
# include <ctype.h>

// Uniquement la partie 1 !

int main()
{
  FILE* fp = fopen("file.txt", "r");
  char line[256];
  if(fp == NULL)
  {
    printf("Erreur de lecture du fichier texte !");
    return 1;
  }
  int first;
  int last = 0;
  int sum = 0;
  while (fgets(line, sizeof(line), fp) != NULL) 
  {
    first = 0; 
    for (int i = 0; line[i] != '\0'; i++)
    {
      if (isdigit(line[i]))
      {
        last = line[i]-48;
        if (first == 0)
          first = last;
      }
    }
    sum += first*10+last;
  }
  printf("sum : %d\n", sum);
  fclose(fp);
  return 0;
}
