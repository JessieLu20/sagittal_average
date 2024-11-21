import numpy as np
from try1111 import *
from sagittal_average.sagittal_brain import *
# import subprocess

def test_code():
    input = [[1,1,1], [0, 0, 0], [0, 0, 0]]
    result = np.mean(input, axis=1) #求每一行的均值
    expect = np.array([1, 0, 0])
    assert np.all(result==expect)
    
def test_func(): #26
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    print("data_input", data_input)
    save_array2CSV(data_input)

    run_averages(file_input='./tests/fixtures/brain_sample.csv', file_output='./tests/fixtures/brain_average.csv')
    # output = readCSV(filepath = 'brain_average.csv') # 
    output = np.loadtxt('./tests/fixtures/brain_average.csv',delimiter=',')
    print('output', output)
    expect = np.array([0.]*20)
    expect[-1] = 1.
    assert np.allclose(output, expect)
    # Run the progam
    # subprocess.run(["python", "sagittal_brain.py"])
    
    #np.testing.assert_array_equal(output, expect)
