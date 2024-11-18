import numpy as np
from try1111 import *
from sagittal_brain import *

def test_code():
    input = [[1,1,1], [0, 0, 0], [0, 0, 0]]
    result = np.mean(input, axis=1) #求每一行的均值
    expect = np.array([1, 0, 0])
    assert np.all(result==expect)
    
def test_func(): #26
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    save_array2CSV(data_input)
    
    run_averages(file_input='brain_sample.csv', file_output='brain_average.csv')
    
    output = readCSV(filepath = 'brain_average.csv') # output = np.loadtxt('brain_average.csv', delimiter=',')
    
    expect = np.array([0.]*20)
    expect[-1] = 1.
    
    # Run the progam
    subprocess.run(["python", "sagittal_brain.py"])
    
    np.testing.assert_array_equal(output, expect)
