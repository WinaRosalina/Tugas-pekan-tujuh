import pandas as pd

pizza={
    'nama' : ['wina', 'krist', 'kristo'],
    'tinggi badan' : [155, 175, 176],
    'berat badan' : [40, 58, 61],
}

pizza_df= pd.DataFrame(pizza)
pizza_df
print(pizza_df)