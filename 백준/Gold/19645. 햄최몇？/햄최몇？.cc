#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX_NUM = 50;
const int MAX_TOTAL = 2500;

int num_count;
int num_list[MAX_NUM + 1];
bool dp_table[MAX_TOTAL + 1][MAX_TOTAL + 1];

int main(){
    int total_sum = 0;
    scanf("%d", &num_count);
    
    for (int i = 1; i <= num_count; i++){
        scanf("%d", &num_list[i]);
        total_sum += num_list[i];
    }
    
    dp_table[0][0] = true;
    
    for (int i = 1; i <= num_count; i++){
        for (int j = total_sum; j >= 0; j--){
            for (int k = total_sum; k >= 0; k--){
                if (j - num_list[i] >= 0) {
                    dp_table[j][k] |= dp_table[j - num_list[i]][k];
                }
                if (k - num_list[i] >= 0){
                    dp_table[j][k] |= dp_table[j][k - num_list[i]];
                }
            }
        }
    }
    
    int max_result = 0;
    for (int i = 0; i <= total_sum; i++){
        for (int j = 0; j <= i; j++){
            if (dp_table[i][j] && j >= (total_sum - i - j)){
                max_result = max(max_result, total_sum - i - j);
            }
        }
    }
    
    printf("%d\n", max_result);
    
    return 0;
}
