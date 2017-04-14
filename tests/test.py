import timeit

if __name__ == "__main__":
    print(timeit.timeit("base64.b64encode(b'whatever')", setup="import base64"))