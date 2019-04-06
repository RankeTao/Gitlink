row = [1,2,3,4,5,6,7,8,9,0]
b = row.pop(0)
row.append(b)
print(row)
#去除语句中多余的空格
sentence  = "nice  to  meet  you"
lst_stn = sentence.split(" ")
print(lst_stn)
word = [s for s in lst_stn if s!=""] # 如果写成if s!=" " 则不会去除空格
print(word)
new_stn = " ".join(word)
print(new_stn)

# Fibonacci数列
a, b = 0, 1
Lst_fib = []
for i in range(15):
    a, b = b, a+b
    Lst_fib.append(a)
print(Lst_fib)
