// arr이 다음을 만족하면 1을 아니라면 0을 반환
// 0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]

class Solution {
    fun solution(arr: Array<IntArray>): Int {
        var answer: Int = 1
        
        for(i in arr.indices){
            for(j in arr.indices){
                if(arr[i][j] != arr[j][i]) answer = 0
            }
        }  
        return answer
    }
}