class Solution {
    fun solution(binomial: String): Int {
        var answer: Int = 0
        
        var lst = binomial.split(" ")
        println(lst)
        
        when(lst[1]){
            "+" -> answer = lst[0].toInt() + lst[2].toInt()
            "-" -> answer =lst[0].toInt() - lst[2].toInt()
            "*" -> answer =lst[0].toInt() * lst[2].toInt()        
        }
        
        return answer
    }
}