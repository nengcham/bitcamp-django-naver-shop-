from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel


class TitanicTemplate(object):

    def __init__(self, train_fname, test_fname):
        self.dataset = Dataset()
        self.model = Model()
        self.titanic_model = TitanicModel(train_fname, test_fname)
