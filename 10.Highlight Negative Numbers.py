import pandas as pd
import numpy as np
np.random.seed(0)
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
def highlight_negative(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'
styled_df = df.style.applymap(highlight_negative)
styled_df
