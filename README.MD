
# luigir

luigir is docker image include luigi which python package pipelines of batch. 

We were adapting it could use the r script in luigi.


## Installation and execute sample

- clone.

```bash
git clone https://github.com/RottenFruits/luigir.git
```

- docker build and start.

```bash
cd luigir
docker build Dockerfile/. -t luigir
docker run --name lugir -it luigir /bin/bash
```

- execute sample
```bash
python3 /home/examples/sample1/main.py
```

## References

- [R in big data pipeline](http://opiateforthemass.es/articles/r-in-big-data-pipeline/)

