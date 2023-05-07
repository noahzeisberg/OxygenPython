import colorama
colorama.init(convert=True)
color = colorama.Fore.GREEN

def get_percentage(n: float, v: float):
    return n/v*100


def bars(percentage: int):
    bar_string = ""
    for i in range(round(percentage/2)):
        bar_string += color + "|"
    for i in range(50-round(percentage/2)):
