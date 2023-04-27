#include <stdio.h>
#include <math.h>

int main(){
  int arr[] = {1,3,4,5};
  int size = sizeof(arr)/sizeof(arr[0]);

  int revnum = 0;
  for(int i=size-1; i>=0; i--){
    revnum += (int)(pow(10, size-1-i)) * arr[size - 1 - i];
  } 
  
  int num=0;
  for(int i=0; i<size; i++){
      num += arr[i] * (int)pow(10, size-i);
  }

  printf("%d\n", num/10);
  printf("%d\n", revnum);

  return 0;
}

