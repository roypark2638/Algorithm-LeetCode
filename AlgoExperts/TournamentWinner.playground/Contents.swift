// https://www.algoexpert.io/questions/Tournament%20Winner

/*
 There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces off against all other teams. Only two teams compete against each other at a time, and for each competition, one team is designated the home team, while the other team is the away team. In each competition there's always one winner and one loser; there are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that receives the most amount of points.
 
 Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition, write a function that returns the winner of the tournament. The input arrays are named competitions and results, respectively. The competitions array has elements in the form of [homeTeam, awayTeam], where each team is a string of at most 30 characters representing the name of the team. The results array contains information about the winner of each corresponding competition in the competitions array. Specifically, results[i] denotes the winner of competitions[i], where a 1 in the results array means that the home team in the corresponding the competition won and a 0 means that the away team won.
 
 It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once. It's also guaranteed that the tournament will always have at least two teams.
 
 Input:
 competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
 ]
 results = [0,0,1]
 
 Output:
 "Python"
 */

/*
 1. Create a map [String: Int]
 2. loop each competitions and increase winner's the point at the map
 3. return the highest score of the team
 
 Time: O(N)
 Space: O(M) where m is the number of the winner's teams
 */
let competitions = [
   ["HTML", "C#"],
   ["C#", "Python"],
   ["Python", "HTML"],
]
let results = [0,0,1]
let HOME_TEAM_WON = 1

func tournamentWinner(_ competitions: [[String]], _ results: [Int]) -> String {
    var hashMap: [String: Int] = [:]
    
    for index in competitions.indices {
        let gameResult = results[index] == 0 ? 1 : 0
        let winner = competitions[index][gameResult]
        if let _ = hashMap[winner] {
            hashMap[winner]! += 1
        } else {
            hashMap[winner] = 1
        }
    }
    
    if let highestScore = hashMap.values.max() {
        for (key, value) in hashMap {
            if value == highestScore {
                return key
            }
        }
    }
    
    return ""
}

tournamentWinner(competitions, results)
