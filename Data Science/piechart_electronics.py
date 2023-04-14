#import modules
import matplotlib.pyplot as plt


def main():
    # Make an example pie plot
    fig = plt.figure()
    ax = fig.add_subplot(111)

    categories = ['Mobiles and Accessories', 'Computer and Accessories', 'Grooming and Wellness (Medical) devices','Other Electronic Devices']
    data = [10, 12, 13, 5] #map data from database
    wedges, plt_labels = ax.pie(data, labels=categories)
    ax.axis('equal')

    make_picker(fig, wedges)
    plt.show()


def make_picker(fig, wedges):
    import webbrowser

    def on_pick(event):
        wedge = event.artist
        label = wedge.get_label()
        webbrowser.open('http://images.google.com/images?q={0}'.format(label))

    # Make wedges selectable
    for wedge in wedges:
        wedge.set_picker(True)

    fig.canvas.mpl_connect('pick_event', on_pick)


if __name__ == '__main__':
    main()
Foo
