# Some Experimentation with Profiling.

from pyinstrument import Profiler
profiler = Profiler()
profiler.start()
# code to profile


def isa(n):
    for i in range(n):
        for j in range(n):
            continue
def n_cubed(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                continue;
                #print(i*j*k);


n_cubed(200)
isa(100)

profiler.stop()
profiler.print()

'''

Todo : 

Profile the methods of InventoryManager.py
display()
takeInputs() ? -> Might need some handling.

'''