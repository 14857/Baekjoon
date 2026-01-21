class Solution {
    fun solution(order: Array<String>): Int {
        var answer: Int = 0
        
        var americano = listOf("iceamericano", "americanoice","hotamericano", "americanohot","americano","anything")
        var latte = listOf("icecafelatte", "cafelatteice","hotcafelatte", "cafelattehot","cafelatte")
        
        for(i in order){
            if (i in americano) answer += 4500
            else if(i in latte) answer += 5000
        }
        
        return answer
    }
}