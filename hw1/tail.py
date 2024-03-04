import sys
import click


def read_last_n_lines(file_path, n):
    """Read n lines from text file and print them to terminal.

    Parameters
    ----------
    file_path : str
        The path to the file we want to process.
    n : int
        the number of lines from the file that we want to output to the terminal
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        last_n_lines = lines[-n:]

        for line in last_n_lines:
            print(line, end="")


def read_last_n_lines_from_stdin(n):
    """Read n lines from stdin and print them to terminal.

    Parameters
    ----------
    n : int
        the number of lines from the stdin that we want to output to the terminal
    """
    for i in range(n):
        print(sys.stdin.readline())


@click.command()
@click.option("--file_path", "-f", multiple=True)
def tail_func(file_path):
    """Simple function that works like `tail` Linux utility

    Parameters
    ----------
    file_path : str
        The path to the text file to process.
    """
    if file_path:
        if len(file_path) == 1:
            read_last_n_lines(file_path[0], n=10)
        else:
            for file in file_path:
                print(f"==> {file} <==")
                read_last_n_lines(file, n=10)
                print()
    else:
        read_last_n_lines_from_stdin(n=17)


if __name__ == "__main__":
    tail_func()
