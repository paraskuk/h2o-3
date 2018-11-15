import h2o
from h2o.estimators import H2OXGBoostEstimator


from tests import pyunit_utils


def pubdev_5265():

    data = h2o.import_file(pyunit_utils.locate("smalldata/testng/airlines_train.csv"))
    for i in range(0,500):
        xgb = H2OXGBoostEstimator(ntrees = 1, max_depth= 2)
        xgb.train(x = ["Origin","Distance"],y="IsDepDelayed", training_frame=data)
        print(i)

if __name__ == "__main__":
    pyunit_utils.standalone_test(pubdev_5265)
else:
    pubdev_5265()
