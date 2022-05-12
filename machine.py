import simpy


class Single_Machine:

    def __init__(self, env, name, time, amount=1):
        self.name = name
        self.time = time
        self.machine = simpy.Resource(env, amount)

    def work(self, env, donut_number):
        station = self.name
        time_entered = env.now
        print(f"Donut {donut_number} entered {station} queue at {time_entered:.2f}")
        # request machine
        with self.machine.request() as req:
            # Freeze until machine is available
            yield req
            # calculate time donut was queuing
            time_left_queue = env.now
            print(f"Donut {donut_number} left {station} queue at {time_left_queue:.2f}")
            time_in_queue = time_left_queue - time_entered
            print(f"Donut {donut_number} was in {station} queue for {time_in_queue:.2f} minutes")

            work_time = self.time

            yield env.timeout(work_time)



class Machine:

    def __init__(self, id, name, workTime):
        self.name = name
        self.workTime = workTime

        self.queue = []

    def addProduct(self, product):
        self.queue.append(product)

    def nextProduct(self):
        if (len(self.queue) > 0):
            current = self.queue.pop(0)
            current.updateState()
        else:
            print('Nothing to do!')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name + '; ' + str(self.workTime) + ' min; Queue: ' + str(self.queue)
