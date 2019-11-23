import numpy as np
from PIL import Image


# NOTA: é adicionado 256 ao final da lista pois, do contrário, o último elemento seria deixado de fora da contagem.
# Dessa forma, o último elemento real é corretamente contabilizado, e '256' é descartado ao final do loop while da linha 24
def compress_rl(im):
    # im_name = im.get('name')
    # im = im.get('im_obj')

    im_name = 'benchmark.bmp'
    dim = im.shape
    if len(dim) == 2: flag = 0
    elif len(dim) == 3: flag = 1
    rl_list = []
    max_count = 1


    pixel_list = np.copy(im)
    pixel_list = pixel_list.flatten()
    pixel_list = pixel_list.tolist()

    # pixel_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 2, 4, 6, 2, 4, 6, 2, 4, 6, 2, 8, 1, 5, 8, 1, 5]

    if flag:
        aux = [(pixel_list[i], pixel_list[i+1], pixel_list[i+2]) for i in range(0, len(pixel_list), 3)]
        pixel_list = aux + [(256, 256, 256)]
    else: pixel_list += 256

    pixel_list = pixel_list[::-1]

    current = pixel_list.pop()
    counter = 1
    while pixel_list:
        next = pixel_list.pop()
        if current == next:
            counter += 1
            current = next
        else:
            rl_list.append(counter)
            rl_list.append(current)
            current = next
            if counter > max_count : max_count = counter
            counter = 1
    header = (flag, dim[0], dim[1])

    write_file(header, rl_list, im_name)
    print('Compressão realizada com sucesso.')


def decompress_rl(filename):
    file_path = 'images/compression/' + filename[:-4] + '_rl.bin'
    header, rl_list = read_file(file_path)
    flag, h, w = header

    print(rl_list[:50])
    im_list = []
    if flag:
        for i in range(0, len(rl_list), 4):
            counter = rl_list[i]
            color = [rl_list[i+1], rl_list[i+2], rl_list[i+3]]
            im_list += counter * color
    else:
        for i in range(0, len(rl_list), 2):
            counter = rl_list[i]
            color = rl_list[i+1]
            im_list += counter * [color]

    im_list = np.asarray(im_list)
    if flag: im_array = np.reshape(im_list, (h, w, 3)).astype(np.uint8)
    else: im_array = np.reshape(im_list, (h, w)).astype(np.uint8)

    im = Image.fromarray(im_array)
    im.save('images/compression/' + filename[:-4] + '_rl.bmp')


def write_file(header, list, im_name):
    file_path = 'images/compression/' + im_name[:-4] + '_rl.bin'
    flag = header[0]
    b_flag = header[0].to_bytes(1, 'little')
    h = header[1].to_bytes(2, 'little')
    w = header[2].to_bytes(2, 'little')

    with open(file_path, 'wb') as file:
        file.write(b_flag)
        file.write(h)
        file.write(w)

        for i in range(0, len(list), 2):
            counter = list[i]
            color = list[i+1]

            while counter > 255:
                counter = counter - 255
                file.write(int(255).to_bytes(1, 'little'))
                if flag:
                    for channel in color:
                        file.write(channel.to_bytes(1, 'little'))
                else:
                    file.write(color.to_bytes(1, 'little'))

            file.write(counter.to_bytes(1, 'little'))
            if flag:
                for channel in color:
                    file.write(channel.to_bytes(1, 'little'))
            else:
                file.write(color.to_bytes(1, 'little'))


def read_file(im_path):
    with open(im_path, 'rb') as file:
        flag = file.read(1)
        h = file.read(2)
        w = file.read(2)
        im_list = file.read()

    flag = int.from_bytes(flag, 'little')
    h = int.from_bytes(h, 'little')
    w = int.from_bytes(w, 'little')
    header = (flag, h, w)

    rl_list = [int(i) for i in im_list]

    return (header, rl_list)