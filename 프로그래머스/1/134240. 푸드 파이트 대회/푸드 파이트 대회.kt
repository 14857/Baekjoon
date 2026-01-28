// 두 선수가 먹는 음식의 종류와 양이 같아야 하며, 음식을 먹는 순서도 같아야 합니다.
// 칼로리가 낮은 음식을 먼저 먹을 수 있게 배치
// 물 : 0

class Solution {
    fun solution(food: IntArray): String {
        var answer: String = ""
        
        for(i in 1 until food.size){
            repeat(food[i]/2){
                answer += i
            }
        }
        
        answer += "0" + answer.reversed()
        
        return answer
    }
}