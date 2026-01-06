class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        
        var mul = 1
        var sum_s = num_list.sumOf{it} * num_list.sumOf{it}
        
        for (i in num_list){
            mul *= i
        }
        
        if (mul < sum_s){
            answer = 1
        }
        return answer
    }
}