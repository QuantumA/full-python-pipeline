from abc import abstractmethod, ABCMeta


class Shape(metaclass=ABCMeta):

   @abstractmethod
   def area(self):
      pass

   def which(self):
       return self.__class__.__name__

