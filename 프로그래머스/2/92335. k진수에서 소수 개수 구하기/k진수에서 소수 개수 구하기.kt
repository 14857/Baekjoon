// n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 조건에 맞는 소수의 개수 반환
// 중복되는 소수를 발견하더라도 모두 따로 센다
// 10진법으로 보았을 때 소수여야 한다.

import kotlin.math.sqrt
class Solution {
    
    // 소수 판별 함수(1인 경우 소수, 아닌 경우 0)
    fun check(n: Long):Int{
        if(n < 2) return 0
        
        // (i in 2..n-1)인 경우 시간복잡도 증가
        val limit = sqrt(n.toDouble()).toLong()
        
        for(i in 2..limit){
                if(n % i == 0L){
                    return 0
                } 
            }
    
        println(n)
        return 1
    }
    
    fun solution(n: Int, k: Int): Int {
        var answer: Int = 0
        
        // k 진수로 변환한 수
        var num = n.toString(k)
        println(num)
        
        // 조건에 맞는 소수 찾기
        var lst = num.split(Regex("0+"))
        println(lst)
        
        for (i in lst) {
            if (i.isNotEmpty()) {
                answer += check(i.toLong())
            }
        }
        
        return answer
    }
}