import io, os.path, glob, tempfile, re, textwrap
import pickle, json, requests, urllib
import numpy as np
import pandas as pd

link="https://pogoda.wp.pl/"
pogoda_html = requests.get(link)
text=pogoda_html.text
miasto=re.compile("\u002Fpogoda-na-dzis\u002F(\\w+)\u002F")
temperatura=re.compile("data-temp=\"(-*\d+)")
z=miasto.findall(text)
z

k=temperatura.findall(text)


z=z[1:] # <- done to reduce duplicate 'gdansk' ( it's a must do the way code was written in the orginal website

final_z=list(dict.fromkeys(z)) # <- getting rid of the duplicates in a controled way
final_z.insert(3,'gorzow-wielkopolskie') # due to pearl langauge it was easier to add this manually

#index_z=final_z.index('bass')
#z_new=final_z[:index_z]
#print(z_new)
#print(len(k))
d={'miasto':final_z,'temperatura':k[0:len(final_z)]}
df=pd.DataFrame(data=d)
print(df)