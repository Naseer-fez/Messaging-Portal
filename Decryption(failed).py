import numpy as np 
import os
import re
import logging
import sys
import base64
import pickle
# from  Encriptions import Encriptions 

np.random.seed(42)
class Decryption:
    def __init__(self):
        self.key=2
        self.filesopening()
        self.converthing()
        self.decoingthespcaes()
        self.randomvalues()
        # self.findingtherealindices(0)
        self.findingingthewords()
        self.performing()
        self.final()
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
            # print(decoded_string)
        except Exception as e:
            # raise Exception("SOMETHING IS WORNG ")
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
                # print((self.decoded_string))
                #i got the complete data
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
    def decoingthespcaes(self):
        # self.decoded_string=np.array(self.decoded_string)
        # print(chr(self.decoded_string[0][0]))
        self.lenofwords=[]
        for i in range(len(self.decoded_string)):
            self.lenofwords.append(int(len(self.decoded_string[i])/256))        
        # print(self.lenofwords)
        self.shuffled_indices=[]
        for i in range(len(self.lenofwords)):
            self.shuffled_indices.append(np.random.permutation((self.lenofwords[i])*256))
        # self.shuffled_indices=np.array(self.shuffled_indices)
        # print((self.shuffled_indices[0])) i got the eariler array 
        pass
    def findingingthewords(self):
        self.indices=[]
        for i in  ((0,1)):#just hardcode it now
            self.indices.append(self.findingtherealindices(i))    
        # print(self.indices)
    def findingtherealindices(self,wordincidecs:int):
        self.randomvalues()
        self.decoingthespcaes()
        # print((self.shuffled_indices))
        # wordlen=[(self.lenofwords/256) for v in range(len(self.lenofwords))]
        # print(len(self.shuffled_indices[0]))
        wordlen=self.lenofwords[wordincidecs]
        word=[' ']*wordlen
        print(len(word))
        combination=[self.Allcombine,word]
        i=0
        realinfo=[]
        np.random.seed(wordlen)
        index=0
        check=0
        while((i<=len(word))):
            ra=np.random.choice(self.shuffled_indices[wordincidecs])
            
            if(self.shuffled_indices[wordincidecs][ra]!=-1):
                value=np.random.choice((1,0))
                if((value==1)&(wordlen!=0)):
                    character=combination[value][(self.lenofwords[wordincidecs])-wordlen]
                    wordlen=wordlen-1
                    word[index]=ra
                    index=index+1
            i=i+1
            pass
        # print(check==wordlen)
        return (word)
        pass
    def performing(self):
        # print(self.indices)
        # print(self.decoded_string[0][235])
        self.deency=[]
        for i in range (len(self.indices)):
            z=[]
            for j in range(len(self.indices[i])):
                real_index = self.indices[i][j]
                z.append(real_index^(self.key % 127))
                # z='0'
            self.deency.append(z)   
        # print(self.deency) i got the word now time for convertions
    def final(self):
        word=[]
        for i in range(len(self.deency)):
            cpyword=[]
            for j in range(len(self.deency[i])):
                cpyword.append(chr(self.deency[i][j]))
            word.append(cpyword)
        print(word)            
        






if __name__=="__main__":
    Decryption()