// dropLast() : List<T>, MutableList<T>, Array<T>, IntArray 등 모두 사용 가능 / 반환 타입은 List<Int>

class Solution {
    fun solution(arr: IntArray, flag: BooleanArray): IntArray {
        var answer: IntArray = intArrayOf()
        
        for(idx in arr.indices){
            if (flag[idx] == true){
                repeat(arr[idx]*2){
                    answer += arr[idx]
                }
            }else{
                answer = answer.dropLast(arr[idx]).toIntArray()
            } 
            // 확인용
            // print(arr[idx])
            // println(answer.contentToString())
        }
        
        return answer
    }
}