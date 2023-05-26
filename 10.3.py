import numpy as np
import pandas as pd

e = {'Name': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Bor', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']}
t = pd.DataFrame(data=e, index=np.arange(1,11))
t['Symbol'] = pd.Series([np.nan, 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne'])
t.insert(2, 'Weight', [1.007842, 4.002602, 6.945872, 9.012183, 10.809518, 12.009876, 14.006485, 15.999769, 18.998403, 20.179766])
left_aligned_t = t.style.set_properties(**{'text-align': 'left'})
display(left_aligned_t)
