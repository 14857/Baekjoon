class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
  
        for(i in num_list){
            
            var num = i
            
            while(num != 1){
                if(num % 2 == 0){ num = num/2}
                else{num = (num-1)/2}
                
                answer += 1
            }
        }
        
        return answer
    }
}