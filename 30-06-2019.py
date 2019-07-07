
#Exception
import sys

try:
    number1=int(input(''))

except FileNotFoundError:
    print('exception')
except:
    print('exception')
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])
finally:
    print('Complete')

