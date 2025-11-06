class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        
        var ans1 = "" // 홀수
        var ans2 = "" // 짝수
        
        for (i in 0 until num_list.size){
            if (num_list[i]%2 == 1){
                ans1 += num_list[i].toString()
            }else{
                ans2 += num_list[i].toString()
            }
        }
        
        answer = ans1.toInt() + ans2.toInt()
        return answer
    }
}