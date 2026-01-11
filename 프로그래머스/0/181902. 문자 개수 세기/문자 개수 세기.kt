// answer[0~25] → 'A' ~ 'Z' : 65 ~ 90
// answer[26~51] → 'a' ~ 'z': 97 ~ 122
// 타입이 다르기 때문에 ch-65로 하면 오류 발생

class Solution {
    fun solution(my_string: String): IntArray {
        var answer: IntArray = IntArray(52){0}
        
        for (ch in my_string){
            when{
                ch in 'A'..'Z'->{ 
                    answer[ch-'A']++
                }
                ch in 'a'..'z'->{
                    answer[ch-'a'+26]++
                }
            }
        } 
        return answer
    }
}