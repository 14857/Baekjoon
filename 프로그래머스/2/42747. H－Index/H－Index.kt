class Solution {
    fun solution(citations: IntArray): Int {
        var answer = 0
        var sort = citations.sortedDescending()
        var maxnum = citations.maxOrNull() ?: 0
        
        for(i in maxnum downTo 0){
            var cnt = citations.count{ it >= i }
            if(cnt >= i) {
               // println("${i} : ${cnt}")
                answer = i
                break
            }
        }
        
        return answer
    }
}