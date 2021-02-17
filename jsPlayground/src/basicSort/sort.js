function swap(arr, i, j) {
    let tem = arr[i]
    arr[i] = arr[j]
    arr[j] = tem
}

//  稳定性: 排序前后相同元素的相对位置不变，则称排序算法是稳定的；否则排序算法是不稳定的。

/**
 * @description 
 *  - time complexity: O(n^2)
 *  - best time complexity: O(n)
 *  - stability: yes
 */

//  
function bubbleSort(arr, asc = true) {

    // i表示数组末尾处, 排好顺序的元素
    for (let i = 0, len = arr.length; i < len; i++) {
        for (let j = 0; j < len - 1 - i; j++) {
            if (asc) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                }
            } else {
                if (arr[j] < arr[j + 1]) {
                    swap(arr, j, j + 1);
                }
            }

        }
    }
}


// 图解: https://www.jianshu.com/p/5223afa8796c
// 每次选择一个位置来把适合的元素放在该位置
function selectSort(arr) {
    for (let i = 0, len = arr.length; i < len; i++) {
        //  用于记录需要移动的索引
        let k = i;
        for (let j = i; j < len; j++) {
            if (arr[j] < arr[k]) {
                k = j;
            }
        }

        if (k !== i) {
            swap(arr, i, k)
        }

    }
}


// 每次在已排序的序列中对于 元素 找到一个合适的位置
function insertSort(arr) {
    for (let i = 1, len = arr.length; i < len; i++) {
        // 从后往前一次和当前元素比较, 交换位置
        for (let j = i; j > 0; j--) {
            if (arr[j] < arr[j - 1]) {
                swap(arr, j, j - 1)
            } else break
        }
    }
}