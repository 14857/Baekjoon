// 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사
// 조합 이용 -> 코틀린에는 파이썬처럼 순열, 조합 내장함수 X -> dfs로 구현 필요
// 이 경우 세 수의 합만 0이면 되기 때문에 for문으로 구현

class Solution {
    fun solution(number: IntArray): Int {
        var answer: Int = 0
        
        for (i in 0 until number.size) {
            for (j in i + 1 until number.size) {
                for(k in j+1 until number.size){
                    if(number[i] + number[j] + number[k] == 0) answer += 1
                }
            }
        }
        
        return answer
    }
}