#include <stdio.h>
#include <string.h>
#include <ctype.h>

//kata link : https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/c

char *to_jaden_case (char *jaden_case){ //, const char *jaden_caseing){
  
  for(int i=0; jaden_case[i] != '\0'; i++){
    if(i == 0 || isspace(jaden_case[i-1])){
      jaden_case[i] = toupper(jaden_case[i]);
    } else{
      jaden_case[i] = tolower(jaden_case[i]);
    }
  }

  return jaden_case;
}

int main(){
  
  char str[] = "s";
  printf("%s", to_jaden_case(str));
  
  return 0;
}
