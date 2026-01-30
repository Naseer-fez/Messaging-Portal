import numpy as np 
import os
import re
import logging
import sys
import base64
import pickle
np.set_printoptions(threshold=sys.maxsize)
# logging.basicConfig(
#     filename='Encription_Data.txt',  
#     filemode='w',            
#     level=logging.DEBUG,     
#     # format='%(asctime)s - %(levelname)s - %(message)s'
# )

class Encriptions:
    def __init__(self,message:None,key):
        random_bytes = os.urandom(4)
        self.key=4239798657
        self.key=key
        # self.key = int.from_bytes(random_bytes, byteorder='big')
        self.message=message
        # so i haev creyed a random crypthogrolica key now , 
        # print(key)
        # self.AssicConvertion()
        # self.xor()
        self.messagespliter()
        self.randomvalues()
        # self.increasingtheword(self.words[3])
        self.usermessage()
        self.finaloutput()
        pass
    def messagespliter(self):
        self.word_list = self.message.split()
        self.words=[self.AssicConvertion(values) for values in  self.word_list]
        self.words=self.xor(word=self.words)
        # print(self.words)
        pass
    def AssicConvertion(self,word):
        AssicValues=[ord(values) for values in word]
        return AssicValues
    
    def xor(self,word):
        # self.xorvalues=[(values)^((self.key)%127) for values in word]
        # self.xorvalues=[[(values)^((self.key)%127) for values in word] 
        #                 for wordlist in self.word_list]
        # print(len(word[]))
        # print(word)
        xor_values=[]
        # for singleword in range(len(word)):
        #     print(singleword)
        #     xor_values[singleword]=[(values)^((self.key)%127) for values in word[singleword]]
        for outterword in ((word)):
            singleword=[]
            for innerword in outterword:
                result=(innerword^(self.key)%127)& 0xFF
                singleword.append(result)
            xor_values.append(singleword)
            
            
        # print(xor_values)
        return xor_values
        
        
        # print(self.xorvalues)
        pass    
    def increasingtheword(self,word):
        np.random.seed(len(word))
        # print(len(word))
        # print((word))
        # self.xor()
        # print(len(self.message)*256)
        wordlen=len(word)
        expanded_len = wordlen * 256 if wordlen > 0 else 1
        newword=[None]*expanded_len
        # # print(len(newword))
        # newword[2]=word
        # print(newword)
        i=0
        
        # index=np.random.randint(low=1,high=((self.key)%len(newword)+1),size=len(newword))
        shuffled_indices = np.random.permutation(expanded_len)
        # allcom=
        # print(len(shuffled_indices))
        # print(len(newword))
        
        combination=[self.Allcombine,word]
        check=0
        remaining = wordlen
        realinfo=[]
        # while ((i<len(newword))):
        #     ra=np.random.choice(shuffled_indices)#what if iam try to use this insed the below one 
        #     # ra=shuffled_indices[i]
        #     # print(ra)
        #     if(shuffled_indices[ra]!=-1):
        #         value=ra % 2
        #         if (value==1 )&(wordlen>0):
        #             character=combination[value][len(word)-wordlen]
        #             wordlen=wordlen-1
        #             newword[ra]=character
        #             realinfo.append(int(ra))
        #             check=check+1
        #             # print(ra)
        #         elif(value==0):
        #             character=combination[value][ra%len(combination[0])]
        #             newword[ra]=character
        #             # check=check+1
        #         shuffled_indices[ra]=-1
        #     else:
        #         pass
        #     i=i+1
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
    
            # if(shuffled_indices[fin]!=-1):
            if(newword[fin] is None):
                newword[fin]=int(np.random.choice(combination[0]))
                
                check=check+1  
            fin=fin+1 
        # print(self.realinfo)
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
        # print(len(self.Allcombine))
        pass  
        
    
    def usermessage(self):
        self.messagespliter()
        self.randomvalues()
        # messages=[self.increasingtheword(value) for value in self.words]
        self.messages=[]
        self.realinfo=[]
        for i in range(len(self.words)):
             result = self.increasingtheword(self.words[i]) 
             self.messages.append(result[0])
             self.realinfo.append(result[1]) 
        
            
        # print((self.realinfo))
        # print(messag# self.encymess=np.array(self.encymess,dtype=object)
        self.encymes=self.messages
        # print(messages)
        
        # print(type(self.encymes))
    
    
    def write_hex_data(self,data,file,mode):
        self.usermessage()
        # bytes_data=
        # try:
        #     basedata=base64.b64decode(pickle.dumps(data))
        # except Exception as e:
        #     basedata=data
        # finally:
        #     self.log_to_file(basedata, file,mode)
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
        # logger = logging.getLogger(filename)  
        # logger.setLevel(logging.DEBUG)

        # # avoid duplicate handlers if function is called multiple times
        # if not logger.handlers:
        #     handler = logging.FileHandler(filename, mode='w')  # append mode
        #     formatter = logging.Formatter('%(asctime)s - %(message)s')
        #     handler.setFormatter(formatter)
        #     logger.addHandler(handler)

        # logger.info(str(data))
        try:   
            with open(filename,mode) as file:
                file.write(data)
        except Exception as e:
        #      with open(filename,'wb') as file:
        #         file.write(data)
            print(e)
            pass
        
    def finaloutput(self):
        self.usermessage()
        self.write_hex_data(data=self.messages,file="Encription_Data.log",mode='wb')
        # self.write_hex_data(self.realinfo,"Decrypt_Data.log",'w')
        # print(self.)
def seedcalculator(key):
    x = key & 0xFFFFFFFF
    x ^= (x << 13) & 0xFFFFFFFF
    x ^= (x >> 17)
    x ^= (x << 5) & 0xFFFFFFFF
    return x
if(__name__=="__main__"):
    # z="ABCD hello hahah A shgfusiogsfuogsufig ogy wgisfsh f gusugrs"
    text=' '
    key=42
    np.random.seed(seedcalculator(key))
    Encriptions(text,key)