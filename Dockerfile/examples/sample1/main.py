import luigi
import os

class Rtask1(luigi.Task):
    def requires(self):
        pass

    def output(self):
        return luigi.LocalTarget('home/examples/sample1/output/hello_world1.csv')

    def run(self):
      os.system("/usr/bin/Rscript home/examples/sample1/tasks/r1.R")

class Rtask2(luigi.Task):
    def requires(self):
        return Rtask1()

    def output(self):
        return luigi.LocalTarget('home/examples/sample1/output/hello_world2.csv')

    def run(self):
      os.system("/usr/bin/Rscript home/examples/sample1/tasks/r2.R")

if __name__ == '__main__':
    luigi.run(['Rtask2', '--local-scheduler'])