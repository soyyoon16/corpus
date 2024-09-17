import argparse
from collections import Counter
from matplotlib import pyplot as plt


def get_ranks_and_frequencies(infile):
    """Produces a list of rank, frequency pairs for each word in a text file
    :param infile: a text file
    :return: a list containing rank, frequency pairs for each word
    """
    with open(infile) as f:
        contents = f.read()
    c = Counter(contents.split())
    ranks_and_frequencies = [(rank + 1, frequency[1]) for rank, frequency in
                             enumerate(c.most_common())]
    return ranks_and_frequencies


def plot(infile):
    """
    Plots rank and frequency pairs to demonstrate Zipf's Law
    :param infile: a text file
    :return: None, produces a matplotlib plot
    """
    ranks_and_frequencies = get_ranks_and_frequencies(infile)
    rs, fs = zip(*ranks_and_frequencies)

    plt.clf()
    plt.title("Zip's Law")
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=2)
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Constructs a curve '
                                                 'demonstrating Zipf\'s Law '
                                                 'by plotting a rank, '
                                                 'frequency plot.')
    parser.add_argument('--path', type=str, required=True, help='Path to file')
    args = parser.parse_args()
    plot(args.path)
