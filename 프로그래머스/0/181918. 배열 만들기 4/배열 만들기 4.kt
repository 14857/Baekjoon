// 배열 만들기
// array에서 마지막 원소 접근 ; arr.last() 또는 arr[arr.size - 1]
// 마지막 원소 제거하기 : stk.dropLast(1) -> 새 배열을 만들어 반환하는 방식

class Solution {
    fun solution(arr: IntArray): IntArray {
        var stk: IntArray = intArrayOf()
        
        var i = 0
        
        while(i < arr.size){
            if(stk.size == 0){
                stk += arr[i]
                i += 1
            }
            else if(stk.size != 0 && stk.last() < arr[i]){
                stk += arr[i]
                i += 1
            }
            else if(stk.size != 0 && stk.last() >= arr[i]){
                // 마지막 원소 제거 -> 새 배열을 만들어 반환
                stk = stk.dropLast(1).toIntArray()
            }
        }
        
        return stk
    }
}