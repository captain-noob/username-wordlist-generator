#!/usr/bin/python3.8

import time
import os
import subprocess

#Authon captain-noob
global user
def main():
    print("")
    print("")
    print("                    USERNAME GENERATOR")
    print("--------------------------------------------------------")
    print("Help :")
    print(f"     Add name of users to :{root}/user.txt ")
    print("             (Then Restart The Program)")
    print("                          v2.0")
    print("--------------------------------------------------------")
    if os.path.isfile(root+'/output.txt'):
        subprocess.run(["rm",root+"/output.txt"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,shell=False)
        open(root+'/output.txt','x')
    else:
        open(root+'/output.txt','x')
    time.sleep(.5)
    print("")
    print("[*] Names Loaded :")
    
    




        
def fileread():
    with open(userlist_path, "r") as user:
        for line in user:
            global word
            word = line.strip()
            username=word
            if username != "":
                print (f"        + {username}")
            
            if len(word.split(" ")) > 1:
                adds()
                fils()
                
            else:
                save(username)
            
            
            


def adds(): #4 word
    user=[]
    user.append(word.replace(' ',"-"))
    user.append(word.replace(' ',"_"))
    user.append(word.replace(' ',"."))
    user.append(word)
    # print(f"usr :{user}")
    for userslist in user:
        save(userslist)

def fils(): #12
    users=[]
    # print("*****************************")
    # print(f"word : {word}")
    splits=word.split(" ")
    # print(f"splited :{splits}")
    n=len(splits)
    # print(f"length of split :{n}")
        
    # print("*****************************")
    if n > 2:
        more3(splits)       
    else:
        fw=splits[0][0]
        sw=splits[1][0]
        users.append(splits[0]+splits[1])
        users.append(fw+splits[1])
        users.append(splits[0]+sw)
        users.append(fw+'-'+splits[1])
        users.append(fw+'_'+splits[1])
        users.append(fw+'.'+splits[1])
        users.append(splits[0]+'-'+sw)
        users.append(splits[0]+'_'+sw)
        users.append(splits[0]+'.'+sw)
        users.append(fw+sw)
        # print(users)
        for userslist in users:
            save(userslist)
        

def more3(splits): #39
    users=[]
    if len(splits)==3:
        fl=splits[0][0]
        sl=splits[1][0]
        tl=splits[2][0]
        users.append(splits[0]+splits[1]+splits[2])
        users.append(fl+splits[1]+splits[2])
        users.append(splits[0]+sl+splits[2])  
        users.append(splits[0]+splits[1]+tl)
        users.append(fl+'-'+splits[1]+'-'+splits[2])
        users.append(fl+'.'+splits[1]+'.'+splits[2])
        users.append(fl+'_'+splits[1]+'_'+splits[2])
        users.append(splits[0]+'-'+sl+'-'+splits[2])        
        users.append(splits[0]+'.'+sl+'.'+splits[2])        
        users.append(splits[0]+'_'+sl+'_'+splits[2])        
        users.append(splits[0]+'_'+splits[1]+'_'+tl)
        users.append(splits[0]+'.'+splits[1]+'.'+tl)
        users.append(splits[0]+'-'+splits[1]+'-'+tl)
        users.append(fl+sl+tl)
        # print(users)
        for userslist in users:
            save(userslist)
    else:
        fl=splits[0][0]
        sl=splits[1][0]
        tl=splits[2][0]
        ftl=splits[3][0]
        users.append(splits[0]+splits[1]+splits[2]+splits[3])
        users.append(fl+splits[1]+splits[2]+splits[3])
        users.append(splits[0]+sl+splits[2]+splits[3])  
        users.append(splits[0]+splits[1]+tl+splits[3])
        users.append(splits[0]+splits[1]+splits[2]+ftl)

        users.append(fl+'-'+splits[1]+'-'+splits[2]+'-'+splits[3])
        users.append(fl+'.'+splits[1]+'.'+splits[2]+'.'+splits[3])
        users.append(fl+'_'+splits[1]+'_'+splits[2]+'_'+splits[3])
        users.append(splits[0]+'-'+sl+'-'+splits[2]+'-'+splits[3])        
        users.append(splits[0]+'.'+sl+'.'+splits[2]+'.'+splits[3])        
        users.append(splits[0]+'_'+sl+'_'+splits[2]+'_'+splits[3])        
        users.append(splits[0]+'_'+splits[1]+'_'+tl+'_'+splits[3])
        users.append(splits[0]+'.'+splits[1]+'.'+tl+'.'+splits[3])
        users.append(splits[0]+'-'+splits[1]+'-'+tl+'-'+splits[3])

        users.append(splits[0]+'.'+splits[1]+'.'+splits[2]+'.'+ftl)
        users.append(splits[0]+'-'+splits[1]+'-'+splits[2]+'-'+ftl)
        users.append(splits[0]+'_'+splits[1]+'_'+splits[2]+'_'+ftl)

        users.append(fl+sl+tl+ftl)
        # print(users)
        for userslist in users:
            save(userslist)


#save to file
def save(ur):
    tofile=ur
    out=open(root+'/output.txt','r+')
    out.read()
    tofile=tofile+'\n'
    out.write(tofile) 


root=os.path.dirname(os.path.realpath(__file__))
userlist_path=root+"/user.txt"
main()
fileread()
print('')
print('[*] Started Converting.....')
time.sleep(.5)
print("[*] Successfully Created Usernames")
print("[*] Saving File....")

time.sleep(.5)
print(f"[*] File Saved to : {root}/output.txt")
print("[*] Happy Hacking ............. ")
