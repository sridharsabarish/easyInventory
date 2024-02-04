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
# def n():
#     for i in range(100):
#         continue
#         #print(i);
# n()


n_cubed(200)
isa(100)

profiler.stop()
profiler.print()