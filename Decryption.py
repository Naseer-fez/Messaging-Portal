import numpy as np 
import os
import re
import logging
import sys
import base64
import pickle
# from  Encriptions import Encriptions 


class Decryption:
    def __init__(self,key):
        self.key=key
        self.filesopening()
        self.converthing()# this both are gonna oppen the file and decode thaat 
        self.randomvalues()
        self.decodingspaces()
        pass
    def filesopening(self):
        try:
            with open("Encription_Data.log",'r') as file:
                self.data=file.read()
                # print('done')
        except FileNotFoundError as e:
            print("File data not found ")
        except Exception as e:
            print(f"The error is {e}")
        finally:
            # print("hf")
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
        # self.tostorelen=[]
        self.tostorelen=[int(len(self.decoded_string[i])/256) for i in range(len(self.decoded_string))]
        self.shuffled_indices=[]
        # print(self.tostorelen)
        for i in range(len(self.tostorelen)):
            np.random.seed(self.tostorelen[i])
            self.shuffled_indices.append(np.random.permutation((self.tostorelen[i])*256))
        # print(len(self.shuffled_indices))   
        pass
        self.indicies=[]
        for i in range(len(self.tostorelen)):
            z=self.findingtherealindices(i)
            self.indicies.append(z)
        # print(self.indicies)  
        self.performing()  
    def findingtherealindices(self,inc):     
        np.random.seed(self.tostorelen[inc])
        wordlen=self.tostorelen[inc]
        word=[' ']*(wordlen)
        # print(wordlen)
        perm = np.random.permutation(wordlen * 256 if wordlen > 0 else 1)
        combination=[self.Allcombine,word]
        i=0
        index=check=0
        remaining = wordlen
        # while((i<len(word)*256)&(wordlen>0)):
            
        #     ra=np.random.choice(self.shuffled_indices[inc])
        #     if(self.shuffled_indices[inc][ra]!=-1):
        #         value=ra%2
        #         if((value==1)):
        #                 character=combination[value][(self.tostorelen[inc])-wordlen]
        #                 wordlen=wordlen-1
        #                 word[index]=ra
        #                 index=ra
        #                 # print(ra)
        #         elif(value==0):
                    
        #             pass
                
                
        #     i=i+1
        #     check=check+1
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
        # print(index)
        # return word
    def performing(self):
        
        self.deency=[]
        for i in range(len(self.indicies)):
            z=[]
            for j in ((self.indicies[i])):
                realind=j
                # print(realind)
                z.append(self.decoded_string[i][j])
            self.deency.append(z)
        self.final()
    def final(self):
        # print(self.deency)
        # # print((self.decoded_string))
        # pass
        xor_key = self.key % 127
        words=[]
        # for i in range(len(self.deency)):
        #     cpyword=[]
        #     for j in range(len(self.deency[i])):
        #         cpyword.append(chr(self.deency[i][j]))
        #     word.append(cpyword)
        # print(self.deency)
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
    print("Done")