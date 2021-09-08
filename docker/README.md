# attakei/pypicloud-trials

Docker image to run pypicloud.

## Usage

### Case 1: Local server

Make env 

```sh
$ docker pull attakei/pypicloud-trials
$ mkdir local
$ docker run --rm -it -v `pwd`/local:/app attakei/pypicloud-trials ppc-make-config -t server.ini
(enter your env on prompt)
$ docker run --rm -p 6543:6543 -v `pwd`/local:/app attakei/pypicloud-trials pserve server.ini
```

Try it

```sh
$ pip install --index http://localhost:6543/simple/ bottle
```

If you see message `Installing collected packages: bottle`, there is packages directory and bottle's wheel in your env. 