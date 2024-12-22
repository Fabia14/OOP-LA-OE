from abc import ABC, abstractmethod

class Pagong(ABC):
    @abstractmethod
    def langoy(self):
        pass

class Leonardo(Pagong):
    def langoy(self):
        return "Leonardo"

class MichaelAngelo(Pagong):
    def langoy(self):
        return "Michael Angelo"

class Donatello(Pagong):
    def langoy(self):
        return "Donatello"

class Raphael(Pagong):
    def langoy(self):
        return "Raphael"

if __name__ == "__main__":
    print("Ang hirap naman nito sir hahahhahaha")

    rap = Raphael().langoy()
    print(rap)

    le = Leonardo().langoy()
    print(le)

    donz = Donatello().langoy()
    print(donz)

    makz = MichaelAngelo().langoy()
    print(makz)