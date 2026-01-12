//  정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 반환

class Solution {
    fun solution(arr: IntArray, idx: Int): Int {
        var answer: Int = -1
        
        for(i in idx..arr.size-1){
            if (arr[i] == 1){
                answer = i
                break
            }
        }
        
        return answer
    }
}