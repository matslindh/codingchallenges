def convert_text_to_number(text):
    possible = {'femti': 50, 'førti': 40, 'tretti': 30, 'tjue': 20, 'nitten': 19, 'atten': 18, 'sytten': 17,
                'seksten': 16, 'femten': 15, 'fjorten': 14, 'tretten': 13, 'tolv': 12, 'elleve': 11, 'ti': 10,
                'ni': 9, 'åtte': 8, 'sju': 7, 'seks': 6, 'fem': 5, 'fire': 4, 'tre': 3, 'to': 2, 'en': 1, }
    s = 0

    while text:
        for textual, value in possible.items():
            if text.startswith(textual):
                s += value
                text = text[len(textual):]
                break

    return s


def test_convert_text_to_number():
    assert convert_text_to_number('entotrefirefem') == 15
    assert convert_text_to_number('sjufirenitrettentrettitretrettitre') == 99


if __name__ == '__main__':
    print(convert_text_to_number(open('input/01', encoding='utf-8').read().strip()))
