import click


@click.command()
@click.argument("file_path", default="")
def nl_func(file_path):
    """Simple function that works like `nl -b a` Linux utility

    Parameters
    ----------
    file_path : str
        The path to the text file to process.
    """
    if file_path:
        with open(file_path, "r") as file:
            for i, line in enumerate(file):
                line = line.strip()
                print(f"{i + 1:>6}  {line}")
    else:
        i = 0
        while True:
            line = input().strip()
            print(f"{i + 1:>6}  {line}")
            i += 1


if __name__ == "__main__":
    nl_func()
