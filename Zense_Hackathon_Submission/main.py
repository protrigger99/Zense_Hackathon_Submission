import discord
import os
import random
from words import words
from keep_alive import keep_alive

def getword(words):
  word = random.choice(words)
  while '-' in word or ' ' in word:
        word = random.choice(words)
  return word.lower()

client =discord.Client()
pl=0
@client.event
async def on_ready():
  print("We have been logged in as {client}")
  

word=getword(words)
l = list(word)
new ='?'*len(word)
star=len(word)
l2 = list(new)
l3=[]
@client.event
async def on_message(message):
  global new
  global p
  global wrong
  global count
  global star
  global l3
  global z
  global y
  global pl
  global b
  global a
  global l
  global l2
  global word
  
  if message.author == client.user :
    return
  if( message.content == '2'):
     will()
  if message.content == "$start" and pl==1:
    send_msg = 'Please wait, '+ b +' is playing now'
    await message.channel.send(send_msg)
  if message.content==("$start") and pl==0:
      await message.channel.send(new) 
      p=1
      wrong = 0
      count=0
      z=1
      pl=1
      a=message.author
      b=message.author.name
  if(star>0): 
    x = message.content 
    if(len(x)==1):

      if(x not in l3) and message.author==a:
        l3.append(x)
      elif message.author==a:
        await message.channel.send("You have guessed this letter already")
        await message.channel.send(l2)
        return
      if any(k in x  for k in l  ) and p==1 and (l3.count(x)==1) and x!="$start" and message.author==a:
    
        
        for i in range(len(l2)):
          if(l2[i]=='?' and l[i]==message.content):
            l2[i]=message.content
            count=1 
            star=star-1
      elif(message.author==a):
          count=0
      if(count==0) and x!="$start" and message.author==a:
        wrong+=1
        count=0
      
      if(wrong == 1) and message.author==a:
        await message.channel.send(file=discord.File('1.png'))  
      if(wrong==2) and message.author==a:
        await message.channel.send(file=discord.File('2.png'))  
        
      if(wrong==3) and message.author==a:
        await message.channel.send(file=discord.File('3.png'))  
        
      if(wrong==4) and message.author==a:
        await message.channel.send(file=discord.File('4.png'))  
    
      if(wrong==5) and message.author==a:
        await message.channel.send(file=discord.File('5.png'))  
        
      if(wrong==6) and message.author==a:
        await message.channel.send(file=discord.File('6.png'))  
        
      if(wrong==7) and message.author==a:
        await message.channel.send(file=discord.File('7.png'))  
        await message.channel.send("You Lost")
        await message.channel.send("The word is:")
        await message.channel.send(word)
        pl=0
        l3=[]
        word=getword(words)
        l = list(word)
        new ='?'*len(word)
        star=len(word)
        l2 = list(new)
        
       
      if(wrong!=7) and message.author==a:
        await message.channel.send(l2) 
    if(len(x)!=1) and x!="$start" and message.author==a:
      await message.channel.send("Enter only 1 letter")
  if(star==0):
      await message.channel.send("You Win")
      pl=0
      l3=[]
      word=getword(words)
      l = list(word)
      new ='?'*len(word)
      star=len(word)
      l2 = list(new)
keep_alive()  
client.run(os.getenv('TOKEN'))

