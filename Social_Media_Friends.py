from collections import deque

class SocialNetwork:
    def __init__(self):
        self.network = {}
    
    def add_user(self, user):
        if user not in self.network:
            self.network[user] = set()
    
    def add_connection(self, user1, user2):
        self.add_user(user1)
        self.add_user(user2)
        self.network[user1].add(user2)
        self.network[user2].add(user1)
    
    def suggest_friends(self, user):
        if user not in self.network:
            return []
        
        visited = set()
        queue = deque([user])
        friends = self.network[user]
        suggestions = {}
        
        while queue:
            current = queue.popleft()
            visited.add(current)
            
            for friend in self.network.get(current, []):
                if friend != user and friend not in friends:
                    if friend not in suggestions:
                        suggestions[friend] = 0
                    suggestions[friend] += 1
                
                if friend not in visited:
                    queue.append(friend)
                    visited.add(friend)
        
        sorted_suggestions = sorted(suggestions.items(), key=lambda x: -x[1])
        return [friend for friend, mutuals in sorted_suggestions]
    
    def display_network(self):
        for user, friends in self.network.items():
            print(f"{user}: {', '.join(friends)}")

# Example usage
if __name__ == "__main__":
    sn = SocialNetwork()
    sn.add_connection("Sawan", "Akshit")
    sn.add_connection("Sawan", "Gourav")
    sn.add_connection("Akshit", "Avneesh")
    sn.add_connection("Gourav", "Avneesh")
    sn.add_connection("Gourav", "Ritik")
    sn.add_connection("Ritik", "Aryan")
    sn.add_connection("Avneesh", "Ritik")
    
    print("Friend Suggestions for Sawan:", sn.suggest_friends("Sawan"))
    print("Friend Suggestions for Akshit:", sn.suggest_friends("Akshit"))
    print("Friend Suggestions for Ritik:", sn.suggest_friends("Ritik"))
    
    sn.display_network()
