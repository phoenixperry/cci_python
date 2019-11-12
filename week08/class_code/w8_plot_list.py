import matplotlib.pyplot as plt

def ViteksPlotter(list_to_plot):
    plt.plot(list_to_plot)
    plt.title('Plotted values:')
    plt.xlabel('Paragraphs')
    plt.ylabel('Occurrences')
    plt.show()
	
# demo_list = [1, 0, 2, 0, 0, 0, 4, 1, 0, 0, 0]