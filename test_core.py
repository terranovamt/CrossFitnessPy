from srcs import core

def test_datapipeline():
    filenames = ['C:/Users/terranom/OneDrive - STMicroelectronics/Desktop/prj/TRASK/CrossFitnessPy/repo/Matteo.txt']
    assert core.datapipeline(filenames)

def test_main():
    assert core.main() == 0
