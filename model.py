import random

class Model(object):
    def __init__(self):
        self._Nmax = 100
        self._Tmax = 10
        self._T = self._Tmax
        self._segreto = None
    def reset(self):
        '''Questo metodo resetta lo stato del gioco.
        Imposta il segreto ad un valore randomico intero tra 0 e Nmax.
        Ripristina il numero di tentativi rimanenti'''
        self._segreto = random.randint(0, self._Nmax)
        self._T = self._Tmax
        print(self._segreto)

    def play(self, tentativo):
        '''
        Questo metodo riceve come argomento un valore intero che sarà
        il tentativo del giocatore e lo confronta con il segreto
        :return:
        -1 se il segreto è piu piccolo del tentativo
        0 se il tentativo è uguale al segreto
        1 se il segreto è piu grande del tentativo
        2 se non ci sono più vite disponibili
        '''
        self._T -= 1

        if tentativo == self._segreto:
            '''Ho vinto!'''
            return 0
        if self._T <= 0:
            '''Non ho più vite!'''
            return 2
        if tentativo > self._segreto:
            '''Il tentativo del utente è più grande del segreto'''
            return -1
        else:
            return 1
    @property
    def Nmax(self):
        return self._Nmax
    @property
    def Tmax(self):
        return self._Tmax
    @property
    def T(self):
        return self._T
    @property
    def segreto(self):
        return self._segreto

if __name__ == '__main__':
    m = Model()
    m.reset()
    print(m.play(10))
    print(m.play(20))
    print(m.play(30))
    print(m.play(40))
    print(m.play(50))
    print(m.play(60))
    print(m.play(70))
