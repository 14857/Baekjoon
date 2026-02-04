// ingredient의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미 
// 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장 -> 1 2 3 1
// 스택 이용하기

class Solution {
    fun solution(ingredient: IntArray): Int {
        var answer: Int = 0
        var stack = mutableListOf<Int>()
        
        for(i in ingredient){
            stack.add(i)
            
            if(stack.size >= 4){
                val n = stack.size
                if(stack[n-4] == 1 && stack[n-3] == 2 && stack[n-2] == 3 && stack[n-1] == 1){
                    repeat(4) {
                        stack.removeAt(stack.lastIndex)
                    }
                    answer++
                }
            }   
        }
        
        return answer
    }
}