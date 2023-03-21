import re
import sys

def is_zh (c):
    x = ord (c) # to unicode
    # Punct & Radicals
    if x >= 0x2e80 and x <= 0x33ff:
        return True

    # Fullwidth Latin Characters
    elif x >= 0xff00 and x <= 0xffef:
        return True

    # CJK Unified Ideographs &
    # CJK Unified Ideographs Extension A
    elif x >= 0x4e00 and x <= 0x9fbb:
        return True
    # CJK Compatibility Ideographs
    elif x >= 0xf900 and x <= 0xfad9:
        return True

    # CJK Unified Ideographs Extension B
    elif x >= 0x20000 and x <= 0x2a6d6:
        return True

    # CJK Compatibility Supplement
    elif x >= 0x2f800 and x <= 0x2fa1d:
        return True

    else:
        return False
def split_zh_en (zh_en_str):
    mark = {"en":1, "zh":2}
    zh_en_group = []
    zh_gather = ""
    en_gather = ""
    zh_status = False

    for c in zh_en_str:
        if not zh_status and is_zh (c):
            zh_status = True
            if en_gather != "":
                zh_en_group.append ([mark["en"],en_gather])
                en_gather = ""
        elif not is_zh (c) and zh_status:
            zh_status = False
            if zh_gather != "":
                zh_en_group.append ([mark["zh"], zh_gather])
        if zh_status:
            zh_gather += c
        else:
            en_gather += c                               
            zh_gather = ""

    if en_gather != "":
        zh_en_group.append ([mark["en"],en_gather])
    elif zh_gather != "":
        zh_en_group.append ([mark["zh"],zh_gather])

    return zh_en_group

if __name__ == "__main__":
    s = 'in addition 誰是你oh'
    x = split_zh_en(s)
    for i in x:
        print(i)
