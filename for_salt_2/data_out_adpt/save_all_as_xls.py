'''
Produces the final excel spreadsheet for all of this.

Done by quintile and decile.

Created on 8 Jan 2015

@author: chris
'''
def main():
    
    base_dir = '/home/chris/Projects/Cookit/family-food-datasets/2014/'
    
    '''By income quintile'''
    '''Weight purchased'''
    suff = 'ConsINCHH-11dec14.xls'
    fname = base_dir + suff
    
    from pickle_dat import get_spec_data  
    dat_wei, units_wei, _ = get_spec_data(fname)
    
    '''Price'''
    suff = 'ExpINC-11dec14.xls'
    fname = base_dir + suff
    
    dat_pri, units_pri, _ = get_spec_data(fname)
    
    from totals_stuff import get_totals
    dat_pri_tot, units_pri_tot, _ = get_totals(fname)
    
    import xlwt
    
    workbook = xlwt.Workbook()
    from save_as_xls import gen_wb
    gen_wb(workbook, dat_wei, units_wei, dat_pri, units_pri, dat_pri_tot, units_pri_tot)
    workbook.save('/tmp/quintile.xls')
    
    
    '''By income decile'''
    '''Weight purchased'''
    suff = 'ConsINCEQUIVHH-11dec14.xls'
    fname = base_dir + suff
    
#     from pickle_dat import get_spec_data  
    dat_wei, units_wei, _ = get_spec_data(fname)
    
#     import xlwt
    '''Price'''
    suff = 'ExpINC_EQUIV-11dec14.xls'
    fname = base_dir + suff
    
    dat_pri, units_pri, _ = get_spec_data(fname)
        
#     from totals_stuff import get_totals
    dat_pri_tot, units_pri_tot, _ = get_totals(fname)
    
    workbook = xlwt.Workbook()
#     from save_as_xls import gen_wb
    gen_wb(workbook, dat_wei, units_wei, dat_pri, units_pri, dat_pri_tot, units_pri_tot)
    workbook.save('/tmp/decile.xls')
    
    
    
    
if __name__ == '__main__':
    main()