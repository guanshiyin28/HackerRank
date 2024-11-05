import Foundation

/*
 * Complete the 'twoPluses' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING_ARRAY grid as parameter.
 */

func calculatePossibleIndex(maxIndex: Int, median: Int, index: Int) -> Int {
    let factor = (index + median) / median
    let res = abs((((factor * median - median) * 2) - index) - (maxIndex % 2) * index / median)
    
    return res
}

func twoPluses(grid: [String]) -> Int {
    // Write your code here
    let grids: [[UInt8]] = grid.map{ [UInt8]($0.utf8) }
    let hIndexCount: Int = grids.first!.count - 1
    let vIndexCount: Int = grids.count - 1
    let hIndexMedian: Int = (hIndexCount / 2) + (hIndexCount % 2)
    let vIndexMedian: Int = (vIndexCount / 2) + (vIndexCount % 2)
    
    var isVerticalValid: Bool = false
    var isHorizontalValid: Bool = false
    var totalGridFound: [Int] = [Int]()
    var coordinates: [[Int]] = [[Int]]()
    var isNeedToCreateCoorBatch: Bool = true
    var possibleIndexes: [Int] = [Int]()
    var offset: Int = 0
    
    for vIndex in 1 ... vIndexCount - 1 {
        let vPossibleIndex: Int = calculatePossibleIndex(maxIndex: vIndexCount, median: vIndexMedian, index: vIndex)
        possibleIndexes.append(vPossibleIndex == 0 ? vIndex : vPossibleIndex)
        
        for hIndex in 1 ... hIndexCount - 1 {
                
            if grids[vIndex][hIndex] == 71 {
                possibleIndexes.append(calculatePossibleIndex(maxIndex: hIndexCount, median: hIndexMedian, index: hIndex) )
                offset = possibleIndexes.min()!
                
                while(offset >= 1) {
                    let minVIndex: Int = vIndex - offset
                    let maxVIndex: Int = vIndex + offset
                    let minHIndex: Int = hIndex - offset
                    let maxHIndex: Int = hIndex + offset
                        
                    // check vertical validity
                    for vIndexPossible in minVIndex ... maxVIndex { 
                        let multiplier: Int = hIndex > 9 ? 100 : 10                   
                        let coor: Int = vIndexPossible * multiplier + hIndex
                        if isNeedToCreateCoorBatch {
                            coordinates.append([coor])
                            isNeedToCreateCoorBatch = false   
                        } else {
                            coordinates[coordinates.count - 1].append(coor)
                        }
                        
                        if grids[vIndexPossible][hIndex] != 71 { break }

                        if vIndexPossible == maxVIndex {
                            isVerticalValid = true
                        }
                    }
                        
                    if !isVerticalValid { 
                        coordinates.popLast()
                        isNeedToCreateCoorBatch = true
                        offset -= 1
                        continue 
                    }
                    
                    // check horizontal validity
                    for hIndexPossible in minHIndex ... maxHIndex {
                        if hIndexPossible == hIndex { continue }
                        
                        let multiplier: Int = hIndexPossible > 9 ? 100 : 10
                        let coor: Int = vIndex * multiplier + hIndexPossible
                        coordinates[coordinates.count - 1].append(coor)
                        
                        if grids[vIndex][hIndexPossible] != 71 { break }
                                                
                        if hIndexPossible == maxHIndex {
                            isHorizontalValid = true
                        }   
                    }
                    
                    if isVerticalValid && isHorizontalValid {                        
                        totalGridFound.append(offset * 4 + 1)
                    } else {
                        coordinates.popLast()
                    }
                    
                    isNeedToCreateCoorBatch = true
                    offset -= 1
                }
                
                possibleIndexes.popLast()
                isVerticalValid = false
                isHorizontalValid = false    
            }
        }
        possibleIndexes.removeAll()
    }
    
    var highest: Int = 0
    var container: [Int] = [Int]()
        
    if totalGridFound.count == 0 {
        return 1
    }
    
    for index1 in 0 ... totalGridFound.count - 1 {
        for index2 in index1 ... totalGridFound.count - 1 {
            let candidates: [Int] = [totalGridFound[index1], totalGridFound[index2]]
            let total: Int = candidates.reduce(1) { $0 * $1 }
            if total > highest {
                container.append(contentsOf: coordinates[index1])
                container.append(contentsOf: coordinates[index2])
                let initialCount: Int = container.count
                container = Array(Set(container))
                if initialCount == container.count {
                    highest = total
                } 
                
                if initialCount != container.count && candidates.max()! > highest {
                    highest = candidates.max()!
                }
                container.removeAll()
            }
        }
    }
    
    return highest
}

let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let firstMultipleInputTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }
let firstMultipleInput = firstMultipleInputTemp.split(separator: " ").map{ String($0) }

guard let n = Int(firstMultipleInput[0])
else { fatalError("Bad input") }

guard let m = Int(firstMultipleInput[1])
else { fatalError("Bad input") }

var grid = [String]()

for _ in 1...n {
    guard let gridItem = readLine() else { fatalError("Bad input") }

    grid.append(gridItem)
}

guard grid.count == n else { fatalError("Bad input") }

let result = twoPluses(grid: grid)

fileHandle.write(String(result).data(using: .utf8)!)
fileHandle.write("\n".data(using: .utf8)!)
