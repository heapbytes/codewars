#include <stdio.h>


int descending(int f){
  int tmp;
}

int main(){
  
  int f = 38433;
  int tmp;
  int arr[6];
  int i =0;

  while(f>0){
    tmp = f % 10;
    //printf("Digit : %d\n", tmp);
    arr[i] = tmp;
    f = f / 10;
    i++;
  }

  for(int j=0; j<6; j++){
    printf("%d \n", arr[j]);
  }

  printf("size of the arrya is : %d", sizeof(arr)/sizeof(arr[0]));

  //printf("Descending order is : %d", descending(f));
  return 0;
}
