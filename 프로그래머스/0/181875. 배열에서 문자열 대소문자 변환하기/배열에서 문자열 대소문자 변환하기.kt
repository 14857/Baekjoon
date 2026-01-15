class Solution {
    fun solution(strArr: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        
        for(i in strArr.indices){
            if(i%2 == 0){ // 짝수인 경우 -> 모든 문자를 소문자로
                answer += strArr[i].lowercase()
            }else{// 홀수인 경우 -> 모든 문자를 대문자로
                answer += strArr[i].uppercase()
            }
        }
        
        return answer
    }
}