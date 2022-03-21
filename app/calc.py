from dataclasses import dataclass
from enum import Enum


class ArithmeticOperation(Enum):
    ADDITION = '+'
    MULTIPICATION = '*'


@dataclass
class Calcutation:
    firstNum: int
    secondNum: int
    operation: ArithmeticOperation

    def calculate(self):
        if self.operation == ArithmeticOperation.ADDITION:
            return self.firstNum + self.secondNum
        elif self.operation == ArithmeticOperation.MULTIPICATION:
            return self.firstNum * self.secondNum
        else:
            raise AttributeError('no operation found')
