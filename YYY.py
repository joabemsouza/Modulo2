
class Corretor():
    def __init__(self,in_name_arquivo = None):
        self.name_arquivo = in_name_arquivo
        self.creat_dict()
        
    def le_arquivo (self):
        f = open(self.name_arquivo,'r') # sai zoado pq tem que codificar direito
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in lines]
        return(lines)

    def creat_dict(self):
        lines = self.le_arquivo()
        dict={}
        for test_str in lines:
            dict1 = {test_str[0:i]+test_str[i+1:]: test_str for i in range (len(test_str))}
            dict.update(dict1)
        return dict
            
    def sugere(self, palavra):
        dict = self.creat_dict()
        sugerida = ""
        for i in dict:
            if palavra == i:
                sugerida = dict[i]
                break   
            elif palavra == dict[i]:
                sugerida = palavra
                break
                   
        return sugerida

    
#x = Corretor('corpus.txt')
#lines = x.le_arquivo()
#dictt = x.creat_dict()
#teste = x.sugere('palara')
#print(teste)