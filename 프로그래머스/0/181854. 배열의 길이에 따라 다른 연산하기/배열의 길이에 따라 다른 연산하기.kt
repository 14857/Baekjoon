// arr의 길이가 홀수: arr의 모든 짝수 인덱스 위치에 n을 더한 배열 반환
// arr의 길이가 짝수: arr의 모든 홀수 인덱스 위치에 n을 더한 배열 반환

class Solution {
    fun solution(arr: IntArray, n: Int): IntArray {
        var answer: IntArray = intArrayOf()
        answer = arr
        
        if(arr.size%2 == 1){ // arr의 길이가 홀수인 경우
            for(i in 0..arr.size-1 step 2){
                answer[i] += n
            }
        }else{
            for(i in 1..arr.size-1 step 2){
                answer[i] += n
            }
        }
        
        return answer
    }
}