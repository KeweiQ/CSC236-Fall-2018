from typing import List


def shade_sort(colour_list: List[str]) -> None:
    """ Put colour_list in order "b" < "g" < "r".

    precondition: colour_list is a List[str] from {"b", "g", "r"}

    >>> list_ = ["r", "b", "g"]
    >>> shade_sort(list_)
    >>> list_ == ["b", "g", "r"]
    True

    postcondition: colour_list has same strings as before,
    ordered "b" < "g" < "r"
    """
    # loop invariants:
    #
    # 0 <= blue <= green <= red <= len(colour_list)
    # colour_list[0 : green] + colour_list[red :] same colours as before
    # and all([c == "b" for c in colour_list[0 : blue]])
    # and all([c == "g" for c in colour_list[blue : green]])
    # and all([c == "r" for c in colour_list[red :]])
    if colour_list == []:
        pass
    else:
        blue = 0
        green = 0
        red = len(colour_list)
        while green != red:
            if colour_list[green] == "g":
                green += 1
            elif colour_list[green] == "b":
                colour_list[green], colour_list[blue] = \
                    colour_list[blue], colour_list[green]
                blue += 1
                green += 1
            else:
                if colour_list[red - 1] == "r":
                    red -= 1
                elif colour_list[red - 1] == "g":
                    colour_list[green], colour_list[red - 1] = \
                        colour_list[red - 1], colour_list[green]
                    red -= 1
                    green += 1
                else:
                    colour_list[green], colour_list[red - 1] = \
                        colour_list[red - 1], colour_list[green]
                    colour_list[green], colour_list[blue] = \
                        colour_list[blue], colour_list[green]
                    red -= 1
                    green += 1
                    blue += 1


def four_shade_sort(colour_list: List[str]) -> None:
    """ Put colour_list in order "b" < "g" < "r" < "y".

    precondition: colour_list is a List[str] from {"b", "g", "r", "y"}

    >>> list_ = ["r", "y", "b", "g"]
    >>> four_shade_sort(list_)
    >>> list_ == ["b", "g", "r", "y"]
    True

    postcondition: colour_list has same strings as before,
    ordered "b" < "g" < "r" < "y"
    """
    # loop invariants:
    #
    # 0 <= blue <= green <= red <= yellow <= len(colour_list)
    # colour_list[0 : red] + colour_list[yellow :] same colours as before
    # and all([c == "b" for c in colour_list[0 : blue]])
    # and all([c == "g" for c in colour_list[blue : green]])
    # and all([c == "r" for c in colour_list[green : red]])
    # and all([c == "r" for c in colour_list[yellow :]])
    if colour_list == []:
        pass
    else:
        blue = 0
        green = 0
        red = 0
        yellow = len(colour_list)
        while red != yellow:
            if colour_list[red] == "r":
                red += 1
            elif colour_list[red] == "g":
                colour_list[green], colour_list[red] = \
                    colour_list[red], colour_list[green]
                red += 1
                green += 1
            elif colour_list[red] == "b":
                colour_list[green], colour_list[red] = \
                    colour_list[red], colour_list[green]
                colour_list[green], colour_list[blue] = \
                    colour_list[blue], colour_list[green]
                red += 1
                blue += 1
                green += 1
            else:
                if colour_list[yellow - 1] == "y":
                    yellow -= 1
                elif colour_list[yellow - 1] == "r":
                    colour_list[yellow - 1], colour_list[red] = \
                        colour_list[red], colour_list[yellow - 1]
                    yellow -= 1
                    red += 1
                elif colour_list[yellow - 1] == "g":
                    colour_list[yellow - 1], colour_list[red] = \
                        colour_list[red], colour_list[yellow - 1]
                    colour_list[green], colour_list[red] = \
                        colour_list[red], colour_list[green]
                    yellow -= 1
                    red += 1
                    green += 1
                else:
                    colour_list[yellow - 1], colour_list[red] = \
                        colour_list[red], colour_list[yellow - 1]
                    colour_list[green], colour_list[red] = \
                        colour_list[red], colour_list[green]
                    colour_list[green], colour_list[blue] = \
                        colour_list[blue], colour_list[green]
                    yellow -= 1
                    red += 1
                    green += 1
                    blue += 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
