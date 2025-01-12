from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keyring = {0}
        
        # Verificamos si hay una habitación cuyo único acceso es su propia llave
        for i, room in enumerate(rooms):
            print(i, room, keyring)
            if len(room) == 1 and room[0] == i:
                return False
        
        keyring.update([item for room in rooms for item in room])
        visitedRooms = set(range(len(rooms)))
    
        if keyring == visitedRooms:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    rooms = [[1],[1]]
    print(solution.canVisitAllRooms(rooms)) 
