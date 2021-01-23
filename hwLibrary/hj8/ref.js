var count;
while (count = readline()) {
    printAll(count);
}
function printAll(n) {
    var obj = {};
    while (n--) {
        var str = readline().split(" ");
        if (!obj[str[0]]) {
            obj[str[0]] = str[1];
        } else {
            obj[str[0]] = parseInt(obj[str[0]]) + parseInt(str[1]);
        }
    }
    Object.keys(obj).forEach(key => { console.log(key, obj[key]) });
}