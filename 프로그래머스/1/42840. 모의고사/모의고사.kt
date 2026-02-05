// 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5 (12345 반복)
// 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5 (인덱스 짝수는 2 홀수는 순서대로 12345)
// 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 (3311224455 반복)

// 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 반환

class Solution {
    fun solution(answers: IntArray): IntArray {
        var answer = intArrayOf()
        
        val base1 = intArrayOf(1,2,3,4,5)
        val base2 = intArrayOf(2, 1, 2, 3, 2, 4, 2, 5)
        val base3 = intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        
        var num1 = IntArray(answers.size) { i -> base1[i % base1.size] }
        var num2 = IntArray(answers.size) { i -> base2[i % base2.size] }
        var num3 = IntArray(answers.size) { i -> base3[i % base3.size] }

        println(num1.contentToString())
        println(num2.contentToString())
        println(num3.contentToString())
        
        val count1 = num1.indices.count{num1[it] == answers[it]}
        val count2 = num1.indices.count{num2[it] == answers[it]}
        val count3 = num1.indices.count{num3[it] == answers[it]}
        
        val max = maxOf(count1,count2,count3)
        
        if(count1 == max) answer += 1
        if(count2 == max) answer += 2
        if(count3 == max) answer += 3
        
        return answer
    }
}