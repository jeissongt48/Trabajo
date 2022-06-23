import threading
class MiThread(threading.Thread):
      def __init__(self, num):
          threading.Thread.__init__(self)
          self.num = num
      def run(self):
          print ('Soy el hilo', self.num)
          print ('Soy el hilo principal')
for i in range(0, 10):
   t = MiThread(i)
   t.start()
   t.join()
# sincronización
lista = []
lock = threading.Lock()
def anyadir(obj):
 lock.acquire()
 lista.append(obj)
 lock.release()
def obtener():
 lock.acquire()
 obj = lista.pop()
 lock.release()
 return obj
 #ejemplo de notify
 lista = []
cond = threading.Condition()
def consumir():
 cond.acquire()
 cond.wait()
 obj = lista.pop()
 cond.release()
 return obj
def producir(obj):
 cond.acquire()
 lista.append(obj)
 cond.notify()
 cond.release()
 #sólo un thread pueda acceder al método 
 def synchronized(lock):
     def dec(f):
         def func_dec(*args, **kwargs):
             lock.acquire()
             try:
                 return f(*args, **kwargs)
             finally:
                  lock.release()
         return func_dec
     return dec
class MyThread(threading.Thread):
    @synchronized(mi_lock)
    def run(self):
        print ('metodo sincronizado')