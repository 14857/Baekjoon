// 특정 프로세스가 몇 번째로 실행되는지 반환

// 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
// 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
// 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
//   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        var answer = 0
        
        // (우선순위, 인덱스) 큐
        var queue = ArrayDeque<Pair<Int,Int>>()
        
        for(i in priorities.indices){
            queue.add(Pair(priorities[i],i))
        } 
        // println(queue)

        while(queue.isNotEmpty()){
            val cur = queue.removeFirst()
            println(cur)
            
            // 현재보다 높은 우선순위가 존재하는 경우
            if(queue.any{it.first > cur.first}){
                queue.addLast(cur)
                // println(queue)
            }else{
                answer++
                
                // 우선 순위 동일한 경우도 고려
                if(cur.second == location){
                    return answer
                }
            }
        }
        
        return answer
    }
}