import numpy as np


def main():
    print("Question 1:")  # A
    arr = np.arange(0, 10, 1)
    print(arr)

    print("\nQuestion 2:")  # D
    arr_a = np.ones((3, 3)) > 0
    arr_b = np.ones((3, 3), dtype=bool)
    arr_c = np.full((3, 3), fill_value=True, dtype=bool)
    print(arr_a)
    print(arr_b)
    print(arr_c)

    print("\nQuestion 3:")  # A
    arr = np.arange(0, 10)
    print(arr[arr % 2 == 1])

    print("\nQuestion 4:")  # B
    arr = np.arange(0, 10)
    arr[arr % 2 == 1] = -1
    print(arr)

    print("\nQuestion 5:")  # B
    arr = np.arange(10)
    arr_2d = arr.reshape(2, -1)
    print(arr_2d)

    print("\nQuestion 6:")  # A
    arr1 = np.arange(10).reshape(2, -1)
    arr2 = np.repeat(1, 10).reshape(2, -1)
    c = np.concatenate([arr1, arr2], axis=0)
    print("Result:\n", c)

    print("\nQuestion 7:")  # C
    arr1 = np.arange(10).reshape(2, -1)
    arr2 = np.repeat(1, 10).reshape(2, -1)
    c = np.concatenate([arr1, arr2], axis=1)
    print("C = ", c)

    print("\nQuestion 8:")  # A
    arr = np.array([1, 2, 3])
    print(np.repeat(arr, 3))  # repeat từng thành phần
    print(np.tile(arr, 3))  # repeat mảng

    print("\nQuestion 9:")  # C
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    index = np.where((a >= 5) & (a <= 10))
    print("Result", a[index])

    print("\nQuestion 10:")  # D

    def maxx(x, y):
        return x if x >= y else y

    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])
    pair_max = np.vectorize(maxx, otypes=[float])
    print(pair_max(a, b))

    print("\nQuestion 11:")  # A
    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])
    print("Result", np.where(a < b, b, a))

    # Image Processing
    import matplotlib.image as mpimg

    print("\nQuestion 12:")  # A
    #!gdown 1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB
    import matplotlib.image as mpimg
    img = mpimg.imread('dog.jpeg')
    gray_img_01 = (np.max(img, axis=2) + np.min(img, axis=2)) / 2
    print(gray_img_01[0, 0])

    print("\nQuestion 13:")  # A
    gray_img_02 = np.mean(img, axis=2)
    print(gray_img_02[0, 0])

    print("\nQuestion 14:")  # C
    gray_img_03 = 0.21 * img[:, :, 0] + 0.72 * \
        img[:, :, 1] + 0.07 * img[:, :, 2]
    print(gray_img_03[0, 0])

    # Data Analysis
    import pandas as pd

    print("\nQuestion 15:")  # C
    #!gdown 1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq
    df = pd.read_csv('advertising.csv')
    data = df.to_numpy()
    max_value = np.max(data[:, 3])
    max_index = np.argmax(data[:, 3])
    print(f"Max: {max_value} - Index: {max_index}")

    print("\nQuestion 16:")  # B
    mean_tv = np.mean(data[:, 0])
    print(mean_tv)

    print("\nQuestion 17:")  # A
    sales_ge_20 = np.sum(data[:, 3] >= 20)
    print(sales_ge_20)

    print("\nQuestion 18:")  # B
    mean_radio = np.mean(data[data[:, 3] >= 15, 1])
    print(mean_radio)

    print("\nQuestion 19:")  # C
    mean_newspaper = np.mean(data[:, 2])
    total_sales = np.sum(data[data[:, 2] > mean_newspaper, 3])
    print(total_sales)

    print("\nQuestion 20:")  # C
    a = np.mean(df[:, 3])
    scores = np.empty(len(df), dtype='<U7')
    scores[df[:, 3] > a] = 'Good'
    scores[df[:, 3] < a] = 'Bad'
    scores[df[:, 3] == a] = 'Average'
    print(scores[7:10])

    print("\nQuestion 21:")  # C
    closest_value = data[np.abs(data[:, 3] - mean_sales).argmin(), 3]
    scores = np.where(data[:, 3] > closest_value, 'Good', np.where(
        data[:, 3] < closest_value, 'Bad', 'Average'))
    print(scores[7:10])

if __name__ == "__main__":
    main()
