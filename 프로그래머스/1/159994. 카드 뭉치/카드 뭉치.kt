class Solution {
    fun solution(cards1: Array<String>, cards2: Array<String>, goal: Array<String>): String {
        var answer: String = "Yes"
        var c1 = cards1
        var c2 = cards2
        
        for(word in goal){
            
            val c1First = c1.firstOrNull()
            val c2First = c2.firstOrNull()

            if(word != c1First && word != c2First ){
                answer =  "No"
                println(word)
                break
            }else{
                // 해당 단어 cards 배열에서 지우기
                if (word == c1First) {
                c1 = c1.drop(1).toTypedArray()
                }
                else if (word == c2First) {
                    c2 = c2.drop(1).toTypedArray()
                }
            }           
        }       
        return answer
    }
}