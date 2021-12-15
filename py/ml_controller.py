import sklearn
from sklearn.linear_model import LogisticRegression

class MLController:
    model = None

    def get_input(self, mlData: list) -> list:
        inputData: list = []
        for entry in mlData:
            sum = 0
            for elem in entry[3]:
                sum += elem
            len = entry[3].__len__()
            if (len != 0):
                inputData.append([int(entry[1]), int(len)])
            else:
                inputData.append([int(entry[1]), 0])
        return inputData

    def get_output(self, mlData: list) -> list:
        outputData: list = []
        for entry in mlData:
            outputData.append(int(entry[2]))
        return outputData

    def init_model(self, mlData: list):
        self.model = LogisticRegression(solver = 'liblinear')
        self.model = self.model.fit(self.get_input(mlData), self.get_output(mlData))

    def predict_for(self, inputData: list) -> list:
        return self.model.predict(inputData)