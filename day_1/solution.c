#include <stdio.h>

/*
* Run in single line : gcc solution.c -o run & run.exe
*/

int solve_first_part(FILE *fp){
    int cur_value;
    int prev_value;
    int counter = 0;

    fscanf(fp, "%d", &cur_value);
    prev_value = cur_value;

    while (!feof(fp))
    {
        fscanf(fp, "%d", &cur_value);
        if (cur_value > prev_value)
        {
            counter++;
        }
        prev_value = cur_value;
    }

    return counter;
}

int sum(int arr[], int len){
    int s = 0;
    for (int i=0; i < len; i ++ ){
        s += arr[i];
    }

    return s;
}

void shift_left(int *arr, int len){
    for (int i=0; i < len; i++ ){
        arr[i] = arr[i + 1];
    }
}

int solve_second_part(FILE *fp){
    int cur_sum;
    int prev_sum;
    int counter = 0;
    int window_size = 3;
    int window[window_size];

    for(int i=0; i < 3 ; i++){
        fscanf(fp, "%d", &window[i]);
    }

    prev_sum = sum(window, window_size);

    while(!feof(fp)){
        shift_left(window, window_size);
        fscanf(fp, "%d", &window[window_size - 1]);

        cur_sum = sum(window, window_size);

        if (cur_sum > prev_sum){
            counter ++;
        }
        prev_sum = cur_sum;
    }

    return counter;
}

void main()
{
    FILE *fp;
    fp = fopen("input.txt", "r");
    int counter = solve_second_part(fp);
    fclose(fp);

    printf("Total number of increases: %d", counter);
}