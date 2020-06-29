def minion_game(string):
    vowel="AEIOU"
    Kevin=0
    Stuart =0
    for i in range(0,len(s)):
        if(s[i] in vowel):
            Kevin = Kevin+len(s)-i
        else:
            Stuart= Stuart + len(s)-i  
    if(Kevin>Stuart):
      print("Kevin " + str(Kevin)) 
    elif(Stuart > Kevin):
      print("Stuart " + str(Stuart))
    else:
      print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
