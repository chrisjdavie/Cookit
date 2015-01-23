'''
Testing that 'pickle_dat' is saving the data properly.
Comparing by eye to the spreadsheet.

Created on 9 Jan 2015

@author: chris
'''
def main():
    
    import pickle
    with open('/tmp/total_test.p','rb') as f:
        dat_pri, units_pri, _ = pickle.load(f)
    
    print dat_pri
    
if __name__ == '__main__':
    main()