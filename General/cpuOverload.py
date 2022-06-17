def f(x):
    while 1:
        # ---bonus: gradually use up RAM---
        x += 10000  # linear growth; use exponential for faster ending: x *= 1.01
        y = list(range(int(x)))
        # ---------------------------------
        pass  # infinite loop, use up CPU


if __name__ == '__main__':  # name guard to avoid recursive fork on Windows
    import multiprocessing as mp
    n = mp.cpu_count() * 4  # multiply guard against counting only active cores
    with mp.Pool(n) as p:
        p.map(f, range(n))
