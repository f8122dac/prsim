schemes = [{
        "edges":"#F25F5C",
        "bg":"#50514F",
        "isol_node":"#0E1407",
        "isol_text": "#F1F9EA",
        "text":"#0D0D0D",
    },
    {
        "edges":"#FF1654",
        "bg":"#B2DBBF",
        "isol_node":"#0E1407",
        "isol_text": "#F1F9EA",
        "text":"#0D0D0D"
    },
    {
        "edges":"#0E103D",
        "bg":"#D3BCC0",
        "isol_node":"#0E1407",
        "isol_text": "#F1F9EA",
        "text":"#0D0D0D"
    },
    {
        "edges":"#BF5A50",
        "bg":"#D9B972",
        "isol_node":"#0E1407",
        "isol_text": "#F1F9EA",
        "text":"#A68776"
    },
    {
        "edges":"#661620",
        "bg":"#EBDDC2",
        "isol_node":"#0E1407",
        "isol_text": "#F1F9EA",
        "text":"#E0B51F"
    }
]

rgb_formatter = lambda rgb: "#{:02X}{:02X}{:02X}".format(*rgb)
# 380nm to 780nm
def nm2rgb(w):
    w = int(w)

    # color calculation gate
    if w >= 380 and w < 440:
        R = -(w - 440.) / (440. - 350.)
        G = 0.0
        B = 1.0
    elif w >= 440 and w < 490:
        R = 0.0
        G = (w - 440.) / (490. - 440.)
        B = 1.0
    elif w >= 490 and w < 510:
        R = 0.0
        G = 1.0
        B = -(w - 510.) / (510. - 490.)
    elif w >= 510 and w < 580:
        R = (w - 510.) / (580. - 510.)
        G = 1.0
        B = 0.0
    elif w >= 580 and w < 645:
        R = 1.0
        G = -(w - 645.) / (645. - 580.)
        B = 0.0
    elif w >= 645 and w <= 780:
        R = 1.0
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0

    # intensity correction
    if w >= 380 and w < 420:
        SSS = 0.3 + 0.7*(w - 350) / (420 - 350)
    elif w >= 420 and w <= 700:
        SSS = 1.0
    elif w > 700 and w <= 780:
        SSS = 0.3 + 0.7*(780 - w) / (780 - 700)
    else:
        SSS = 0.0
    SSS *= 255

    return rgb_formatter([int(SSS*R), int(SSS*G), int(SSS*B)])

#S,E = 380, 780
#S,E = 580, 680 # spectrum 1
#S,E = 660, 560 # spectrum 2
#S,E = 570, 690 # spectrum 3
S,E = 490, 632 # spectrum 4
spectrum = lambda n: [nm2rgb(wl+(E-S)/n) for wl in range(S, E, (E-S)//n)]
