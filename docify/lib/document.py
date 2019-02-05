from copy import deepcopy

from docify.lib import components as c


class Document(object):
    '''The core document object.
    It can be passed as input to different formatters which can parse
    it into various formats.

    :param list components: Components to be added in the document.
    
    Example usage: ::

        doc = Document(P('Hail Docify!'))
        print(HTML(doc))
        print(Markdown(doc))
        print(Whatever(doc))
    '''

    def __init__(self, *components, cite=True):
        self.components = []
        self.depth = 0
        self.cite = cite
        for c in components:
            self.add(c)

    def __repr__(self):
        return '{}(\n{}{})'.format(
            self.__class__.__name__, ' ' * (self.depth + 1) * 4,
            ('\n' + (' ' * (self.depth + 1) * 4)).join(map(str, self.components)))

    def add(self, component):
        '''Adds a component in the doc.

        :param Component component: Component to be added
        '''
        if isinstance(component, str):
            component = c.Span(component)
        component.setparent(self)

        if len(self.components) > 0:
            self.components[-1].setnext(component)

        self.components.append(component)
