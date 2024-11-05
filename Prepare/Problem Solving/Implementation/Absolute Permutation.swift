import Foundation

/*
 * Complete the 'absolutePermutation' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 */

func absolutePermutation(n: Int, k: Int) -> [Int] {
    var results: [Int] = [Int]()
    var isUpper: Bool = false
    
    if k == 0 { return Array(1 ... n) }
    
    for number in 0 ... n - 1 {        
        if number % k == 0 { isUpper = !isUpper }
        
        if isUpper { results.append((number + 1) + k) }
        else { results.append((number + 1) - k) }
    
        if results.last! > n { return [-1] }
    }
    return results
}


let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let t = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

for tItr in 1...t {
    guard let firstMultipleInputTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }
    let firstMultipleInput = firstMultipleInputTemp.split(separator: " ").map{ String($0) }

    guard let n = Int(firstMultipleInput[0])
    else { fatalError("Bad input") }

    guard let k = Int(firstMultipleInput[1])
    else { fatalError("Bad input") }

    let result = absolutePermutation(n: n, k: k)

    fileHandle.write(result.map{ String($0) }.joined(separator: " ").data(using: .utf8)!)
    fileHandle.write("\n".data(using: .utf8)!)
}
