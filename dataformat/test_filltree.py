import unittest

from jet_tree import *

class TestFillTree(unittest.TestCase):
     
    def test_particledata_1(self):
        NamedDataBlock.varlist = ['pt', 'E']
        d = NamedDataBlock('ptcs', ['pt', 'E'], nptcsmax= 5)
        d.fill_particle(pt=0.2, E=0.5)
        with self.assertRaises(TypeError) as err:
            d.fill_particle(0.2)
        with self.assertRaises(KeyError) as err:
            d.fill_particle(toto=0.5)
            
    def fill_ptcs(self):
        ptcs = [(i, i + 1) for i in range(4)]
        d = NamedDataBlock('ptcs', ['pt', 'E'], nptcsmax= 5)
        for i in ptcs:
            d.fill_particle(pt=i[0],
                            E=i[1])
        d.clear()
        
    def test_branch(self):
        class FakeTree(object):
            def Branch(self, name, data, representation):
                self.representation = representation
        tree = FakeTree()
        d = NamedDataBlock('ptcs', ['pt', 'E'], nptcsmax= 5)
        branch(tree, d)
        self.assertEqual(tree.representation, 'ptcs[5][2]')

        
if __name__ == '__main__':
    unittest.main()
