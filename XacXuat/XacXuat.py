import numpy as np

#random.randint
a = np.random.randint(0, 2) # Ngẫu nhiên số nguyên trong khoảng [0, 2)
print("a = ",a)
coins = np.random.randint(2, size=1000)
print(coins.shape)

#Tính % số lần tung được mặt ngửa và úp, ta sẽ thấy nó đều xấp xỉ 50%:
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)

# random.choice
coins = np.random.choice([0, 1], size=1000, p=[0.2, 0.8])
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)

#random.binomial
b = np.random.binomial(20, 0.5) # Số mặt ngửa nhận được khi tung đồng xu 20 lần trong 10 lần lặp
print("b = ", b)

array = np.random.binomial(20, 0.5, 10)
print(array)

print("Trung bình số mặt ngửa nhận được khi tung đồng xu 20 lần trong vòng 10 lần lặp: ", np.random.binomial(20, 0.5, 10).mean())

n = 10  # tung 10 đồng xu trong 1 lần
p = 0.2  # bias cho mặt ngửa (xác suất cho mặt ngửa là 0.2)
l = 1000  # số lần lặp

b = np.random.binomial(n, p, l)
print("Trung bình số mặt ngửa nhận được: ", b.mean())
