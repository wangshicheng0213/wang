import random
from fractions import Fraction
import string
import  string

questions = open('question.txt','w')
answers = open('answers.txt','w')

testnumber = int(input("请问要做几道题:"))
answers.write('2018103004'+"\n")
for i in range(1,testnumber+1):
    test = [str(random.randint(1, 10))]

    for b in range (random.randint(1,3)):
        list = [random.randint(1, 10), Fraction(random.randint(1, 10), random.randint(1, 10))]     #f = str(Fraction(random.randint(1,100),random.randint(1,100)))
        new = Fraction(random.choice(list))
        part = [str(random.choice(['+', '-', '*', '/'])), str(new)]  # p = ['+','-','*','/']
        test = test + part
    #插入括号
    m = int(random.randrange(0,len(test)-1,2))
    test.insert(m,'(')   #前括号
    test.insert(m+4+random.randrange(m,len(test),2),')')  #后括号
    str1 = ' '.join(test)  #数组转化成字符串
    result = eval(str1)    #计算结果
    result = Fraction(result)  #转成分数
    str2 = '问题'+str(i)+':'+str1+'='
    lastresult = round(result,2)
    print(str2, file=questions)
    #answer1 = '答案22222' + str(i) + ':' + str(lastresult)
    answer1 =  str(lastresult)

    answers.write(str1+'='+str(answer1)+"\n")
    #print(answer1, file=answers)
    print(str2)
    doanswer = input("请输入你的答案：")
    if str(doanswer) == str(lastresult):
        print("回答正确")
    else:
        print("回答错误")


