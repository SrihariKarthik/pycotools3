#-*-coding: utf-8 -*-
"""

 This file is part of pycotools.

 pycotools is free software: you can redistribute it and/or modify
 it under the terms of the GNU Lesser General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 pycotools is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public License
 along with pycotools.  If not, see <http://www.gnu.org/licenses/>.


 $Author: Ciaran Welsh

Module that tests the operations of the _Base base test

"""

import site
site.addsitedir('C:\Users\Ciaran\Documents\pycotools')
site.addsitedir('/home/b3053674/Documents/pycotools')
import pandas
import pycotools
from pycotools.Tests import _test_base
import unittest
import os
import pickle
import test_data
import numpy
import shutil
import glob



class ParameterEstimationTests(_test_base._BaseTest):
    def setUp(self):
        super(ParameterEstimationTests, self).setUp()
        self.TC1 = pycotools.tasks.TimeCourse(self.model, end=1000, step_size=100,
                                               intervals=10, report_name='report1.txt')

        pycotools.misc.correct_copasi_timecourse_headers(self.TC1.report_name)
        ## add some noise
        data1 = pycotools.misc.add_noise(self.TC1.report_name)

        ## remove the data
        os.remove(self.TC1.report_name)

        ## rewrite the data with noise
        data1.to_csv(self.TC1.report_name, sep='\t')

        self.MPE = pycotools.tasks.MultiParameterEstimation(
            self.model,
            self.TC1.report_name,
            copy_number=2,
            pe_number=8,
            method='genetic_algorithm',
            population_size=10,
            number_of_generations=10,
            results_directory='test_mpe')
        self.list_of_tasks = '{http://www.copasi.org/static/schema}ListOfTasks'

        self.MPE.write_config_file()
        self.MPE.setup()
        # self.MPE.run()

    def test(self):
        # pass
        df = pycotools.viz.Parse(self.MPE).data
        pl = pycotools.tasks.ProfileLikelihood(self.model, df=df, index=[0,1])
        for model in pl.model_dct:
            for param in pl.model_dct[model]:
                pass
                # print pl.model_dct[model][param].save()
                # print pl.model_dct[model][param].fit_item_order
                # pl.model_dct[model][param]
        # pl.model_dct[0]['A'].open()
        # pl.insert_parameters()
        # df = pandas.DataFrame({'A':100, 'B':200}, index=[0])
        # print pycotools.model.InsertParameters(self.model, df=df)






if __name__=='__main__':
    unittest.main()

































































