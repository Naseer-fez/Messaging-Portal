import numpy as np
import os
import re
import logging
import sys
import base64
import pickle
np.set_printoptions(threshold=sys.maxsize)


class Encriptions:
    def __init__(self,message:None,key):
        random_bytes = os.urandom(4)
        self.key=4239798657
        self.key=key
        self.message=message
        self.messagespliter()
        self.randomvalues()
        self.usermessage()
        self.finaloutput()
        pass
    def messagespliter(self):
        self.word_list = self.message.split()
        self.words=[self.AssicConvertion(values) for values in self.word_list]
        self.words=self.xor(word=self.words)
        pass
    def AssicConvertion(self,word):
        AssicValues=[ord(values) for values in word]
        return AssicValues
    
    def xor(self,word):
        xor_values=[]
        for outterword in ((word)):
            singleword=[]
            for innerword in outterword:
                result=(innerword^(self.key)%127)& 0xFF
                singleword.append(result)
            xor_values.append(singleword)
        return xor_values
        pass 
    def increasingtheword(self,word):
        np.random.seed(len(word))
        wordlen=len(word)
        expanded_len = wordlen * 256 if wordlen > 0 else 1
        newword=[None]*expanded_len
        i=0
        shuffled_indices = np.random.permutation(expanded_len)
        combination=[self.Allcombine,word]
        check=0
        remaining = wordlen
        realinfo=[]
        next_char_idx = 0
        for ra in shuffled_indices:
            inc=int(ra)
            value=ra%2
            if (value == 1) and (remaining > 0):
                newword[inc] = int(word[next_char_idx])
                realinfo.append(inc)
                next_char_idx += 1
                remaining -= 1
            else:
                newword[inc] = int(np.random.choice(self.Allcombine))
            
        fin=0
        for k in range(len(word)):
            if(newword[fin] is None):
                newword[fin]=int(np.random.choice(combination[0]))
                check=check+1 
            fin=fin+1
        return newword,realinfo
        
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
    
    def usermessage(self):
        self.messagespliter()
        self.randomvalues()
        self.messages=[]
        self.realinfo=[]
        for i in range(len(self.words)):
            result = self.increasingtheword(self.words[i])
            self.messages.append(result[0])
            self.realinfo.append(result[1]) 
        
        self.encymes=self.messages
    
    def write_hex_data(self,data,file,mode):
        self.usermessage()
        if mode=='wb':
            try:
                encode=base64.b64encode(pickle.dumps(data))
            except Exception as e:
                pass
            basedata=encode
        else:
            basedata=str(data)
        self.log_to_file(basedata,file,mode)
        
    def log_to_file(self,data, filename,mode):
        try: 
            with open(filename,mode) as file:
                file.write(data)
        except Exception as e:
            print(e)
            pass
        
    def finaloutput(self):
        self.usermessage()
        self.write_hex_data(data=self.messages,file="Encription_Data.log",mode='wb')
def seedcalculator(key):
    x = key & 0xFFFFFFFF
    x ^= (x << 13) & 0xFFFFFFFF
    x ^= (x >> 17)
    x ^= (x << 5) & 0xFFFFFFFF
    return

if(__name__=="__main__"):
    text=' '
    key=42
    np.random.seed(seedcalculator(key))
    Encriptions(text,key)