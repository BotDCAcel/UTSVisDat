import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from data import df_profit, df_product, proporsi_produk, df_heatmap
import numpy as np
import pandas as pd

HEADER_COLOR = '#8B4513'
BG_COLOR = '#111111'
CHART_BG_COLOR = '#2C2C2C'
LINE_COLOR = '#FFA500' 
TEXT_COLOR = 'white' 

plt.style.use('default') 
plt.rcParams['figure.facecolor'] = BG_COLOR
plt.rcParams['axes.facecolor'] = CHART_BG_COLOR
plt.rcParams['text.color'] = TEXT_COLOR
plt.rcParams['axes.labelcolor'] = TEXT_COLOR
plt.rcParams['xtick.color'] = TEXT_COLOR
plt.rcParams['ytick.color'] = TEXT_COLOR
plt.rcParams['grid.alpha'] = 0.4 
plt.rcParams['grid.linestyle'] = '-'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['legend.fontsize'] = 9

def draw_header(fig, rect_coords, title):
    ax_header = fig.add_axes(rect_coords)
    ax_header.set_facecolor(HEADER_COLOR)
    ax_header.set_xticks([])
    ax_header.set_yticks([])
    ax_header.spines[['top', 'bottom', 'left', 'right']].set_visible(False)
    ax_header.text(0.01, 0.5, title, color='white', fontsize=14, va='center', fontweight='bold')
    return ax_header

def create_dashboard_final_v7():
    fig = plt.figure(figsize=(16, 20)) 
    
    ax_main_header = fig.add_axes([0.05, 0.94, 0.90, 0.025])
    ax_main_header.set_facecolor(HEADER_COLOR)
    ax_main_header.set_xticks([])
    ax_main_header.set_yticks([])
    ax_main_header.spines[['top', 'bottom', 'left', 'right']].set_visible(False)
    ax_main_header.text(0.01, 0.5, 'Dashboard Profit Penjualan dan Top Produk', 
                        color='white', fontsize=20, va='center', fontweight='bold')
    
    draw_header(fig, [0.05, 0.88, 0.90, 0.02], 'Profit Penjualan (Juta)')
    ax1 = fig.add_axes([0.05, 0.70, 0.90, 0.17]) 
    
    ax1.plot(df_profit['Bulan'], df_profit['Profit_Juta'], color=LINE_COLOR, linewidth=2)
    ax1.set_ylabel('Profit Penjualan (Juta)', fontsize=12)
    ax1.set_xlabel('')
    ax1.spines[['top', 'right', 'left', 'bottom']].set_visible(False)
    ax1.set_ylim(0, 25)
    ax1.tick_params(axis='x', rotation=0, labelsize=10)
    ax1.tick_params(axis='y', labelsize=10)
    
    
    draw_header(fig, [0.05, 0.61, 0.90, 0.02], 'Top 3 Produk Terjual per Bulan')
    ax2 = fig.add_axes([0.05, 0.45, 0.90, 0.15]) 

    bottom_samsung = np.zeros(len(df_product))
    bottom_nokia = df_product['Samsung']
    colors_prod = ['#FBE5A1', '#FFD870', '#FFA500'] 
    
    ax2.bar(df_product['Bulan'], df_product['Samsung'], bottom=bottom_samsung, label='Samsung', color=colors_prod[0])
    ax2.bar(df_product['Bulan'], df_product['Nokia'], bottom=bottom_nokia, label='Nokia', color=colors_prod[1])
    ax2.bar(df_product['Bulan'], df_product['Xiaomi'], bottom=df_product['Samsung'] + df_product['Nokia'], label='Xiaomi', color=colors_prod[2])
    
    ax2.set_ylabel('Unit Terjual', fontsize=12)
    ax2.set_xlabel('')
    ax2.set_ylim(0, 9)
    ax2.grid(True, axis='y', linestyle=':', alpha=0.6)
    ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, frameon=False, fontsize=9)
    ax2.tick_params(axis='x', rotation=0, labelsize=10)
    ax2.spines[['top', 'right', 'left', 'bottom']].set_visible(False)
    

    draw_header(fig, [0.05, 0.35, 0.45, 0.02], 'Produk Terbanyak Terjual')
    ax3 = fig.add_axes([0.05, 0.05, 0.45, 0.28]) 
    
    colors_pie = ['#FBE5A1', '#FFD870', '#FFA500'] 
    wedgeprops = {'width': 0.5, 'edgecolor': CHART_BG_COLOR}
    
    wedges, texts = ax3.pie(proporsi_produk, startangle=90, wedgeprops=wedgeprops, colors=colors_pie)
    
    total_sales = proporsi_produk.sum()
    

    ax3.text(-1.1, 0.8, f'{proporsi_produk.index[0]}', fontsize=11, va='center', ha='right', color='white', fontweight='bold')
    ax3.text(-1.1, 0.6, f'{proporsi_produk.iloc[0]/total_sales*100:.1f}%', fontsize=11, va='center', ha='right', color=LINE_COLOR, fontweight='bold')
    
    ax3.text(-0.05, -1.3, f'{proporsi_produk.index[1]}', fontsize=11, va='center', ha='center', color='white', fontweight='bold')
    ax3.text(-0.05, -1.5, f'{proporsi_produk.iloc[1]/total_sales*100:.1f}%', fontsize=11, va='center', ha='center', color=LINE_COLOR, fontweight='bold')
    
    ax3.text(1.1, 0.8, f'{proporsi_produk.index[2]}', fontsize=11, va='center', ha='left', color='white', fontweight='bold')
    ax3.text(1.1, 0.6, f'{proporsi_produk.iloc[2]/total_sales*100:.1f}%', fontsize=11, va='center', ha='left', color=LINE_COLOR, fontweight='bold')

    ax3.axis('equal') 
    ax3.spines[['top', 'right', 'left', 'bottom']].set_visible(False)
    ax3.set_xticks([])
    ax3.set_yticks([])


    draw_header(fig, [0.52, 0.35, 0.43, 0.02], 'Heatmap Target Usia')
    ax4 = fig.add_axes([0.52, 0.05, 0.43, 0.28]) 

    sns.heatmap(df_heatmap, 
                annot=True, 
                fmt=".1f", 
                cmap="YlOrBr",
                cbar=False, 
                linewidths=2, 
                linecolor=CHART_BG_COLOR,
                yticklabels=df_heatmap.index,
                ax=ax4)
    
    for t in ax4.texts: 
        t.set_text(t.get_text() + " %")
        t.set_color('black')
        t.set_fontsize(7)
    
    ax4.tick_params(axis='x', rotation=0, labelsize=8)
    ax4.tick_params(axis='y', rotation=0, labelsize=9)
    ax4.set_xlabel('')
    
    plt.savefig('final_dashboard_rapi_v7.png', dpi=300, facecolor=BG_COLOR)

if __name__ == '__main__':
    create_dashboard_final_v7()
