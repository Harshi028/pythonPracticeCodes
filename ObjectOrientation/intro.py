class Student:
    def learn(self):
        print(self.name,'inside learning method')
    def play():
        print('Inside play method ')

s1 = Student()

# s1.play() #Student.play() takes 0 positional arguments but 1 was given --parameter is missing
s1.name = 'pooja'
print('name is',s1.name)
s1.learn()
