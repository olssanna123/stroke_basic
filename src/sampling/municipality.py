from utils.random_generator import model

# Draw a sample from sampling_array between 0 and highest_number
def draw_sample(sampling_array):
    index = model(len(sampling_array))
#    print("Idx:", index)
    sample = sampling_array[index]
    return sample