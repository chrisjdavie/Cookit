'''
Opens the pickled test 5-a-day data, and saves it as
a spreadsheet.  

Is more for developing and debugging, these fuctions 
are mostly called elsewhere.  

Created on 14 Nov 2014

@author: chris
'''

import xlwt

def main():
    import pickle
    
    workbook = xlwt.Workbook()
    
    with open('/tmp/test.p','rb') as f:
        dat, units, book_name = pickle.load(f)
        
    gen_sheet(workbook, dat, units, book_name)
    workbook.save('/tmp/tst.xls')
        
def gen_sheet(workbook, dat, units, book_name):
    bold_style = xlwt.easyxf('font: bold 1')
    
    sheet = workbook.add_sheet(book_name)

    yr_keys = dat[dat.keys()[0]]['Fresh fruit'].keys()
    ordr = [ k[2:4] for k in yr_keys ]
    
    import numpy as np
    
    i_sort  = np.argsort(ordr)
    yr_keys = np.array(yr_keys)[i_sort]
    
    for i, yr_k in enumerate(yr_keys):
        sheet.write(1, 4+i, yr_k, bold_style)
    i_yr = i + 5
        
    sheet.write(1, 3, 'Units', bold_style)  
        
    j_0 = -2
    for age in dat.keys():
        j_0 += 3
        sheet.write(1+j_0, 1, age, bold_style)
    
        for j, fud_type in enumerate(dat[age].keys()):
#             print j, j+j_0
            sheet.write(2+j+j_0, 2, fud_type, bold_style)
            sheet.write(2+j+j_0, 3, units[fud_type], bold_style)
                        
            for i, yr_k in enumerate(yr_keys):
                sheet.write(2+j+j_0, 4+i, dat[age][fud_type][yr_k])
        
        j_0 = j+j_0

        
    for i, yr_k in enumerate(yr_keys):
        sheet.write(1, 4+i+i_yr, yr_k, bold_style)
        
    sheet.write(1, 3+i_yr, 'Units', bold_style)       
        
    j_0 = -2
    for age in dat.keys():
        j_0 += 3
        sheet.write(1+j_0, 1+i_yr, age, bold_style)
    
        for j, fud_type in enumerate(dat[age].keys()):
#             print j, 2+j+j_0, 2+i_yr
            sheet.write(2+j+j_0, 2+i_yr, fud_type, bold_style)
            sheet.write(2+j+j_0, 3+i_yr, 'portions', bold_style)
            if units[fud_type] == 'g':
                div = 80
            elif units[fud_type] == 'ml':
                div = 150
            
                        
            for i, yr_k in enumerate(yr_keys):
#                 print j, 2+j+j_0, 4+i_yr
                q = dat[age][fud_type][yr_k]
                q = q/div/7.0
                sheet.write(2+j+j_0, 4+i+i_yr, xlwt.Formula(xlwt.Utils.rowcol_to_cell(2+j+j_0, 4+i)+'/'+str(div)+'/7'))
        
        j_0 = j+j_0    
        
if __name__ == '__main__':
    main()