from matplotlib import pyplot as plt

def show(df):
    plt.figure(figsize=(10, 10))
    columns = ['Close','SMA1','SMA2']
    for column, data in df.iteritems():
        if column in columns:
            print(column, data.dtype)
            plt.plot(df[column], label=column)

    plt.legend()
    plt.show(block=True)