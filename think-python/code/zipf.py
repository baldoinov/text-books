# https://en.wikipedia.org/wiki/Zipfs_law


from analyze_book import readbook, most_frequent
import matplotlib.pyplot as plt

def rank(d: dict) -> list:
    """Gets a mapping from words to values and returns a list of tuples in the form
    (rank, frequency, word).
    """

    freq = most_frequent(d)
    l = []
    rank = 1

    for tuples in freq:
        l += [(rank, tuples[0], tuples[1])]
        rank += 1
    
    return l


def plot_rank(l: list, scale: str='log') -> None:
    """Plot frequency vs. rank.
    
    l: list of tuples in form (rank, frequency, word)
    scale: string 'linear' or 'log'
    """

    ranks, freqs, words = zip(*l)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(ranks, freqs, 'r-', linewidth=3)
    plt.show()


if __name__ == '__main__':
    book = readbook()
    ranking = rank(book)
    plot_rank(ranking)

