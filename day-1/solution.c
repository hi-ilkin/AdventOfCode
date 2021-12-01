#include <stdio.h>

/*
* Run in single line : gcc solution.c -o run & run.exe
*/
void main(){
    FILE *fp;
    int cur_value = -1;
    int prev_value = -1;
    int counter = 0;
    

    fp = fopen("input.txt", "r");
    
    fscanf(fp, "%d", &cur_value);
    prev_value = cur_value;

    while(!feof(fp)){
        fscanf(fp, "%d", &cur_value);
        if (cur_value > prev_value){
            counter ++; 
        }
        prev_value = cur_value;
    }

    fclose(fp);
    printf("Total number of increases: %d", counter);
}