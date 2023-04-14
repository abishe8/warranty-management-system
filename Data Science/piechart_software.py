#import necessary modules
import matplotlib.pyplot as plt


def main():
    # Make an example pie plot
    fig = plt.figure()
    ax = fig.add_subplot(111)

    categories = ['Anti-virus and Security', 'Small-to-Medium Scale Business Software', 'Office Software',"Creator's Software"]
    data = [10, 12, 13, 5] #maps from database
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
