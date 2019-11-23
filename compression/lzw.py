import numpy as np
from PIL import Image

def dec2bin(num, n_bits):
    result = bin(num)[2:]
    result = result.zfill(n_bits)
    return result


def bin2dec(num):
    saida = 0

    num[::-1]
    for i in range(len(num)):
        print(saida)
        if num[i]:
            saida += (2 ** i)
    print(saida)
    return saida


def encode_list(list):
    dic = {}
    result = []
    nextCode = 256
    list.reverse()

    current = list.pop()
    while list:
        next = list.pop()
        pair = (current, next)
        if pair in dic:
            current = dic[pair]
        else:
            result.append(current)
            dic[pair] = nextCode
            nextCode += 1
            current = next
    # codificando última entrada da lista
    result.append(current)

    n_bits = (nextCode - 1).bit_length()
    print('lzw aplicado.')
    return (n_bits, result)


# def decode_list(list):
#     dic = {i: [i] for i in range(256)}
#     result = []
#     nextCode = 256
#     list.reverse()
#
#     current = list.pop()
#     while list:
#         next = list.pop()
#         # pair = [current, next]
#         # if pair not in dic: # !!!
#         #     dic[nextCode] = pair
#         #     nextCode += 1
#
#         entry = dic.get(current)
#         if isinstance(entry, int):
#             result.append(entry)
#             current = next
#         else:
#             reading_list = []
#             entry = entry.reverse()
#             while len(entry) > 0:
#                 a = dic.get(entry.pop())
#                 if isinstance(a, int):
#                     reading_list.append(a)
#                 else:
#                     for item in a.reverse():
#                         entry.append(item)
#             for item in reading_list:
#                 result.append(item)
#             current = next
#
#     # codificando última entrada:
#     entry = dic.get(current)
#     if isinstance(entry, int):
#         result.append(entry)
#     else:
#         reading_list = []
#         entry = entry.reverse()
#         while len(entry) > 0:
#             a = dic.get(entry.pop())
#             if isinstance(a, int):
#                 reading_list.append(a)
#             else:
#                 for item in a.reverse():
#                     entry.append(item)
#         for item in reading_list:
#             result.append(item)
#
#     return result


def write_file(header, list, im_name):
    file_path = 'images/compression/' + im_name[:-4] + '_lzw.bin'
    n_bits = header[1]

    # binarizando list em uma stringzord
    bin_string = ''
    for i in list:
        bin_string += dec2bin(i, n_bits)
    image_bytes = [bin_string[i:i + 8] for i in range(0, len(bin_string), 8)]

    flag = header[0].to_bytes(1, 'little')
    h = header[2].to_bytes(2, 'little')
    w = header[3].to_bytes(2, 'little')
    n_bits = n_bits.to_bytes(1, 'little')

    with open(file_path, 'wb') as file:
        file.write(flag)
        file.write(n_bits)
        file.write(h)
        file.write(w)

        for s in image_bytes:
            aux = int(s, 2).to_bytes(1, 'little')
            file.write(aux)

def read_file(im_path):
    with open(im_path, 'rb') as file:
        flag = file.read(1)
        n_bits = file.read(1)
        h = file.read(2)
        w = file.read(2)
        im_list = file.read()

    flag = int.from_bytes(flag, 'little')
    n_bits = int.from_bytes(n_bits, 'little')
    h = int.from_bytes(h, 'little')
    w = int.from_bytes(w, 'little')
    header = (flag, n_bits, h, w)

    aux_list = [int(i) for i in im_list]
    bin_str = ''

    # transformando bytes da imagem em uma lista de bits
    for i in range(len(aux_list)-1):
        bin_str += bin(aux_list[i])[2:].zfill(8)
    aux = aux_list[len(aux_list)-1]   # pega ultimo elemento da lista
    bin_str += bin(aux)[2:]

    return (header, bin_str)


def compress_lzw(im):
    # im_name = im.get('name')
    # im = im.get('im_obj')
    im_name = 'benchmark.bmp'
    im_name = 'teste.bmp'
    dim = im.shape

    pixel_list = np.copy(im)
    pixel_list = pixel_list.flatten()
    pixel_list = pixel_list.tolist()
    pixel_list = [116, 104, 105, 115, 105, 115, 116, 104, 101]

    if len(dim) == 2: flag = 0
    elif len(dim) == 3: flag = 1

    aux = encode_list(pixel_list)
    print('encoded test: {}'.format(aux))
    n_bits = aux[0]
    lzw_im = aux[1]
    header = (flag, n_bits, dim[0], dim[1])

    write_file(header, lzw_im, im_name)
    print('Compressão realizada com sucesso.')


def decompress_lzw(filename):
    file_path = 'images/compression/' + filename[:-4] + '_lzw.bin'

    header, bin_str = read_file(file_path)

    flag, n_bits, h, w = header
    print(flag, n_bits, h, w)

    coded_im = [int(bin_str[i:i + n_bits], 2) for i in range(0, len(bin_str), n_bits)]      # reorganizando lista de bits
    print(coded_im)
    # decoded_im = decode_list(coded_im)
    # print(decoded_im)
    decoded_im = [116, 104, 105, 115, 105, 115, 116, 104, 101, 115, 101, 115]
    decoded_im = np.asarray(decoded_im)
    im_array = np.reshape(decoded_im, (2, 2, 3))

    if flag: im_array = np.reshape(decoded_im, (h, w, 3)).astype(np.uint8)
    else: im_array = np.reshape(decoded_im, (h, w)).astype(np.uint8)

    im = Image.fromarray(im_array)
    im.save('images/compression' + filename[:-4] + '_lzw.bmp')



