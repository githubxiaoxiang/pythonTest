import numpy as np
# https://seancheney.gitbook.io/python-for-data-analysis-2nd/di-04-zhang-numpy-ji-chu-shu-zu-he-shi-liang-ji-suan#ji-ben-de-suo-yin-he-qie-pian
# data = np.random.randn(2,3)
# print(data)
# print(data*10)
# print(data+data)
# print(data.shape)
# print(data.dtype)

# data1 = [6, 7.5, 8, 0, 1]
# arr1=np.array(data1);
# print(arr1)

# data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# arr2 = np.array(data2,complex)
# print(arr2)
# print(arr2.ndim)
# print(arr2.shape)

# list0 = np.zeros(10)
# print(list0)
# list1 = np.ones(10)
# print(list1)
# 认为np.empty会返回全0数组的想法是不安全的。很多情况下（如前所示），它返回的都是一些未初始化的垃圾值。
# [[6.23042070e-307 3.56043053e-307 1.60219306e-306]
#  [2.44763557e-307 1.69119330e-306 1.78022342e-306]]
# list2 = np.empty((2,3))
# print(list2)


# arange是Python内置函数range的数组版  NumPy关注的是数值计算，因此，如果没有特别指定，数据类型基本都是float64（浮点数）。

# print(np.arange(10))#[0 1 2 3 4 5 6 7 8 9]
# print(list(range(10)))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 基本的索引和切片
# 跟列表最重要的区别在于，数组切片是原始数组的视图。这意味着数据不会被复制，视图上的任何修改都会直接反映到源数组上。
# arr = np.arange(10)
# print(arr) #[0 1 2 3 4 5 6 7 8 9]
# print(arr[5]) #5
# print(arr[5:8]) #[5 6 7]
# arr[5:8] = 12 
# print(arr)#[ 0  1  2  3  4 12 12 12  8  9]
# arr_slice = arr[5:8]
# print(arr_slice) #[12 12 12]
# arr_slice[1] = 12345
# print(arr)#[  0   1   2   3   4  12 12345  12   8   9]
# # 切片[ : ]会给数组中的所有值赋值
# arr_slice[:] = 64
# print(arr)#[ 0  1  2  3  4 64 64 64  8  9]
# # 注意：如果你想要得到的是ndarray切片的一份副本而非视图，就需要明确地进行复制操作，例如arr[5:8].copy()。
# arr_slice = arr[5:8].copy()
# arr_slice[1] = 360
# print(arr)  #[ 0  1  2  3  4 64 64 64  8  9]

# 二维切片
# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # 先行后列
# # print(arr2d[:2,1:]) #[[2 3] [5 6]]
# # 选取第二行的前两列
# # print(arr2d[1,:2]) # [4 5]
# # 第三列的前两行
# print(arr2d[:2,2]) #[3 6]
# # “只有冒号”表示选取整个轴，因此你可以像下面这样只对高维轴进行切片
# print(arr2d[:,:1]) #[[1] [4] [7]]

# # 花式索引  用整数数组进行索引 
# # 选取第1,3行数据
# print(arr2d[[0,2]]) #[[1 2 3] [7 8 9]]

#数组转置和轴对换  https://blog.csdn.net/u012762410/article/details/78912667
# arr = np.arange(15).reshape(3,5)
# print(arr)
# print(arr.T)

# arr = np.arange(16).reshape((2, 2, 4))
# print(arr)
# print(arr.transpose(1,0,2))

# arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
# print("原数组\n",arr)
# # 先行到列相加  合并成一维数组
# print("先行到列累加  合并成一维数组\n",arr.cumsum());#[ 0  1  3  6 10 15 21 28 36]
# # [[ 0  1  2]
# #  [ 3  5  7]
# #  [ 9 12 15]]  列相加
# print("列累加\n",arr.cumsum(axis=0))
# # [[ 0  1  3]
# #  [ 3  7 12]
# #  [ 6 13 21]]  行相加
# print("行累加\n",arr.cumsum(axis=1))
# #  [[ 0  1  2]
# #  [ 0  4 10]
# #  [ 0 28 80]]  列累乘
# print("列累乘\n",arr.cumprod(axis=0))
# #  [[  0   0   0]
# #  [  3  12  60]
# #  [  6  42 336]] 行累乘
# print("行累乘\n",arr.cumprod(axis=1))

# https://www.cnblogs.com/pineapple-chicken/p/11994457.html
# arr = np.arange(10)
# np.save("some_arr",arr)
# load_arr=np.load("some_arr.npy")
# print(load_arr)

# arr_a = np.arange(5)
# arr_b = np.arange(10)
# np.savez("archi_arr.npz",a=arr_a,b=arr_b)
# archi = np.load("archi_arr.npz")
# print("archi----a",archi["a"])

# np.savez_compressed("arr_compress.npz",a=arr_a,b=arr_b)
# compress_arr = np.load("arr_compress.npz")
# print(compress_arr["b"])

# np.savetxt("arr.csv",arr,"%d",",")
# txt_arr=np.loadtxt("arr.csv",dtype=np.int,comments="#",delimiter=",")
# print(txt_arr)


# 矩阵点乘
# 第一个矩阵第一行的每个数字（2和1），各自乘以第二个矩阵第一列对应位置的数字（1和1），然后将乘积相加（ 2 x 1 + 1 x 1），得到结果矩阵左上角的那个值3。
# arr_a = np.array([[1,2,3],[4,5,6]])
# arr_b = np.array([[7,8],[9,10],[11,12]])
# print("arr_a\n",arr_a)
# print("arr_b\n",arr_b)
# dot_ab = arr_a.dot(arr_b)  #等价于dot_ab = np.dot(arr_a,arr_b)
# # dot_ab = np.dot(arr_a,arr_b)
# print("dot_ab\n",dot_ab)

# 一次模拟多个随机漫步
# nwalks = 5000
# nsteps = 1000
# draws = np.random.randint(0,2,size=nsteps)#draws = np.random.randint(0, 2, size=(nwalks, nsteps))
# print("draws\n",draws)
# steps = np.where(draws>0,1,-1)
# print("steps\n",steps)
# walk = steps.cumsum()  #walks = steps.cumsum(1)
# print("walk\n",walk)
# print("walk_---min\n",walk.min())
# print("walk----max\n",walk.max())
#复杂点的统计任务——首次穿越时间，即随机漫步过程中第一次到达某个特定值的时间。假设我们想要知道本次随机漫步需要多久才能距离初始0点至少10步远（任一方向均可）。np.abs(walk)>=10可以得到一个布尔型数组，它表示的是距离是否达到或超过10，而我们想要知道的是第一个10或－10的索引。可以用argmax来解决这个问题，它返回的是该布尔型数组第一个最大值的索引（True就是最大值
#这里使用argmax并不是很高效，因为它无论如何都会对数组进行完全扫描。在本例中，只要发现了一个True，那我们就知道它是个最大值了。
# print((np.abs(walk)>10).argmax())


