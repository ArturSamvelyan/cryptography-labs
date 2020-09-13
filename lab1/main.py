import string

class Cypher:
    def __init__(self, alphabet = None):
        if not alphabet:
            self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            self.alphabet = alphabet
        self.n = len(self.alphabet)
        # s2i = symbol to index
        self.s2i = {c:idx for (c, idx) in zip(self.alphabet, range(len(self.alphabet)))}
        # i2s = index to symbol
        self.i2s = {idx:c for (c, idx) in self.s2i.items()}


class Caesar(Cypher):
    def __init__(self, alphabet = None):
        super().__init__(alphabet)

    def string_to_vec(self, text: str):
        res = []
        for c in text:
            res.append(self.s2i[c])
        return res

    def vec_to_string(self, vec):
        res = ""
        for i in vec:
            res += self.i2s[i]
        return res

    def encrypt(self, text: str, key: int):
        vec = self.string_to_vec(text)
        encoded = list(map(lambda x: (x+key)%self.n, vec))
        return self.vec_to_string(encoded)

    def decrypt(self, text: str, key: int):
        vec = self.string_to_vec(text)
        decoded = list(map(lambda x: (x+(self.n-key))%self.n, vec))
        return self.vec_to_string(decoded)


class Vizhener(Cypher):
    def __init__(self, alphabet = None):
        super().__init__(alphabet)

    def encrypt(self, text:str, key:str):
        i = 0
        m = len(key)
        res = ""
        for c in text:
            if c == ' ' or c == '\n':
                res += c
            else:
                c_num = (self.s2i[c] + self.s2i[key[i]])%self.n
                res += self.i2s[c_num]
            # in order to step circularly on every char in key
            i = (i + 1)%m
        return res

    def decrypt(self, text:str, key:str):
        i = 0
        m = len(key)
        res = ""
        for c in text:
            if c == ' ' or c == '\n':
                res += c
            else:
                c_num = (self.s2i[c] + self.n - self.s2i[key[i]])%self.n
                res += self.i2s[c_num]
            # in order to step circularly on every char in key
            i = (i + 1)%m
        return res




def main():
    # Initialization
    full_name = "ARTUR SAMVELYAN"
    K = (72 + 25 + 15) % 26

    #print("Caesar:")
    #print("K: ", K)
    #caesar_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    #crypter = Caesar(caesar_alphabet)
    #encrypted = crypter.encrypt(full_name, K)
    #decrypted = crypter.decrypt(encrypted, K)
    #print("Encrypted:", encrypted)
    #print("Decrypted:", decrypted)

    print("Vizhener: ")
    K = "SAMVELYAN"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890[],.()-|\/"
    crypter = Vizhener(alphabet)

    with open('var_8.txt', 'r') as f:
        text = f.read()

    print(text)

    encrypted = crypter.encrypt(text, K)

    with open('encrypted_8.txt', 'w') as f:
        f.write(encrypted)

    decrypted = crypter.decrypt(encrypted, K)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)





if __name__ == '__main__':
    main()
