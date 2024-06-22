'''
    Answers to multiple choice questions.
'''
from Softmax import Softmax, SoftmaxStable
from Ward import Ward, Student, Teacher, Doctor
from Stack import MyStack
from Queue import MyQueue

import torch
import torch.nn as nn


def main():
    print('Question 1:')  # C
    data = torch.Tensor([1, 2, 3])
    softmax_function = nn.Softmax(dim=0)
    output = softmax_function(data)
    print(output)

    print('Question 2:')  # B
    data = torch.Tensor([5, 2, 4])
    my_softmax = Softmax()
    output = my_softmax(data)
    print(output)

    print('Question 3:')  # C
    data = torch.Tensor([1, 2, 300000000])
    my_softmax = Softmax()
    output = my_softmax(data)
    print(output)

    print('Question 4:')  # A
    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    print(output)

    print('Question 5:')  # A
    student1 = Student(name=" studentZ2023 ", yob=2011, grade="6")
    assert student1._yob == 2011
    student1.describe()

    print('Question 6:') # B
    teacher1 = Teacher(name=" teacherZ2023 ", yob=1991, subject=" History ")
    assert teacher1 . _yob == 1991
    teacher1 . describe()

    print('Question 7:') # A
    doctor1 = Doctor ( name =" doctorZ2023 ", yob =1981 , specialization =" Endocrinologists ")
    assert doctor1 . _yob == 1981
    doctor1.describe ()

    print('Question 8:') # C
    student1 = Student(name="studentA", yob=2010, grade="7")
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor1 = Doctor(name="doctorA", yob=1945, specialization="Endocrinologists")
    doctor2 = Doctor(name="doctorB", yob=1975, specialization="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    print(ward1.count_doctor())
    
    print('Question 9:') # B
    stack1 = MyStack(capacity = 5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print(stack1.is_full() )

    print('Question 10:') # B
    stack1 = MyStack(capacity = 5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print(stack1.top())

    print('Question 11:') # A
    queue1 = MyQueue(capacity = 5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)
    print(queue1.is_full())
    
    print('Question 12:') # D
    queue1 = MyQueue(capacity = 5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)
    print(queue1.front())

if __name__ == "__main__":
    main()
