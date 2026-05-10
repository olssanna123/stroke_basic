from utils.random_generator import model

# Draw a sample from array between 0 and highest_number
def draw_sample(array):
    index = model(len(array))
    sample = array[index]
    return sample