#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:51:44 2021

@author: kurkela
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
#from analysis_spec import roidata_save_dir, roi_1_name

roi_list = ['ANG', 'PRC', 'PHC']
sub_list = ['sub-01', 'sub-02', 'sub-03', 'sub-04', 'sub-07', 'sub-08', 'sub-09', 'sub-10', 'sub-11', 'sub-12', 'sub-13', 'sub-14', 'sub-15', 'sub-16', 'sub-18', 'sub-19', 'sub-21', 'sub-22', 'sub-23', 'sub-24']
run_list = [1,2,3,4]
roidata_save_dir = '/gsfs0/data/kurkela/Desktop/PyMVPD/results/roidata_noMotion/'
var_expl = []
subject = []
roi = []
run_num = []

# Iterate over subjects, ROIs, runs
for roi_name in roi_list:
    for sub in sub_list:
        for run in run_list:
            
            # Load Data
            filedir = roidata_save_dir+'roi_run_'+str(run)+'/'
            filename = sub+'_'+roi_name+'_data_run_'+str(run)+'.npy'
            filepath = filedir + filename
            roi_data = np.load(filepath)
            
            # perform PCA analysis
            pca_ROI_1 = PCA(n_components=3)
            pca_ROI_1.fit(roi_data)
            
            # Percentage of variance explained by the first principal component
            var_expl.append(pca_ROI_1.explained_variance_ratio_[0])
            subject.append(sub)
            roi.append(roi_name)
            run_num.append(run)
            
d  = {'subject': subject, 'run': run_num, 'roi': roi, 'var_expl': var_expl}
df = pd.DataFrame(data=d)
df.to_csv('roi_homogeneity.csv', index=False)