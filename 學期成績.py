score1=float(input("score1"))
score2=float(input("score2"))
score3=float(input("score3"))
list=[score1,score2,score3]
list.sort()
score=float(list[2]*0.5+list[1]*0.3+list[0]*0.2)
print("你的學期成績")
print(score)