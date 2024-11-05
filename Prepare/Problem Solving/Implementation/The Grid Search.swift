import Foundation

/*
 * Complete the 'gridSearch' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING_ARRAY G
 *  2. STRING_ARRAY P
 */

func gridSearch(G: [String], P: [String]) -> String {
    // Write your code here
    
    var pIndex: Int = 0
    var gIndex: Int = 0
    var prevIndex: Int = -1
    
    var set = Set<Character>()
    
    while(gIndex <= G.count - 1) {
        if let ranged = G[gIndex].range(of: P[pIndex], options: .regularExpression) {
            let index: Int = G[gIndex].distance(from: G[gIndex].startIndex, to: ranged.lowerBound)
                   
            if prevIndex != -1 && prevIndex != index { 
                let squeezed: String = G[gIndex - 1].filter{ set.insert($0).inserted }
                if squeezed.count != 1 {
                    pIndex = 0
                    prevIndex = -1
                    continue
                }
             }
            if pIndex == P.count - 1 { break } 
            if pIndex < P.count - 1 { pIndex += 1 } 
            if prevIndex == -1 { prevIndex = index }
            
        } else if (pIndex != 0) {
            pIndex = 0 
            continue 
        }

        gIndex += 1
    }
        
    return pIndex == P.count - 1 ? "YES" : "NO"
}

let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let t = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

for tItr in 1...t {
    guard let firstMultipleInputTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }
    let firstMultipleInput = firstMultipleInputTemp.split(separator: " ").map{ String($0) }

    guard let R = Int(firstMultipleInput[0])
    else { fatalError("Bad input") }

    guard let C = Int(firstMultipleInput[1])
    else { fatalError("Bad input") }

    var G = [String]()

    for _ in 1...R {
        guard let GItem = readLine() else { fatalError("Bad input") }

        G.append(GItem)
    }

    guard G.count == R else { fatalError("Bad input") }

    guard let secondMultipleInputTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }
    let secondMultipleInput = secondMultipleInputTemp.split(separator: " ").map{ String($0) }

    guard let r = Int(secondMultipleInput[0])
    else { fatalError("Bad input") }

    guard let c = Int(secondMultipleInput[1])
    else { fatalError("Bad input") }

    var P = [String]()

    for _ in 1...r {
        guard let PItem = readLine() else { fatalError("Bad input") }

        P.append(PItem)
    }

    guard P.count == r else { fatalError("Bad input") }

    let result = gridSearch(G: G, P: P)

    fileHandle.write(result.data(using: .utf8)!)
    fileHandle.write("\n".data(using: .utf8)!)
}
