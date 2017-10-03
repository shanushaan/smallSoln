from queue import Queue
import threading
import random
import time
import pickle

max_tp=10

q = Queue()
fred = [i for i in range(100)]
threadDict ={}


class WorkItem(object):
    def __init__(self, fn, *args, **kwargs):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except BaseException as e:
            raise e
        else:
            return result

    def __repr__(self):
        return "WorkItem :" + fn.__name__ 


def worker (executer, work_queue):
    try:
        while True:
            # get the next item and run
            work_item=work_queue.get(block=True)
            if work_item is not None:
                return work_item.run()
                del work_item
            else:
                #read from file.
                try:
                    work_item = pickle.load(executer.fileH)
                    returnwork_item.run()
                except pickle.PickleError as ex:
                    print ("Error while unpickling "+ str(ex))
    except BaseException as ex:
        print ("Error in base Worker" +str(ex))
        


class Executer(object):

    def __init__(self, maxThreads=None):
        if maxThreads <=0:
            raise Exception("Please provide a valid >0 value for threads")
        if maxThreads == None:
           maxThreads = 5 #setting default.
        self.maxThreads = maxThreads
        self.taskQ = Queue()
        self.threads=set()
        self.Qlock=threading.Lock()
        self.fileH = open("tmp.txt","wb+")
        self.stop=False


    def addTask (self, func, *args, **kwargs):
        if self.stop:
            raise BaseException("Cannot add while the system is getting down")
        
        with self.Qlock:
            if not self.taskQ.full():
                self.taskQ.put(WorkItem(func,*args,**kwargs))
            else:
                pickle.dump(WorkItem(func,*args,**kwargs),self.fileH,pickle.HIGHEST_PROTOCOL)
            self.addThread()
            
    def addThread(self):
        if len(self.threads)<self.maxThreads:
            t = threading.Thread(target=worker, args=(self, self.taskQ))
            t.daemon=True
            t.start()
            self.threads.add(t)
            threadDict[t]=self.taskQ
            

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stopExecutor(wait=True)
        self.fileH.close()
        return False

    def stopExecutor(self, wait=True):
        with self.Qlock:
            self.shutdown = True
            self.taskQ.put(None)
        if wait:
            for t in self.threads:
                t.join()
    
    
    
# change fx and calls as per reuirement. 
def f(x):
    res = x * x
    if q.full():
        print ("Full" )
    else:
        q.put(res)
 
def main():
    with Executer(maxThreads=max_tp) as executor:
        for num in fred:
            executor.addTask(f, num)
    #
    while not q.empty():
        print (q.get())
 
####################
 
if __name__ == "__main__":
   main()


