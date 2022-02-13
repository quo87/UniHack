import pandas as pd
#test.generate_data(0,1000)
#print(test.data)
def list_to_series(research):
    word_count = pd.Series(research)
    return word_count
#print(word_count)
#print(word_count.mean(),word_count.std())