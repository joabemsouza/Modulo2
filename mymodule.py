
# variáveis a serem importadas

__all__ = ['variable1','variable2']

_variable0 = '_variable0: not imported'

variable1 = 'variable1: imported'
variable2 = 'variable2: imported'

variable3 = 'variable3: not imported'

if __name__ == '__main__':
    print('Module configuration')
    print(_variable0,variable1,variable2,variable2,)
