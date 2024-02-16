'''Write a class method get_all_instances() in a class called
 InstanceCounter that returns the total number of instances
  created using cls.'''

class InstanceCounter:
    _instances = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        InstanceCounter._instances += 1
    @classmethod
    def get_all_instances(cls):
        return cls._instances
Instance1 = InstanceCounter("k",41)
Instance2 = InstanceCounter("e",54)
Instance3 = InstanceCounter("w",65)
No_of_instances = InstanceCounter.get_all_instances()
print(No_of_instances)



