fun main(args: Array<String>) {
		val input = readLine()!!.split(' ')
    val s1 = input[0]
    val a = input[1]!!.toInt()
    
    var ans :String = ""
    
    for (i in 0 until a){
        ans += s1
    }
    
    println("$ans")
}