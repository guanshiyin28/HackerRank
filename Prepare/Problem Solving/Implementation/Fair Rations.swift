import Foundation

/*
 * Complete the 'fairRations' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts INTEGER_ARRAY B as parameter.
 */

func fairRations(B: [Int]) -> String {
    // Write your code here
    var oddIndex: [Int] = [Int]()
    var oddDict: [Int: Int] = [:]
    var steps: Int = 0
    
    for index in 0 ... B.count - 1 {
        if B[index] % 2 == 1 {
            oddIndex.append(index)
            oddDict[index] = index
        }
    }
    
    if oddIndex.count % 2 == 1 { return "NO" }    
    
    while(oddIndex.count > 1) {
      var currentOddIndex: Int = oddIndex.first!
      steps += 2
      let nextOddIndex: Int = currentOddIndex + 1
        if oddDict[nextOddIndex] == nil {
            oddIndex[0] = nextOddIndex
            oddDict.removeValue(forKey: currentOddIndex)
            oddDict[nextOddIndex] = nextOddIndex
            continue
        }
          
        while(currentOddIndex <= nextOddIndex) {
            oddIndex.removeFirst()
            oddDict.removeValue(forKey: currentOddIndex)
            currentOddIndex += 1
        }
    }
        
    return String(steps)
}

let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let N = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let BTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }

let B: [Int] = BTemp.split(separator: " ").map {
    if let BItem = Int($0) {
        return BItem
    } else { fatalError("Bad input") }
}

guard B.count == N else { fatalError("Bad input") }

let result = fairRations(B: B)

fileHandle.write(result.data(using: .utf8)!)
fileHandle.write("\n".data(using: .utf8)!)
