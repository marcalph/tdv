
#O(n+k) time | O(n) space 
# where n number of rooms/ k number of keys
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]

        while queue:
            room = queue.pop(0)
            if room in visited: 
                continue
            visited.add(room)
            queue.extend(rooms[room])
                
        return len(visited) == len(rooms)