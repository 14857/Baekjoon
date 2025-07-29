fun main(args: Array<String>) {
    val s1 = readLine()!!
    var ans : String = ""
    
    for (i in s1.indices){
        if (s1[i].isLowerCase()){
            ans += s1[i].toUpperCase()
        }
        else{
            ans += s1[i].toLowerCase()
        }
    }
    
    println(ans)
}