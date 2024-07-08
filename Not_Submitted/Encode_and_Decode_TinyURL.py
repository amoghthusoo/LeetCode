import hashlib as hl

class Codec:

    def __init__(self):
        self.map_dict = {}

    def getHash(self, s):
        return hl.md5(s.encode()).hexdigest()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
         
        url_hash = "http://tinyurl.com/" + self.getHash(longUrl)
        self.map_dict[url_hash] = longUrl

        return url_hash
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return self.map_dict[shortUrl]




