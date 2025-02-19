import abc


#######################################################################
# autos
#######################################################################
class AbsAuto(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass


class FordFiesta(AbsAuto):
    def start(self):
        print("Ford Fiesta running cheaply.")

    def stop(self):
        print("Ford Fiesta shutting down.")


class LincolnMKS(AbsAuto):
    def start(self):
        print("Lincoln MKS running smoothly.")

    def stop(self):
        print("Lincoln MKS shutting down.")


class FordMustang(AbsAuto):
    def start(self):
        print("Ford Mustang roaring and ready to go!")

    def stop(self):
        print("Ford Mustang shutting down.")


class CadillacCTS(AbsAuto):
    def start(self):
        print("Cadillac CTS purring luxuriously.")

    def stop(self):
        print("Cadillac CTS shutting down.")


class ChevyCamaro(AbsAuto):
    def start(self):
        print("Chevy Camaro V8 sounding awesome!")

    def stop(self):
        print("Chevy Camaro shutting down.")


class ChevySpark(AbsAuto):
    def start(self):
        print("Chevy Spark running efficiently.")

    def stop(self):
        print("Chevy Spark shutting down.")


#######################################################################
# factories
#######################################################################


class AbsFactory(abc.ABC):
    @staticmethod
    @abs.abstractmethod
    def create_economy():
        pass

    @staticmethod
    @abs.abstractmethod
    def create_sport():
        pass

    @staticmethod
    @abs.abstractmethod
    def create_luxury():
        pass


class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return LincolnMKS()


class GMFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return ChevySpark()

    @staticmethod
    def create_sport():
        return ChevyCamaro()

    @staticmethod
    def create_luxury():
        return CadillacCTS()


#######################################################################
# main
#######################################################################

if __name__ == "__main__":
    for factory in FordFactory, GMFactory:
        car = factory.create_economy()
        car.start()
        car.stop()
        car = factory.create_sport()
        car.start()
        car.stop()
        car = factory.create_luxury()
        car.start()
        car.stop()
