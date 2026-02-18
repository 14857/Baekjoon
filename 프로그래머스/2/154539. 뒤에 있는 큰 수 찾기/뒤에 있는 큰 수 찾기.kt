// 뒷 큰수 : 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수
// 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열 반환
// 뒷 큰수가 존재하지 않는 원소는 -1

// 이중 for문 -> 시간초과 발생 => 스택으로 다시 풀기


class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer = IntArray(numbers.size)
        var stack = mutableListOf<Int>() // 스택
        
        // 뒤에서부터 찾기
        for(i in numbers.size-1 downTo 0){
            
            // 현재와 같거나 작은 값 제거
            while(stack.isNotEmpty() && stack.last() <= numbers[i]){
                stack.removeAt(stack.size-1) // 마지막 값 제거
            }
            
            // 뒷 큰수 결정하기
            answer[i] = if(stack.isEmpty()) -1 else stack.last()
            
            // 현재값 push
            stack.add(numbers[i])
            
        }
          
        return answer
    }
}