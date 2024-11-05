import Foundation

/*
 * Complete the 'stones' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER a
 *  3. INTEGER b
 */

func stones(n: Int, a: Int, b: Int) -> [Int] {
    // Write your code here
    guard n > 1 else {
        return []
    }
    var results: Set<Int> = []
    for nB in 0..<n {
        let sum = nB * b + (n-nB-1) * a
        results.insert(sum)
    }
    return results.sorted()
}


let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let T = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

for TItr in 1...T {
    guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
    else { fatalError("Bad input") }

    guard let a = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
    else { fatalError("Bad input") }

    guard let b = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
    else { fatalError("Bad input") }

    let result = stones(n: n, a: a, b: b)

    fileHandle.write(result.map{ String($0) }.joined(separator: " ").data(using: .utf8)!)
    fileHandle.write("\n".data(using: .utf8)!)
}
