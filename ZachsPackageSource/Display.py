import matplotlib.pyplot as plt
import numpy as np

def Display(data, lineType, label='', done = False, xLabel=None, yLabel=None, plotLabel=None, f=None, log=False, save=False, show=True):
    """ Displays data as [x, y]"""
    t = np.arange(0, 4, 0.01)
    
    plt.plot(data[0], data[1], lineType, label=label)
    if (done):
        if f != None:
            plt.plot(t, f(t, 1), 'k', label='Exact')
        if log:
            plt.xscale("log")
            plt.yscale("log")
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend(loc='best')
        # plt.tight_layout()
        if save:
            plt.savefig('{0}.pdf'.format(plotLabel))
        if show:
            plt.show()

def ProduceLatexTable(columnHeadings, data, title='', label=''):
    """ Prints latex table"""
    # Adds a catption and begins table
    caption = '{' + title + '}'
    print('\\begin{table}')
    print('   \centering')
    print('   \caption{0}'.format(caption))

    # Sets the columns in \begin{tabular} (cccc...)
    cols = ''
    for i in range(len(data[0])):
        cols += 'c'
    print('   \\begin{tabular}{@{}', cols, '@{}}\\toprule')

    # Sets the column headings
    line = ''
    for i in range(len(columnHeadings)-1):
        line += columnHeadings[i] + ' & '
    line += columnHeadings[-1]
    print('      ', line, '\\\\ \midrule')

    # Prints the rows with the data provided
    for i in range(len(data)):
        row = ''
        for j in range(len(columnHeadings)-1):
            row += str(data[i][j]) + ' & '
            # row += '{0:6.4G}'.format(data[i][j]) + ' & '
        row += str(data[i][-1])
        # row += '{0:5.4G}'.format(data[i][-1])
        print('      ', row, '\\\\')

    # Ends the table schema
    print('      \\bottomrule')
    print('   \end{tabular}')
    label = '{' + label + '}'
    print('   \label{0}'.format(label))
    print('\end{table}')

def HowIFeel():
    with plt.xkcd():
        ax = plt.subplot(111)

        t = np.arange(0.0, 10, 0.01)
        s = -t**3+1000
        line, = plt.plot(t, s, lw=2)
        plt.plot(9, 271, 'ko')

        plt.annotate('Me', xy=(9, 271), xytext=(3, 700),
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    )
        plt.xlabel('Time')
        plt.ylabel('Motivation')
        plt.tight_layout()
        plt.show()

HowIFeel()