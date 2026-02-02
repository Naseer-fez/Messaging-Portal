import Encriptions as en
import Decryption as de
import secrets

def generate_integer_key(bits=256):
    return int.from_bytes(secrets.token_bytes(bits // 10), 'big')

key = generate_integer_key()

text="""import numpy as np
import os
import re
import logging
import sys
import base64
import pickle


class Decryption:
    def __init__(self,key):
        self.key=key
        self.filesopening()
        self.converthing()
        self.randomvalues()
        self.decodingspaces()
        pass
    def filesopening(self):
        try:
            with open("Encription_Data.log",'r') as file:
                self.data=file.read()
        except FileNotFoundError as e:
            print("File data not found ")
        except Exception as e:
            print(f"The error is {e}")
        finally:
            pass
            
    def converthing(self):
        try:
            raw=base64.b64decode(self.data.encode("utf-8"))
            self.decoded_string=pickle.loads(raw)
        except Exception as e:
            print(f"Error {e}")
            pass
        finally:
            try:
                with open("Test.log",'w') as file:
                    file.write(str(self.decoded_string))
            except Exception as c:
                print(f"Error {c}")
                pass
            finally:
                pass
    def randomvalues(self):
        Allnumbers="0123456789"
        Allnumbers=[ord(values) for values in Allnumbers]
        Small="abcdefghijklmnopqrstuvwxyz"
        Small=[ord(values) for values in Small]
        Characters="!@#$^&*()_+-=[]{}|;:',.<>?/`~"
        Characters=[ord(values) for values in Characters]
        Capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Capital=[ord(values) for values in Capital]
        self.Allcombine=Allnumbers+Capital+Small+Characters
        pass
    def decodingspaces(self):
        self.tostorelen=[int(len(self.decoded_string[i])/256) for i in range(len(self.decoded_string))]
        self.shuffled_indices=[]
        for i in range(len(self.tostorelen)):
            np.random.seed(self.tostorelen[i])
            self.shuffled_indices.append(np.random.permutation((self.tostorelen[i])*256))
        pass
        self.indicies=[]
        for i in range(len(self.tostorelen)):
            z=self.findingtherealindices(i)
            self.indicies.append(z)
        self.performing()
    def findingtherealindices(self,inc):
        np.random.seed(self.tostorelen[inc])
        wordlen=self.tostorelen[inc]
        word=[' ']*(wordlen)
        perm = np.random.permutation(wordlen * 256 if wordlen > 0 else 1)
        combination=[self.Allcombine,word]
        i=0
        index=check=0
        remaining = wordlen
        real_positions = []
        for ra in perm:
            ra = int(ra)
            value = ra % 2
            if value == 1 and remaining > 0:
                real_positions.append(ra)
                remaining -= 1
            if remaining == 0:
                break
        return real_positions
    def performing(self):
        self.deency=[]
        for i in range(len(self.indicies)):
            z=[]
            for j in ((self.indicies[i])):
                realind=j
                z.append(self.decoded_string[i][j])
            self.deency.append(z)
        self.final()
    def final(self):
        xor_key = self.key % 127
        words=[]
        for arr in self.deency:
            decoded_chars = [(c ^ xor_key) for c in arr]
            word = "".join(chr(x) for x in decoded_chars)
            words.append(word)
        final_message = " ".join(words)
        print(final_message)
        pass
def seedcalculator(key):
    x = key & 0xFFFFFFFF
    x ^= (x << 13) & 0xFFFFFFFF
    x ^= (x >> 17)
    x ^= (x << 5) & 0xFFFFFFFF
    return x
if __name__=="__main__":
    key=42
    np.random.seed(seedcalculator(key))
    Decryption(key)
    print("Done")"""
en.Encriptions(text,key)

de.Decryption(key=key)

