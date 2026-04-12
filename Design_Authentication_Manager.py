class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.am = dict()
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        
        self.am[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        
        if(tokenId in self.am and currentTime < self.am[tokenId]):
            self.am[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        
        count = 0
        for token, expiry_time in self.am.items():
            if(currentTime < expiry_time):
                count += 1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)