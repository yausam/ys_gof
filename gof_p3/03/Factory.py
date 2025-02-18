import abc

from importlib import import_module
from inspect import getmembers, isabstract, isclass


#######################################################################
# autos
#######################################################################


class AbsAuto(abc.ABC):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass


class ChevyVolt(AbsAuto):
    def start(self):
        print("%s running with shocking power!" % self.name)

    def stop(self):
        print("%s shutting down." % self.name)


class FordFusion(AbsAuto):
    def start(self):
        print("%s running cooly!" % self.name)

    def stop(self):
        print("%s shutting down." % self.name)


class JeepSahara(AbsAuto):
    def __init__(self, name):
        self._name = name

    def start(self):
        print("%s running ruggedly." % self.name)

    def stop(self):
        print("%s shutting down." % self.name)


class NullCar(AbsAuto):
    def start(self):
        print('Unknown car "%s".' % self.name)

    def stop(self):
        pass


#######################################################################
# factories
#######################################################################


class AbsFactory(abc.ABC):
    @abc.abstractmethod
    def create_auto(self):
        pass


class ChevyFactory(AbsFactory):
    def create_auto(self):
        self.chevy = chevy = ChevyVolt()
        chevy.name = "Chevy Volt"
        return chevy


class FordFactory(AbsFactory):
    def create_auto(self):
        self.ford = ford = FordFusion()
        ford.name = "Ford Fusion"
        return ford


class JeepFactory(AbsFactory):
    def create_auto(self):
        self.jeep = jeep = JeepSahara("Jeep Sahara")
        return jeep


#######################################################################
# factory loader
#######################################################################


def load_factory(factory_name):
    try:
        factory_module = import_module("." + factory_name, "factories")
    except ImportError:
        factory_module = import_module(".null_factory", "factories")

    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m))

    for _, _class in classes:
        if issubclass(_class, AbsFactory):
            return _class()


#######################################################################
# main
#######################################################################

if __name__ == "__main__":
    for factory_name in (
        "chevy_factory",
        "jeep_factory",
        "ford_factory",
        "tesla_factory",
    ):

        factory = load_factory(factory_name)
        car = factory.create_auto()

        car.start()
        car.stop()
