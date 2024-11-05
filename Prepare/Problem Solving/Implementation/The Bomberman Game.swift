import Foundation

/*
 * Complete the 'bomberMan' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. STRING_ARRAY grid
 */

func bomberMan(n: Int, grid: [String]) -> [String] {
    // Write your code here    
    var currentGrid: [[UInt8]] = grid.map{ [UInt8]($0.utf8) }
    var results: [[[UInt8]]] = [currentGrid]
    
    let resultIndex: Int = abs((n % 4) - 1)
    let allBombs: [[UInt8]] = [[UInt8]](repeating: [UInt8](repeating: 79, count: currentGrid.first!.count), count: currentGrid.count) 
    
    if n == 1 {
        return grid
    }
    
    if resultIndex % 2 == 1 {
        return allBombs.map{ String(bytes: $0, encoding: String.Encoding.utf8)! }
    }
    
    while(true) {
        var result: [[UInt8]] = allBombs 
        for index1 in 0 ... currentGrid.count - 1 {
            for index2 in 0 ... currentGrid[index1].count - 1 {
                if currentGrid[index1][index2] == 79 {
                    if index2 - 1 >= 0 {
                        result[index1][index2 - 1] = 46
                    }
                    if index2 + 1 <= currentGrid[index1].count - 1 {
                        result[index1][index2 + 1] = 46
                    }

                    if index1 > 0 {
                        result[index1 - 1][index2] = 46
                    }
                    if index1 + 1 <= currentGrid.count - 1 {
                        result[index1 + 1][index2] = 46
                    }       
                    result[index1][index2] = 46
                }
            }
        }
        
        if results.firstIndex(where: { $0 == result }) != nil {
            break
        }
        results.append(result)
        currentGrid = result
    }
    
    if results.count > 2 {
        results.removeFirst()
        results.swapAt(0, 1)
    }
            
    return results[resultIndex / 2].map{ String(bytes: $0, encoding: String.Encoding.utf8)! }
}


let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let firstMultipleInputTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }
let firstMultipleInput = firstMultipleInputTemp.split(separator: " ").map{ String($0) }

guard let r = Int(firstMultipleInput[0])
else { fatalError("Bad input") }

guard let c = Int(firstMultipleInput[1])
else { fatalError("Bad input") }

guard let n = Int(firstMultipleInput[2])
else { fatalError("Bad input") }

var grid = [String]()

for _ in 1...r {
    guard let gridItem = readLine() else { fatalError("Bad input") }

    grid.append(gridItem)
}

guard grid.count == r else { fatalError("Bad input") }

let result = bomberMan(n: n, grid: grid)

fileHandle.write(result.joined(separator: "\n").data(using: .utf8)!)
fileHandle.write("\n".data(using: .utf8)!)
