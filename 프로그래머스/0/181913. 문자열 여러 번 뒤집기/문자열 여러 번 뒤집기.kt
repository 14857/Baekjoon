//  인덱스 s부터 인덱스 e까지의 문자열 뒤집기
// 

class Solution {
    fun solution(my_string: String, queries: Array<IntArray>): String {
        
        var answer: String = my_string
        
        for (q in queries){
            
            var ans = StringBuilder()
            var s = q[0]
            var e = q[1]
            
            ans.append(answer.substring(0,s))
            ans.append(answer.substring(s,e+1).reversed())
            ans.append(answer.substring(e+1))
            
            answer = ans.toString()
        }
        return answer
    }
}