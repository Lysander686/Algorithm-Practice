function* count() {
    let saleList = [3, 7, 5]
    for (let i = 0; i < saleList.length; i++) {
        yield saleList[i]
    }
}


let myArr = count()

console.log(myArr.next());
