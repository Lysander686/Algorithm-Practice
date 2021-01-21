var str = readline()
var letter = readline()
var count = function (str, letter) {
    //将字符串和字母全部转换为小写
    str = str.toLowerCase()
    letter = letter.toLowerCase()
    var arr = []
    for (var i = 0; i < str.length; i++) {
        i = str.indexOf(letter, i)
        if (i == -1) {
            break
        }
        arr.push(i)
    }
    return arr.length
}
console.log(count(str, letter))