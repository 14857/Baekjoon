// k가 홀수 : arr의 모든 원소에 k를 곱한다
// k가 짝수 : arr의 모든 원소에 k를 더한다

class Solution {
    fun solution(arr: IntArray, k: Int): IntArray {
        var answer: IntArray = intArrayOf()
        
        if(k%2 == 1){
            answer = arr.map {it * k}.toIntArray()
        }else{
            answer = arr.map {it + k}.toIntArray()
        }
        
        
        return answer
    }
}