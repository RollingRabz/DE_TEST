def accum(s: str):
    if not s.isalpha():  # Check if the input contains only alphabetic characters
        raise ValueError("Input must only contain letters from a-z and A-Z")
    multi = 0    #Multiply that word by ... 
    ans = ''     # empty string for store output
    for i in s: 
        if multi == 0:
            ans += i.upper()  # If it first letter then no multiply
        else:
            ans += '-' + i.upper() + i.lower() * multi  # The second letter onward will be add '-' before it uppercase letter and repeat the leter.
        multi += 1
    return ans


# Run this file for test
assert accum("ZpglnRxqenU") == "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
assert accum("NyffsGeyylB") == "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
assert accum("MjtkuBovqrU") == "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
assert accum("EvidjUnokmM") == "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
assert accum("HbideVbxncC") == "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"