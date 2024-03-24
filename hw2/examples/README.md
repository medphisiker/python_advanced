# Description

Examples of python scripts using the `latex-gen-small` module([link](https://pypi.org/project/latex-gen-small/)).

## Install module

You can install this module by command:
```
poetry add latex-gen-small==0.1.4
```

Also you can use:
* `pyproject.toml`
* `poetry.lock`

from `hw2/examples` of `https://github.com/medphisiker/python_advanced_2024`.

You can copy this files to you project's repository and than run command:
```
cd to\your\project\folder
poetry install
```

Than you activate poetry virtual environment by command:
```
poetry shell
```

We are in our poetry virtual env now.

## Create a latex file with a table

We use `hw2/examples/table_gen.py` to create LaTex code to create a table.

Then we can run it by command:
```
python table_gen.py
```

And we get `main_table.tex` with LaTex code to create a table.

### Create a pdf file from our latex file with table

We can use any LaTex what we love to create a pdf from Latex source.

Also I prepared a useful Docker image to run Docker container to create pdf files from LaTex source `*.tex` files.

You can get this file from `https://github.com/medphisiker/python_advanced_2024` by this relative path `hw2/examples/Dockerfile`.

To build Docker image run this command:
```
docker build -t pdflatex:0.0.1 .
```

Then we can run Docker container by this command:
```
docker run \
    --rm \
    -it \
    -v "${PWD}:/root/shared_folder"  \
    pdflatex:0.0.1 \
    pdflatex main_table.tex
```

And we get output files from it:
* main_table.aux
* main_table.log
* main_table.pdf - the pdf file with our LaTex table

## Create a latex file with a table and image
We want to create a LaTex file with a table and some picture.
We save our pictures ti a folder `./images`, for example `mesh.png`.

We use `hw2/examples/table_picture_gen.py` to create LaTex code to create a table.

Then we can run it by command:
```
python table_picture_gen.py
```

And we get `main_table.tex` with LaTex code to create a table.

### Create a pdf file from our latex file with table and image

Then we can run Docker container by this command:
```
docker run \
    --rm \
    -it \
    -v "${PWD}:/root/shared_folder"  \
    pdflatex:0.0.1 \
    pdflatex main_table_picture.tex
```

And we get output files from it:
* main_table_picture.tex.aux
* main_table_picture.tex.log
* main_table_picture.tex.pdf - the pdf file with our LaTex table and picture `mesh.png`.
