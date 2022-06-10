import simpy


class Machine:

    def __init__(self, env, name, workTime):
        self.name = name
        self.workTime = workTime
        self.env = env
        self.productInQueue = env.event()

        self.queue = []

    def reset(self, env):
        self.queue = []
        self.env = env

    # Add product to queue and inform machine
    def addProduct(self, product):
        self.queue.append(product)
        self.productInQueue.succeed()
        self.productInQueue = self.env.event()


    # Get and return Next product from queue
    def nextProductFromQueue(self):
        if (len(self.queue) > 0):
            current = self.queue.pop(0)
            return current


    # Infinite process to handle products from queue in specified work time
    # Inform product when task is completed
    def run(self):
        while True:
            product = self.nextProductFromQueue()

            if(product):
                print('Time: ' + str(self.env.now) + '; Donut entered: (' + str(self) + ')')
                yield self.env.timeout(self.workTime)
                product.stepDone.succeed()
                product.stepDone = self.env.event()
            else:
                yield self.productInQueue
            

    def __repr__(self):
        return self.name


    def __str__(self):
        return self.name + '; ' + str(self.workTime) + ' min; Queue Length: ' + str(len(self.queue))
