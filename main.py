from machine import *
from product import SugarDonut
from env import DonutShop
import simpy

# machines = {}
# machines[1] = Machine(1, 'Mixer', 3)
# machines[2] = Machine(2, 'Donut Cutter', 1)
# machines[3] = Machine(3, 'deepFryer', 5)
# machines[4] = Machine(4, 'Glazing Station', 2)
#


donuts_produced=0 #global variable
#Generates Entities, in this case Donuts that enter the factory
def donut_generator_sugar_donut(env, donuts_interarrival_time, baking_machine,mixing_machine):
    donut_number = 0

    while True:
        #create instance of activity generator
        bake = activity_generator_sugar_donut_production(env, baking_machine,mixing_machine, donut_number)

        #run the activity generator for this donut
        env.process(bake)

        #time till next donut enters queue
        t = donuts_interarrival_time

        #freeze till time has passed
        yield env.timeout(t)

        donut_number+=1



def activity_generator_sugar_donut_production(env, baking_machine, mixing_machine, donut_number):
    baking_name=baking_machine.name
    mixing_name=mixing_machine.name
    time_entered_for_mixing = env.now
    global donuts_produced

    print(f"Donut {donut_number} entered {mixing_name} queue at {time_entered_for_mixing:.2f}")
    with mixing_machine.machine.request() as req:
        yield req

        # calculate time donut was queuing
        time_left_queue_for_mixing = env.now
        print(f"Donut {donut_number} was transferred into {mixing_name}  at {time_left_queue_for_mixing:.2f}")
        time_in_queue_for_mixing = time_left_queue_for_mixing - time_entered_for_mixing
        print(f"Donut {donut_number} was in {mixing_name} queue for {time_in_queue_for_mixing:.2f} minutes")

        mixing_time = mixing_machine.time
        yield env.timeout(mixing_time)

    time_entered_for_baking = env.now

    print(f"Donut {donut_number} entered {baking_name} queue at {time_entered_for_baking:.2f}")
    with baking_machine.machine.request() as req:
        yield req

        # calculate time donut was queuing
        time_left_queue_for_baking = env.now
        print(f"Donut {donut_number} was transferred into {baking_name} at {time_left_queue_for_baking:.2f}")
        time_in_queue_for_baking = time_left_queue_for_baking - time_entered_for_baking
        print(f"Donut {donut_number} was in {baking_name} queue for {time_in_queue_for_baking:.2f} minutes")

        baking_time = baking_machine.time
        yield env.timeout(baking_time)
    # baking_machine.work(env, donut_number)
    print(f"Donut {donut_number} finished at {env.now:.2f}")
    donuts_produced +=1


#setup parameters

donut_spawn= 2
mixing_time = 3
cutting_time = 1
baking_time = 5
glazing_time = 2

Sim_duration=100 # 24 hours

#setup simulation environment
env = simpy.Environment()

#setup resources
baking_machine=Single_Machine(env,"baking machine",baking_time)
mixing_machine=Single_Machine(env,"mixing machine",mixing_time)
cutting_machine=Single_Machine(env,"cutting machine", cutting_time)
glazing_machine=Single_Machine(env,"glazing machine", glazing_time)

#start arrivals generator
env.process(donut_generator_sugar_donut(env, donut_spawn, baking_machine,mixing_machine))

#run the simulation
env.run(until=Sim_duration)

print(f"Total amount of {donuts_produced} donuts produced")

# def Work(env,Single_Machine,donut_number):
#     print("WORK CALLS")
#     station = Single_Machine.name
#     time_entered = env.now
#     print(f"Donut {donut_number} entered {station} queue at {time_entered:.2f}")
#     # request machine
#     with Single_Machine.machine.request() as req:
#         # Freeze until machine is available
#         yield req
#         # calculate time donut was queuing
#         time_left_queue = env.now
#         print(f"Donut {donut_number} left {station} queue at {time_left_queue:.2f}")
#         time_in_queue = time_left_queue - time_entered
#         print(f"Donut {donut_number} was in {station} queue for {time_in_queue:.2f} minutes")
#
#         work_time = Single_Machine.time
#
#         yield env.timeout(work_time)

#defines Activity of entity