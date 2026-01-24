class Solution {
    fun solution(s: String): Int {
        var answer: Int = 0
        
        val num = arrayOf("0","1","2","3","4","5","6","7","8","9")
        val words = arrayOf("zero","one","two","three","four","five","six","seven","eight","nine")
        var string = s
        
        for(word in words){
            if (word in string){
                string = string.replace(word, num[words.indexOf(word)])
            }
        }
        
        answer = string.toInt()
        
        return answer
    }
}