'''
Finding total expenditure and pickling it - this is a different
case than before (using the unique identifier 'cat105' in interest
and using 'i_cats = [0]', not a combination of 1, 2 or 3.

The 'get_data' function required a little editting.

Created on 9 Jan 2015

@author: chris
'''
def main():
    base_dir = '/home/chris/Projects/Cookit/family-food-datasets/2014/'
    
    suff = 'ExpINC-11dec14.xls'
    fname = base_dir + suff
    
    dat_pri, units_pri, book_name_pri = get_totals(fname)
    
    import pickle
    with open('/tmp/total_test.p','w+') as f:
        pickle.dump([dat_pri, units_pri, book_name_pri], f)

def get_totals(fname):   
    interest = [ 'cat105' ]
    from pickle_dat import get_data
    return get_data(fname, interest, i_cats=[0])
    
    
if __name__ == '__main__':
    main()