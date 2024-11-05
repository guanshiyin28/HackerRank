import Foundation

/*
 * Complete the 'surfaceArea' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY A as parameter.
 */

func surfaceArea(A: [[Int]]) -> Int {
    // Write your code here
    let H: Int = A.count - 1
    let W: Int = A.first!.count - 1
    
    var totalSurface: Int = 0
    
    for index1 in 0 ... W {
        var lastNumberLeft = 0
        var lastNumberRight = 0
        
        for index2 in 0 ... H {
            // calculate left facing cube
            if A[index2][index1] > lastNumberLeft {
                totalSurface += A[index2][index1] - lastNumberLeft
            }
            lastNumberLeft = A[index2][index1] 
            
            // calculate right facing cube
            if A[H - index2][W - index1] > lastNumberRight {
                totalSurface += A[H - index2][W - index1] - lastNumberRight
            }
            lastNumberRight = A[H - index2][W - index1]
        }
    }
    
    
    for index1 in 0 ... H {
        var lastNumberFront = 0
        var lastNumberBack = 0
        
        for index2 in 0 ... W {
            // calculate front facing cube
            if A[index1][index2] > lastNumberFront {
               totalSurface += A[index1][index2] - lastNumberFront 
            }
            lastNumberFront = A[index1][index2]

            // calculate back facing cube
            if A[H - index1][W - index2] > lastNumberBack {
               totalSurface += A[H - index1][W - index2] - lastNumberBack 
            }
            lastNumberBack = A[H - index1][W - index2]
        }
    }
    
    return ((H + 1) * (W + 1)) * 2 + totalSurface
}

let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let firstMultipleInputTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }
let firstMultipleInput = firstMultipleInputTemp.split(separator: " ").map{ String($0) }

guard let H = Int(firstMultipleInput[0])
else { fatalError("Bad input") }

guard let W = Int(firstMultipleInput[1])
else { fatalError("Bad input") }

var A = [[Int]]()

for _ in 1...H {
    guard let ARowTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }

    let ARow: [Int] = ARowTemp.split(separator: " ").map {
        if let AItem = Int($0) {
            return AItem
        } else { fatalError("Bad input") }
    }

    guard ARow.count == W else { fatalError("Bad input") }

    A.append(ARow)
}

guard A.count == H else { fatalError("Bad input") }

let result = surfaceArea(A: A)

fileHandle.write(String(result).data(using: .utf8)!)
fileHandle.write("\n".data(using: .utf8)!)
