class Solution {
    fun solution(myString: String): IntArray {
        var answer: IntArray = intArrayOf()
        
        var lst = myString.split("x")
        
        for(i in lst){
            answer += i.length
        }
        
        return answer
    }
}