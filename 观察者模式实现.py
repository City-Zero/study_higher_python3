# coding=utf-8


#观察者
class Observer:
    def update(self,stat):
        return

    def display(self):
        return

#被观察者
class Observed:
    def registerObserver(self,observer):
        return

    def removeObserver(self,observer):
        return

    def notifyObservers(self):
        return


class plant(Observed):
    def __init__(self):
        self.observers = []
        self.status = 'new'
        return

    def registerObserver(self,observer):
        self.observers.append(observer)
        return

    def removeObserver(self,observer):
        self.observers.remove(observer)
        return

    def notifyObservers(self):
        for item in self.observers:
            item.update(self.status)
        return

    def statusChanged(self):
        self.notifyObservers()

    def setStatus(self,status):
        self.status = status
        self.statusChanged()

class planter(Observer):
    def __init__(self,plant):
        self.plant = plant
        self.doing = 'nothing'
        plant.registerObserver(self)
        return

    def update(self,stat):
        self.doing = 'work' if stat == 'ill' else 'nothing'
        self.display()
        return

    def display(self):
        print('I am planter,my plant now is %s,i doing %s.' % \
              (self.plant.status,self.doing))
        return

class eater(Observer):
    def __init__(self,plant):
        self.plant = plant
        self.doing = 'nothing'
        plant.registerObserver(self)
        return

    def update(self,stat):
        self.doing = 'work' if stat == 'ok' else 'nothing'
        self.display()
        return

    def display(self):
        print('I am eater,my plant now is %s,i doing %s.' % \
              (self.plant.status,self.doing))
        return


if __name__ == '__main__':
    tree = plant()
    display = planter(tree)
    tree.setStatus('ill')
    display = eater(tree)
    tree.setStatus('ok')
    tree.setStatus('unknow')