import unittest
import random
import os
import time
import logging

from ParameterConfigSpace.config_space import ConfigSpace

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        random.seed(12345)
        self.src_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.clasp_pcs_file = os.path.join(self.src_dir, "ParameterConfigSpace", "unittest",
                                           "files", "clasp-sat-params-nat.pcs")
        self.lingeling_pcs_file = os.path.join(self.src_dir, "ParameterConfigSpace", "unittest",
                                               "files", "lingeling-params.pcs")

        #logging.basicConfig(level=logging.DEBUG)

    def test_clasp(self):
        
        print("clasp")

        cs = ConfigSpace(self.clasp_pcs_file)
        
        t0 = time.time()
        for _ in xrange(1,10000):
            vec = cs.get_random_config_vector()
            #print(cs.convert_param_vector(vec))
        print("clasp random configs time (sec): %f" %(time.time() - t0))

    def test_convert_clasp(self):
        
        print("clasp convert")
        cs = ConfigSpace(self.clasp_pcs_file)
        def_config = cs.get_default_config_dict()
        print(def_config)
        def_vec = cs.convert_param_dict(def_config)
        def_config_back = cs.convert_param_vector(def_vec)
        #print(def_config)
        #print(def_vec)
        
        for param, value in def_config.iteritems():
            assert value == def_config_back[param], "%s: %s vs %s" %(param, str(value), str(def_config_back[param]))
        
    def test_neighbor_clasp(self):
        print("clasp neighbor")

        cs = ConfigSpace(self.clasp_pcs_file)
        def_config = cs.get_default_config_dict()
        def_vec = cs.convert_param_dict(def_config)
        
        
        t0 = time.time()
        for _ in xrange(0,10000):
            neighbor_vec = cs.get_random_neighbor(def_vec)
        print("clasp neighbor time (sec): %f" %(time.time() - t0))
        
        #print(def_vec)
        #print(neighbor_vec)
        #=======================================================================
        # neighbor_dict = cs.convert_param_vector(neighbor_vec)
        # for p in def_config.keys():
        #     if neighbor_dict.get(p, None) != def_config[p]:
        #         print(p, neighbor_dict.get(p, None), def_config[p])
        #=======================================================================
        
    def test_lingeling(self):
        
        print("lingeling")
        
        cs = ConfigSpace(self.lingeling_pcs_file)
        
        t0 = time.time()
        for _ in xrange(1,10000):
            cs.get_random_config_vector()
        print("lingeling random configs time (sec): %f" %(time.time() - t0))
        
    def test_convert_lingeling(self):
        
        print("lingeling convert")
        cs = ConfigSpace(self.lingeling_pcs_file)
        def_config = cs.get_default_config_dict()
        def_vec = cs.convert_param_dict(def_config)
        def_config_back = cs.convert_param_vector(def_vec)
        #print(def_config)
        #print(def_vec)
        
        for param, value in def_config.iteritems():
            assert value == def_config_back[param], "%s: %s vs %s" %(param, str(value), str(def_config_back[param]))

    def test_neighbor_lingeling(self):
        print("lingeling neighbor")

        cs = ConfigSpace(self.lingeling_pcs_file)
        def_config = cs.get_default_config_dict()
        def_vec = cs.convert_param_dict(def_config)
        
        
        t0 = time.time()
        for _ in xrange(0,10000):
            neighbor_vec = cs.get_random_neighbor(def_vec)
        print("lingeling neighbor time (sec): %f" %(time.time() - t0))
        
        #print(def_vec)
        #print(neighbor_vec)
        #=======================================================================
        # neighbor_dict = cs.convert_param_vector(neighbor_vec)
        # for p in def_config.keys():
        #     if neighbor_dict.get(p, None) != def_config[p]:
        #         print(p, neighbor_dict.get(p, None), def_config[p])
        #=======================================================================

if __name__ == '__main__':
    unittest.main()