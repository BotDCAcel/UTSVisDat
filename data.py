# data.py

import pandas as pd
import numpy as np

profit_data = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 
              'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Profit_Juta': [2.5, 4.0, 6.0, 7.5, 10.0, 9.5, 12.0, 15.0, 18.0, 17.5, 20.0, 23.0]
}
df_profit = pd.DataFrame(profit_data)

product_data = {
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 
              'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    'Samsung': [0, 0, 0, 1, 1, 2, 3, 3, 2, 3, 0, 1],
    'Nokia': [1, 1, 2, 1, 0, 0, 0, 0, 1, 1, 3, 4],
    'Xiaomi': [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 5, 2]
}
df_product = pd.DataFrame(product_data)
df_product['Total'] = df_product[['Samsung', 'Nokia', 'Xiaomi']].sum(axis=1)

proporsi_produk = pd.Series([16, 14, 12], index=['Samsung', 'Nokia', 'Xiaomi'])

heatmap_data = {
    'Januari': [100.0, 0.0, 0.0],
    'Februari': [0.0, 100.0, 0.0],
    'Maret': [33.3, 33.3, 33.3],
    'April': [0.0, 50.0, 50.0],
    'Mei': [50.0, 0.0, 50.0],
    'Juni': [100.0, 0.0, 0.0],
    'Juli': [100.0, 0.0, 0.0],
    'Agustus': [25.0, 50.0, 25.0],
    'September': [50.0, 25.0, 25.0],
    'Oktober': [50.0, 50.0, 0.0],
    'November': [37.5, 37.5, 25.0],
    'Desember': [28.6, 28.6, 42.8]
}
index_heatmap = ['Older kids', 'Teens', 'Adults']
df_heatmap = pd.DataFrame(heatmap_data, index=index_heatmap)
