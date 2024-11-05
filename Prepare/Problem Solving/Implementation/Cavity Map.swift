import Foundation

/*
 * Complete the 'cavityMap' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts STRING_ARRAY grid as parameter.
 */

func cavityMap(grid: [String]) -> [String] {
    // Write your code here
    if grid.first!.count < 3 { return grid }
    
    var gridUTF8: [[UInt8]] = grid.map{ [UInt8]($0.utf8) }
    
    let gridMaxIndex: Int = gridUTF8.count - 1
    let gridContentMaxIndex: Int = gridUTF8.first!.count - 1
    
    for index1 in 1 ... gridMaxIndex - 1 {
        for index2 in 1 ... gridContentMaxIndex - 1 {
            let currentGrid: UInt8 = gridUTF8[index1][index2]
            let isHValid: Bool = gridUTF8[index1][index2 - 1] < currentGrid && gridUTF8[index1][index2 + 1] < currentGrid
            let isVValid: Bool = gridUTF8[index1 - 1][index2] < currentGrid && gridUTF8[index1 + 1][index2] < currentGrid
            if isHValid && isVValid  {
                gridUTF8[index1][index2] = 88
                continue
            }
        }
    }
    
    return gridUTF8.map{ String(bytes: $0, encoding: String.Encoding.utf8) ?? "" }
}

let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

var grid = [String]()

for _ in 1...n {
    guard let gridItem = readLine() else { fatalError("Bad input") }

    grid.append(gridItem)
}

guard grid.count == n else { fatalError("Bad input") }

let result = cavityMap(grid: grid)

fileHandle.write(result.joined(separator: "\n").data(using: .utf8)!)
fileHandle.write("\n".data(using: .utf8)!)
