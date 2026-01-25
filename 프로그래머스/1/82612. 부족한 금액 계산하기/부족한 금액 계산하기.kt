class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        var answer: Long = -1
        var fee = 0L
        
        for(i in 1..count){
            fee += i.toLong() * price.toLong()
        }
        
        answer = maxOf(fee - money, 0L)
        
        return answer
    }
}