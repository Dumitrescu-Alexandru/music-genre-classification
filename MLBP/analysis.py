
import pandas as pd
import numpy as np




class NN_heatmaps():
    learning_rate_ = [0.01, 0.03, 0.05, 0.1, 0.5]
    layers = [2, 3]
    dims_ = [[[264, 264 + 60], [264 + 60, 10]], [[264, 264 + 60], [264 + 60, 264 + 60], [264 + 60, 10]]]
    keep_prob_ = [1, 0.98, 0.95, 0.90]

    learning_rates = [0.001, 0.003, 0.005, 0.01, 0.03]
    keep_probs = [0.7, 0.8, 0.85, 0.9, 0.95]
    no_batches = 100
    heat_map_2_test = []
    heat_map_3_test = []
    heat_map_2_train = []
    heat_map_3_train = []
    heat_map_2_test_steps = []
    heat_map_3_test_steps = []
    heat_map_2_train_steps = []
    heat_map_3_train_steps = []

    def __init__(self):
        pass

    def convert_numpy(self):
        self.heat_map_2_test = np.array(self.heat_map_2_test)
        self.heat_map_3_test = np.array(self.heat_map_3_test)
        self.heat_map_2_train = np.array(self.heat_map_2_train)
        self.heat_map_3_train = np.array(self.heat_map_3_train)
        self.heat_map_2_test_steps = np.array(self.heat_map_2_test_steps)
        self.heat_map_3_test_steps = np.array(self.heat_map_3_test_steps)
        self.heat_map_2_train_steps = np.array(self.heat_map_2_train_steps)
        self.heat_map_3_train_steps = np.array(self.heat_map_3_train_steps)

    def hmaps(self):

        for no_layers in self.layers:
            for keep_prob in self.keep_probs:
                current_kp_train = []
                current_kp_test = []
                current_kp_test_steps = []
                current_kp_train_steps = []
                for learning_rate in self.learning_rates:
                    file_name = "results/TRAIN_LAYERS_" + str(no_layers) + "_KeepProb_" + str(keep_prob) + "_Batches_" + str(self.no_batches) + \
                                        "_LrnRate_" + str(learning_rate)
                    data = pd.read_csv(file_name, header=None)
                    train_results = data.values

                    file_name = "results/TEST_LAYERS_" + str(no_layers) + "_KeepProb_" + str(
                        keep_prob) + "_Batches_" + str(self.no_batches) + \
                                "_LrnRate_" + str(learning_rate)
                    data = pd.read_csv(file_name, header=None)
                    test_results = data.values
                    train_results[0:5,1]=-1
                    test_results[0:5,1]=-1
                    max_test = np.max(test_results[:,1])
                    max_test_iter = np.argwhere(test_results[:,1]==max_test)
                    max_test_iter = max_test_iter[0,0]*100
                    max_train = np.max(train_results[:,1])
                    max_train_iter = np.argwhere(train_results[:,1]==max_train)
                    max_train_iter = max_train_iter[0,0]*100
                    current_kp_train.append(max_train)
                    current_kp_test.append(max_test)
                    current_kp_test_steps.append(max_test_iter)
                    current_kp_train_steps.append(max_train_iter)
                if no_layers == 2:
                    self.heat_map_2_test.append(current_kp_test)
                    self.heat_map_2_train.append(current_kp_train)
                    self.heat_map_2_test_steps.append(current_kp_test_steps)
                    self.heat_map_2_train_steps.append(current_kp_train_steps)
                if no_layers == 3:
                    self.heat_map_3_test.append(current_kp_test)
                    self.heat_map_3_train.append(current_kp_train)
                    self.heat_map_3_test_steps.append(current_kp_test_steps)
                    self.heat_map_3_train_steps.append(current_kp_train_steps)


