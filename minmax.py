import math
scores=[3, 5, 2, 9, 12, 5, 23, 23]
treedepth=math.log(len(scores),2)

def minimax(currentdepth,nodeindex,maxturn,scores,targetdepth):
    if currentdepth==targetdepth:
        return scores[nodeindex]
    if maxturn:
        return max(minimax(currentdepth+1,nodeindex*2,False,scores,targetdepth) ,
                   minimax(currentdepth+1,nodeindex*2+1,False,scores,targetdepth))
    else:
        return min(minimax(currentdepth+1,nodeindex*2,True,scores,targetdepth) ,
                   minimax(currentdepth+1,nodeindex*2+1,True,scores,targetdepth))
print("The Optimal values is:" )
print(minimax(0,0,True,scores,treedepth))