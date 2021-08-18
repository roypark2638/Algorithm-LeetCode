/*
 Write a function that takes in an array of words and returns the smallest array of characters needed to form all of the words. The characters don't need to be in any particular order.
 
 For example, the characters ["y","r","o","u"] are needed to form the words ["your", "you", "or", "yo"].
 
 Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.
 */

/*
 O(n * I)time | O(c) space - where n is the number of words, I is the length of the longest word, and c is the number of unique characters across al words.
 
 1. Create two hashMaps. One for currentWordHash and one for staticWordHash
 2. loop the words
    3. loop single word for each char
        * if there is no word, then create on with value 1
        * if there is word, then increment value by 1
    4. compare the value to staticWordHash and update the value
        * from the currentHashMap, loop all the elements and if the element exist, then check the value. If that value < staticWordHash's value then skip, if that value > staticWordHash's value, then update the value
    5. Reset the currentWordHash
 6. loop the staticWordHash to create new array for the result and return.
 */

func minimumCharactersForWords(_ words: [String]) -> [String] {
    var currentMap: [String: Int] = [:]
    var staticMap: [String: Int] = [:]
    
    for word in words {
        
        for char in word {
            let newWord = String(char)
            if currentMap[newWord] == nil {
                currentMap[newWord] = 1
            } else {
                currentMap[newWord]! += 1
            }
        }
        
        for (key, value) in currentMap {
            if staticMap[key] != nil {
                let staticValue = staticMap[key]!
                if staticValue < value {
                    staticMap[key] = value
                }
            } else {
                staticMap[key] = value
            }
        }
        
        currentMap.removeAll()
        
    }
    
    var result: [String] = []
    
    for (key, value) in staticMap {
        for _ in 0..<value {
            result.append(key)
        }
    }
    
    return result
}



