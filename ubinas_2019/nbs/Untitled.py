# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# %load_ext autoreload
# %autoreload 2

# %%
from useful_scit.imps import *

# %%
sys.path.append('../../../ubinas-2019/')

# %%

from ubinas_2019.util import *
import ubinas_2019.util

# %%
ds = get_joined_ds()

# %%
fig,ax = plt.subplots()
ax.scatter(C_SO2,C_SO4,alpha=.05,data=ds)

# %%
ax.set_xlim(.01,100)
ax.set_ylim(.01,100)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel(C_SO2)
ax.set_ylabel(C_SO4)

ax.figure

# %%
ds4 = import_acsm_data()

# %%
ax = ds[[C_SO4,C_SO2]].plot(figsize = (20,10))
ax.grid(True,'both')
ax.figure.autofmt_xdate()

# %%

# %%
