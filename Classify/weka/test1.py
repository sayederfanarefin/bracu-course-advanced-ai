import weka.core.jvm as jvm 
jvm.start()

from weka.classifiers import Classifier
from weka.core.converters import Loader
loader = Loader(classname="weka.core.converters.ArffLoader")

iris_inc = loader.load_file("iris.arff", incremental=True)
iris_inc.class_is_last()

print(iris_inc)

cls = Classifier(classname="weka.classifiers.bayes.NaiveBayesUpdateable")
cls.build_classifier(iris_inc)
for inst in loader:
    cls.update_classifier(inst)

print(cls)
