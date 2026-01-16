class Solution {
    fun solution(strArr: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        
        for(i in strArr){
            if("ad" !in i){
                answer += i
            }
        }
        
        return answer
    }
}