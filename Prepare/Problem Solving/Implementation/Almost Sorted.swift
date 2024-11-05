import Foundation

/*
 * Complete the 'almostSorted' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

func isSorted(arr: [Int]) -> Bool {
    for index in 1 ... arr.count - 1 {
        if arr[index] < arr[index - 1] {
             return false   
        }
    }
    return true
}

func reverseIt(arr: [Int], startIndex: Int, endIndex: Int) -> [Int] {
    let slicedArr: [Int] = Array(arr[startIndex ... endIndex])
    var arrTemp: [Int] = arr
    var index = slicedArr.count - 1

    while(index > -1) {
        arrTemp[startIndex + ((slicedArr.count - 1) - index)] = slicedArr[index]
        index -= 1
    }
    return arrTemp
}

func almostSorted(arr: [Int]) -> Void {
    // Write your code here
    var dict: [Int: Bool] = [:]
    var arrTemp: [Int] = arr
    var lastTrend: Bool?
    var resultWording: String = ""
    var decreaseIndex: [Int] = [Int]()
    var decreaseCount: Int = 0
    var increaseCount: Int = 0
    
    for index in 0 ... arr.count - 2 {
        let currElement: Int = arr[index]
        let nextElement: Int = arr[index + 1]
        let isUp: Bool = nextElement > currElement
        
        if (lastTrend != nil && lastTrend != isUp) || lastTrend == nil {
            dict[index + 1] = isUp
            lastTrend = isUp
        }
    }
    
    var arrayDict = dict.sorted(by: { $0.key < $1.key })
        
    if arrayDict.count == 1 && arrayDict.first!.value {
        print("yes")
        return
    }
    
    for index in 0 ... arrayDict.count - 1 {
        if !arrayDict[index].value {
            decreaseCount += 1
            decreaseIndex.append(arrayDict[index].key)
        }
        if arrayDict[index].value { increaseCount += 1 }
        
        if decreaseCount == 1 {
            arrTemp.swapAt(arrayDict[index].key - 1, arrayDict[index].key)
            resultWording = "yes\nswap \(arrayDict[index].key) \(arrayDict[index].key + 1)"
        }
        if decreaseCount == 2 {
            arrTemp.swapAt(decreaseIndex.first! - 1, decreaseIndex.last!)
            resultWording = "yes\nswap \(decreaseIndex.first!) \(decreaseIndex.last! + 1)"
        }
        if isSorted(arr: arrTemp) { 
            print(resultWording)
            return
        }
        
        if increaseCount == 2 { 
            arrTemp = reverseIt(arr: arr, startIndex: decreaseIndex.first! - 1, endIndex: arrayDict[index].key - 1)
            resultWording = "yes\nreverse \(decreaseIndex.first!) \(arrayDict[index].key)"
            
            if isSorted(arr: arrTemp) { 
                print(resultWording)
                return
            }
         }

        arrTemp = arr
    }
    
    print("no")
}

guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let arrTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }

let arr: [Int] = arrTemp.split(separator: " ").map {
    if let arrItem = Int($0) {
        return arrItem
    } else { fatalError("Bad input") }
}

guard arr.count == n else { fatalError("Bad input") }

almostSorted(arr: arr)
