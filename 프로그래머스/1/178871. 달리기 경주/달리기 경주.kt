class Solution {
    fun solution(players: Array<String>, callings: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        
        // 해시맵(기존 players.indexOf(i) 방식에서 시간초과 발생)
        val rankMap = mutableMapOf<String,Int>()
        
        for (i in players.indices){
            rankMap[players[i]] = i
        }
        
        for (name in callings){
            var cur = rankMap[name] ?: continue
            var prevName = players[cur-1]
            
            players[cur-1] = name
            players[cur] = prevName
            
            rankMap[name] = cur-1
            rankMap[prevName] = cur
        }
        //print(players.contentToString())
        
        answer = players
        
        return answer
    }
}