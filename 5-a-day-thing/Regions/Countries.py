'''
Testing functionality of function designed generating spreadsheet
for quintiles on another data set. 

Created on 13 Nov 2014

@author: chris
'''
def main():
    fname = '/home/chris/Projects/Cookit/family-food-datasets/ConsGORHH-12dec13.xls'
    
    from quintiles import get_fruit_n_veg_data, plottity
    
    regions_dat = get_fruit_n_veg_data(fname)

    Countries = [ 'England', 'Wales', 'Scotland', 'Northern Ireland' ]
    
    plottity(regions_dat, Countries, Countries, 'Countries in the UK', 'country', 1)
    
    England_areas = [ 'North East', 'North West', 'Yorkshire and The Humber', 'South West', 'South East', 'East Midlands', 'West Midlands', 'London' ]
    England_labels = [ 'North\n East', 'North\n West', 'Yorkshire', 'South\n West', 'South\n East', 'East\n Midlands', 'West\n Midlands', 'London' ]
    
    plottity(regions_dat, England_areas, England_labels, 'Regions in England', 'region', 2)
    
    import matplotlib.pyplot as pl
    
    pl.show()

if __name__ == '__main__':
    main()