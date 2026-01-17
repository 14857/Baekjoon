// X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의 배열 X 반환 -> array

class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        
        for(i in arr){
            repeat(i){
                answer += i
            }
        }
        
        return answer
    }
}