import random

def nested_sum(matrix: list) -> int:
    """Takes a list of lists and adds up all the elements from the nested lists.
    """
    accumulator = 0
    
    for list in matrix:
        for element in list:
            accumulator = accumulator + element
    
    return accumulator


def cumsum(list_of_numbers: list) -> list:
    
    new_list = []
    accumulator = 0

    for i in list_of_numbers:
        accumulator = accumulator + i
        new_list.append(accumulator)
    
    return new_list


def middle(old_list: list) -> list:
    """Takes the an list and returns a new list withou the elements
    in the borders.
    """
    new_list = old_list[1:-1]
    return new_list


def chop(same_list: list) -> None:
    """Modifies a list by removing its first and last elements."""
    
    del same_list[0]
    del same_list[-1]


def is_sorted(t: list) -> bool:
    """Takes a list and return True if the list is sorted, returns False otherwise."""

    # lenght = len(t)
    # for i in range(1, lenght):
        # if t[i - 1] > t[i]:
            # return False
    # return True

    return t == sorted(t)


def is_anagram(word1: str or list, word2: str or list) -> bool:
    """Takes two string and checks if they can be anagrams."""

    # Essa solução comentada só é válida quando word é str.
    # if len(word1) != len(word2):
        # return False
    # for i in word1.lower():
        # if i not in word2.lower():
            # return False
    # return True

    return sorted(word1) == sorted(word2)


def has_duplicates(t: list or str) -> bool:

    s = list(t)
    
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            return True
    
    return False


def main():
    
    print("\n---nested_sum()\n")

    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    print("\n---cumsum()\n")

    t = [1, 2, 3]
    print(cumsum(t))

    print("\n---middle() and chop()\n")

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print("\n---is_sorted()\n")

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print("\n---is_anagram()\n")

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print("\n---has_duplicates()\n")

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == '__main__':
    main()

main()