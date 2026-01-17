// toTypedArray() : List<T> → Array<T>로 변환

class Solution {
    fun solution(myStr: String): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        var lst = myStr.split("a", "b", "c").filter { it.isNotEmpty() } // 리스트 타입(변환 필요)
        
        if(lst.isEmpty()){
            answer = arrayOf("EMPTY")
        }else{
            answer = lst.toTypedArray()
        }
        
        return answer
    }
}