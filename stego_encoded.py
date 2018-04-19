

def extract_data(path):
    f_data = open(path, "rb")
    data = []
    for line in f_data.readlines():
        data += list(line)
    if data[-1] != 0:
        data.append(0)
    return data


def extract_byte(byte):
    byte1 = "" + bin(byte)[2:]
    while len(byte1) < 8:
        byte1 = '0' + byte1
    return byte1


def write_data(data, pic, code):
    ind = 0
    LAST_ZERO_BYTE = 254
    ans = []

    if (len(data) * 8 * code > len(pic)):
        print("Your data is too big.")
        raise Exception()

    for byte in data:
        byte1 = extract_byte(byte)
        for bit in byte1:
            x = pic[ind] & LAST_ZERO_BYTE if bit == '0' else pic[ind] | 1
            ans.append(x)
            ans += pic[ind + 1:ind + code]
            ind += code
    for elem in pic[ind:]:
        ans.append(elem)
    return ans


def extract_message(pic, code):
    res = list()
    res_byte = 1
    ind = 0
    while res_byte != 0:
        res_byte = 0
        for i in range(8):
            res_byte = res_byte*2 + (pic[ind] & 1)
            ind += code
        res.append(res_byte)
    return res
