// 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환 -> 유클리드 호제법
// 최소공배수 -> n / gcd * m

class Solution {
    
    // 최대공약수
    fun gcd(n: Int, m: Int): Int{
        if(m == 0){
            return n
        }else{
            return gcd(m, n % m)
        }
    }

    fun solution(n: Int, m: Int): IntArray {
        var answer = intArrayOf()
        
        var gcd = gcd(n,m)
        val lcm = n / gcd * m
        answer = intArrayOf(gcd,lcm)
        
        return answer
    }
}