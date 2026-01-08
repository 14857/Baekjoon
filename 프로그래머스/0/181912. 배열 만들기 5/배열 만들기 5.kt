class Solution {
    fun solution(intStrs: Array<String>, k: Int, s: Int, l: Int): IntArray {
        var answer: IntArray = intArrayOf()
        
        for(i in intStrs){
            // 문자열 잘라내기
            var num = i.substring(s,s+l).toInt()
            
            // k와 비교하여 배열에 넣기
            if(num > k){
                answer += num
            }
        }
        
        return answer
    }
}