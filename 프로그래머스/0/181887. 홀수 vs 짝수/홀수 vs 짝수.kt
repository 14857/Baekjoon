class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        
        var even = 0
        var odd = 0
        
        for (i in num_list.indices){
            if (i%2 == 0){
                even += num_list[i]
            }
            else{
                odd += num_list[i]
            }
        }
        
        answer =  maxOf(even,odd)
        
        return answer
    }
}