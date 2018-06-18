import numpy as np


class NamedDataBlock(object):
        
    def __init__(self, name, varlist, nptcsmax):
        '''Creates a numpy array with nptcsmax lines and len(varlist) columns.
        varlist is the list of variables to be stored, e.g. : ['pt','E','type']
        '''
        self.name = name
        self.varlist = varlist
        self.data = np.zeros((nptcsmax, len(self.varlist)))
        self.column_indices = dict( (varname, i) for i, varname in enumerate(self.varlist))
        self.i_curptc = 0
        
    def fill_particle(self, **kwargs):
        '''fill the data for a particle.
        kwargs are the keyword arguments, corresponding to the varlist:
        e.g. fill_particle(pt=1, E=2, type=3)
        '''
        for name, value in kwargs.iteritems():
            j = self.column_indices[name]
            self.data[self.i_curptc, j] = value
        self.i_curptc += 1
            
    def clear(self):
        '''Call this at every event to clear the data structure'''
        self.i_curptc = 0
        self.data.fill(0.)
        
        
def branch(tree, pdata):
    '''Create a new branch in tree for the NamedDataBlock pdata'''
    representation = '{}[{}][{}]'.format(pdata.name,
                                         pdata.data.shape[0], pdata.data.shape[1])
    tree.Branch(pdata.name, pdata.data, representation)
    
