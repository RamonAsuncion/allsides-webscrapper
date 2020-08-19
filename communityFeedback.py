# js file https://www.allsides.com/sites/default/files/js/js_RkhuUtuGis_wrzoAtkhY74JegSNy1LhoCkjSMXavCTI.js

def communityVote(ratio):
    # the value of the ratio goes through this if statement and prints out the return string
    if ratio > 3:
        return "Absolutely agrees"

    elif 2 < ratio <= 3:
        return "Strongly agrees"

    elif 1.5 < ratio <= 2:
        return "Agrees"

    elif 1 < ratio <= 1.5:
        return "Somewhat agrees"

    elif 0.67 < ratio < 1:
        return "Somewhat disagrees"

    elif 0.5 < ratio <= 0.67:
        return "Disagrees"

    elif 0.33 < ratio <= 0.5:
        return "Strongly disagrees"

    elif ratio <= .33:
        return "Absolutely disagrees"

    elif ratio == 1:
        return "Neutral"

    else:
        return None
