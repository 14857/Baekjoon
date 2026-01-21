class Solution {
    fun solution(myString: String): String {
        var answer: String = ""
        
        for(char in myString){
            if(char < 'l'){
                answer += 'l'
            }else{ answer += char}
        }
        return answer
    }
}