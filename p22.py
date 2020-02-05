# p22.py

score = input().split()
score = [int(i) for i in score]

if score[0] <= 60 or (score[1] < 60 and score[2] < 60):
    print('False')
else:
    print('True')
