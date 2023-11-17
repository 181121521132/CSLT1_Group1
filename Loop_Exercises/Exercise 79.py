from random import randrange
so = 100
GiaTriLonNhat = randrange(1, so + 1)
print(GiaTriLonNhat)
CapNhat = 0
for i in range(1, so):
  a = randrange(1, so + 1)
  if a > GiaTriLonNhat:
    GiaTriLonNhat = a
    CapNhat += 1
    print(a, '<== Update')
  else:
    print(a)
print('Gia tri lon nhat tim duoc la:', GiaTriLonNhat)
print('Gia tri toi da duoc cap nhat la:', CapNhat, 'lan')