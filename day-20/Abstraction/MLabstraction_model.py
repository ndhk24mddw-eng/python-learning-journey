#Build an ML Model abstraction.
from abc import ABC,abstractmethod

class MLModel(ABC):
    @abstractmethod
    def train(self,data):
        pass
    @abstractmethod
    def predict(self,data):
        pass

class LinearModel(MLModel):
    def train(self,data):
           print("Linear Model training:", data)
    def predict(self,data):
        print("Linear Model prediction:", data)

class NeuralNetwork(MLModel):
    def train(self,data):
        print('training',data)
    def predict(self,data):
        print('predict',data)

def run_model(model):
    model.train("training data")
    model.predict("test data")
run_model(LinearModel())
run_model(NeuralNetwork())