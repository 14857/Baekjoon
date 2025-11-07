// 가로로 택배 상자를 w개씩
// 인덱스 짝수인 경우 정방향, 홀수인 경우 역방향
// 마지막줄 일부만 채워지고 앞은 0으로 채우기

// 층 수 확인하기 특정 숫자가 존재하는 리스트의 인덱스와 전체 인덱스의 차이
// 해당 맨 윗층이 0인 경우 answer에서 1 빼주기

class Solution {
    fun solution(n: Int, w: Int, num: Int): Int {
        var answer: Int = 0
        

        val boxes = (1..n).chunked(w).map { it.toMutableList() }.toMutableList()
        val pad = MutableList(w - boxes.last().size) { 0 }

        boxes[boxes.lastIndex] = if (boxes.size % 2 == 0) 
            (pad + boxes.last()).toMutableList()
        else
            (boxes.last() + pad).toMutableList()
            
        for (i in 1 until boxes.size-1 step 2){
            boxes[i] = boxes[i].reversed().toMutableList()
        }
            
        print(boxes)
        
        
        for (i in boxes){
            if (num in i){
                answer = boxes.size - (boxes.indexOf(i))
               // println(boxes.indexOf(i))
                println(answer)
               var lastindex = boxes.lastIndex
               var numindex = i.indexOf(num)
               
              // print(boxes[lastindex][numindex])
               
               if (boxes[lastindex][numindex] == 0){
                   answer -= 1
               }
            }
        }

        
        return answer
    }
}