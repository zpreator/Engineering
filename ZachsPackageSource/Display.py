import matplotlib.pyplot as plt

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