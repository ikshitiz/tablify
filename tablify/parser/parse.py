from tablify.core.html import HTML

class pyobj():
    
    def dictToHTMLTable(dict : dict):
        html = HTML(Header = dict.keys(),
                    tableStyles={'margin': '3px'},
                    trStyles={'background-color': '#7cc3a97d'},
                    thStyles={ 'color': 'white'})
        for i, row in enumerate(zip(*dict.values())):
            if i%2 == 0:
                BGC = 'aliceblue'
            else:
                BGC = '#c2d4e4'
            html.addRow(row, trStyles={'background-color' : BGC},\
                tdStyles={'padding': '1rem'})
        return html

