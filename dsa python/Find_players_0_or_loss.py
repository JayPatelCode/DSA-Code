matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
loss_count={}
player=set()
for a,b in matches:
    player.add(a)
    player.add(b)
    loss_count[b]=loss_count.get(b,0)+1
print(loss_count)
print(player)
one_loss=[]
zero_loss=[]
for p in player:
    if loss_count.get(p,0)==0:
        zero_loss.append(p)
    elif loss_count[p]==1:
        one_loss.append(p)
print(sorted(one_loss))
print(sorted(zero_loss))