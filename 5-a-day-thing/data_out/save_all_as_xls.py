'''
Extracts the 5-a-day data from the different excel spreadsheets, and 
saves it all in one big spreadsheet. 

Created on 14 Nov 2014

@author: chris
'''
def main():
    base_dir = '/home/chris/Projects/Cookit/family-food-datasets/'
    
    import xlwt
    workbook = xlwt.Workbook()    
    
    from pickle_this import get_fruit_n_veg_data
    
    files = [ 'ConsAGEHRPHH-12dec13.xls', 'ConsGORHH-12dec13.xls', 'ConsINCHH-12dec13.xls',  'ConsAGEHRPEDHH-12dec13.xls', 'ConsCOMPHH-12dec13.xls', 'ConsINCEQUIVHH-12dec13.xls' ] 
    book_names = ['age (old)',                    'region',               'income quintile', 'age (young)',               'household composition', 'income decile'   ]
    
    '''By old age'''
    for suff, book_name in zip(files,book_names):
        fname = base_dir + suff
          
        dat, units, _ = get_fruit_n_veg_data(fname)
        
        from save_as_xls import gen_sheet
        
        gen_sheet(workbook, dat, units, book_name)
        
    workbook.save('/tmp/tst.xls')    

if __name__ == '__main__':
    main()