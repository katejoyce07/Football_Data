# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:01:59 2024

@author: KateJoyce
"""

import pathlib
import os
import pandas as pd
import json



# Update the path to match your local file structure
path = os.path.join(r"~Desktop\Wyscout\Matches", "matches_England.json") 

# Open and load the JSON file
with open(path, 'r') as f:
    data = json.load(f)

# Save it in a dataframe
df_matches = pd.DataFrame(data)

# Display the structure of the data
df_matches.info()



# Update the path to match your local file structure
path = os.path.join(r"~\Desktop\Wyscout", "players.json")

# Open and load the JSON file
with open(path, 'r') as f:
    data = json.load(f)

# Save it in a DataFrame
df_players = pd.DataFrame(data)

# Display the structure of the data
df_players.info()



# Define the path to the events file (assuming there's only one events file for England)
file_name = 'events_England.json'  # Adjust this based on the actual filename
path = os.path.join(r"~\Desktop\Wyscout\Events", file_name)

# Check if the file exists
if os.path.exists(path):
    # Open and load the event data from the file
    with open(path, 'r') as f:
        data = json.load(f)
    
    # Convert the data to a DataFrame
    df_events = pd.DataFrame(data)
    
    # Display the structure of the event data (overview of columns, non-null counts, etc.)
    df_events.info()
else:
    print(f"File not found: {path}")
    
    
    
    
 #SIGN TEST
import pandas as pd
import numpy as np
import json
# plotting
import matplotlib.pyplot as plt
#opening data
import os
import pathlib
import warnings

pd.options.mode.chained_assignment = None
warnings.filterwarnings('ignore')   
