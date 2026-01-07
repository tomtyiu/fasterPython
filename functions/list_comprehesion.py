# avoid manual loop
# Reference: https://dev.to/rayeanmahmud/7-ways-to-speed-up-your-python-code-5id
squares = [i*i for i in range(10000)]
