import pandas as pd  #  type: ignore

pd.set_option("display.notebook_repr_html", True)




# Carga del archivo desde un repo en GitHub
truck_events = pd.read_csv("../files/input/truck_event_text_partition.csv")

# Cabecera del archivo
truck_events.head()





# Obtención de un subconjunto de registros
# truck_events_subset = truck_events.head(10) 
truck_events_subset = truck_events[0:10]
truck_events_subset





# Obtención de un subconjunto de columnas
specific_columns = truck_events_subset[
    ["driverId", "eventTime", "eventType"]
]
specific_columns