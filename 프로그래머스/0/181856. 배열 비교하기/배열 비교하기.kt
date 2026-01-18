// 두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
// 배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.

// arr2가 크다면 -1 / arr1이 크다면 1 /  두 배열이 같다면 0

class Solution {
    fun solution(arr1: IntArray, arr2: IntArray): Int {
        var answer: Int = -1
        
        if(arr1.size > arr2.size){ answer = 1}
        else if(arr1.size == arr2.size){
            if(arr1.sum() > arr2.sum()){
                answer = 1
            }else if(arr1.sum() == arr2.sum()){ answer = 0}
        }
        
        
        return answer
    }
}