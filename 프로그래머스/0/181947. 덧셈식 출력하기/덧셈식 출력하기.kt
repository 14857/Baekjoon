fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    var ans : Int = a + b
    println("$a + $b = $ans")
}