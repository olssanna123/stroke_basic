import pandas as pd
from data.municipalities import get_population_municipalities

def initiate_sampling_array():
    data = get_population_municipalities()
    df = pd.DataFrame(data)
    sampling_array_list_of_lists = []
    sampling_array = []
    i = 0
    while i < 49:
        name_region = df.loc[i].at["Kommun"]
        nb_citizens = df.loc[i].at["Folkmangd"]
        item = [name_region]*nb_citizens
        sampling_array_list_of_lists.append(item)
        i += 1
    # Make it a single list
    j = 0
    k = 0
    while j < 49:
        k = 0
        while k < len(sampling_array_list_of_lists[j]):
            tmp = sampling_array_list_of_lists[j][k]
            sampling_array.append(tmp)
            k += 1
        j += 1
    return sampling_array