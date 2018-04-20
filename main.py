import sten_func as sf
import os
import numpy
import matplotlib.pyplot as plt
import compression as cmpr

#Хи-квадрат для каждого элемента разбиения sinica.png и enc_sinica.png
def test_1():
    path = os.path.join(os.getcwd(), 'images')
    sf.chi_square_all(path, 'sinica.png', 0)
    path = os.path.join(os.getcwd(), 'images\encoded')
    sf.chi_square_all(path, 'enc_sinica.png', 0)
    return

#Шифрование в sinica.png - 30%
def test_2():
    path = os.path.join(os.getcwd(), 'images')
    sf.encode(path, 'sinica.png', 'data.txt')

#Фильтр для enc_sinica.png
def test_3():
    path = os.path.join(os.getcwd(), 'images\encoded')
    sf.pictures_lsb_colored(path, 'enc_sinica.png', 0, 0)

#Декодирование из enc_sinica.png
def test_5():
    path = os.path.join(os.getcwd(), 'images\\encoded')
    sf.decode(path, 'enc_sinica.png', 'result.txt')

#Матожидание размера черного блока в углу 100x100 в sinica.png и enc_sinica.png
def test_4():
    left = 0
    right = 100
    height = 100
    width = 100
    path = os.path.join(os.getcwd(), 'images')
    matrix_1 = sf.picture_to_lsb_matrix_colored(path, 'sinica.png', 0, 0)
    matrix_2 = sf.picture_to_lsb_matrix_colored(path + '\\encoded', 'enc_sinica.png', 0, 0)
    freq_1 = sf.black_area_frequencies(matrix_1[0:width, 0:height], left, right)
    freq_2 = sf.black_area_frequencies(matrix_2[0:width, 0:height], left, right)
    try:
        print('E_wout_st = {}'.format(sum([i*freq_1[i] for i in range(len(freq_1))]) / sum(freq_1) / width*height))
    except:
        print("There aren't black blocks with size between {} and {}, so E_wout_st = 0".format(left, right))
    try:
        print('E_w_st = {}'.format(sum([i*freq_2[i] for i in range(len(freq_2))]) / sum(freq_2) / width*height))
    except:
        print("There aren't black blocks with size between {} and {}, so E_w_st = 0".format(left, right))
    fig = plt.figure()
    plt.title('Рапределение черных полей')
    plt.plot(range(left, right), freq_1, label = 'Without_stego')
    plt.plot(range(left, right), freq_2, label = 'With_stego')
    plt.legend()
    plt.savefig(os.path.join(path + '\\plots', 'sinica.png'))
    return

#Шифрование в mothers_kiss.png - 5%
def test_5():
    path = os.path.join(os.getcwd(), 'images')
    sf.encode(path, 'mothers_kiss.png', 'shir.cpp')
    return 

#Фильтр
def test_6():
    path = os.path.join(os.getcwd(), 'images\\encoded')
    sf.pictures_lsb_colored(path, 'enc_mothers_kiss.png', 0, 0)


#Хи-квадрат для стеганографии enc_mothers_kiss.png
def test_7():
    path = os.path.join(os.getcwd(), 'images\\encoded')
    sf.chi_square_all(path, 'enc_mothers_kiss.png', 0)
    return

#Мат. ожидание относительной площади черного блока в углу 100х100 в mothers_kiss.png и enc_mothers_kiss.png
def test_8():
    left = 0
    right = 100
    height = 100
    width = 100
    path = os.path.join(os.getcwd(), 'images')
    matrix_1 = sf.picture_to_lsb_matrix_colored(path, 'mothers_kiss.png', 0, 0)
    matrix_2 = sf.picture_to_lsb_matrix_colored(path + '\\encoded', 'enc_mothers_kiss.png', 0, 0)
    freq_1 = sf.black_area_frequencies(matrix_1[0:width, 0:height], left, right)
    freq_2 = sf.black_area_frequencies(matrix_2[0:width, 0:height], left, right)
    try:
        print('E_wout_st = {}'.format((sum([i*freq_1[i] for i in range(len(freq_1))]) / sum(freq_1)) / (width*height)))
    except:
        print("There aren't black blocks with size between {} and {}, so E_wout_st = 0".format(left, right))
    try:
        print('E_w_st = {}'.format((sum([i*freq_2[i] for i in range(len(freq_2))]) / sum(freq_2)) / (width*height)))
    except:
        print("There aren't black blocks with size between {} and {}, so E_w_st = 0".format(left, right))
    fig = plt.figure()
    plt.title('Рапределение черных полей')
    plt.plot(range(left, right), freq_1, label = 'Without_stego')
    plt.plot(range(left, right), freq_2, label = 'With_stego')
    plt.legend()
    plt.savefig(os.path.join(path + '\\plots', 'mothers_kiss.png'))
    return


def main():
    test_8()
    return 0

if __name__ == '__main__':
    main()
