class Solution {
    fun solution(code: String): String {
        var answer: String = ""
        var mode = 0
        
        for (i in code.indices){
            if(code[i] == '1'){
                mode = if(mode == 1) 0 else 1
            }
            else{
                if((i%2==0 && mode == 0 )|| (i%2==1 && mode == 1)){
                    answer += code[i]
                }
            }
        }
        
        return if (answer.isEmpty()) "EMPTY" else answer

    }
}