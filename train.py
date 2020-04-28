from test import test
from model import ActorCritic
import torch
import torch.optim as optim
import gym
import csv
from datetime import datetime
import time 

def train():
    # Defaults parameters:
    #    gamma = 0.99
    #    lr = 0.02
    #    betas = (0.9, 0.999)
    #    random_seed = 543
    random_seed = 1444
    proportional = True
    step_rate=2
    start=800
    flie_name="data from test {} random seed {} proportional {} step rate {} start {}.csv".format(time.time(), random_seed, proportional, step_rate, start)
    c = csv.writer(open(flie_name, 'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    c.writerow(["Episode", "length", "reward", "time since start"])
    start_time=time.time()
    render = False
    gamma = 0.99
    lr = 0.01
    betas = (0.9, 0.999)
    
    
    torch.manual_seed(random_seed)
    
    env = gym.make('LunarLander-v2')
    env.seed(random_seed)
    
    policy = ActorCritic()
    name_swag="network_from_test_1588051408.5123308_random_seed_543_proportional_True_step_rate_1.1_start_200_step_1.pth"
    policy.load_state_dict(torch.load('./preTrained/{}'.format(name_swag)))
    optimizer = optim.Adam(policy.parameters(), lr=lr, betas=betas)
    print(lr,betas)
    height=start
    step=1
    while height<801:
        running_reward = 0
        for i_episode in range(0, 10000):
            state = env.reset(start=height)
            for t in range(10000):
                action = policy(state)
                state, reward, done, _ = env.step(action)
                policy.rewards.append(reward)
                running_reward += reward
                if render and i_episode > 1000:
                    env.render()
                if done:
                    break
                        
            # Updating the policy :
            optimizer.zero_grad()
            loss = policy.calculateLoss(gamma)
            loss.backward()
            optimizer.step()        
            policy.clearMemory()
            
            # saving the model if episodes > 999 OR avg reward > 200 
            #if i_episode > 999:
            #    torch.save(policy.state_dict(), './preTrained/LunarLander_{}_{}_{}.pth'.format(lr, betas[0], betas[1]))
            
            if running_reward > 4000:
                save_name="network_from_test_{}_random_seed_{}_proportional_{}_step_rate_{}_start_{}_step_{}.pth".format(time.time(), random_seed, proportional, step_rate, start, step)
                torch.save(policy.state_dict(), './preTrained/'+save_name)
                print("########## Solved! ##########")
                c.writerow([i_episode, t, running_reward, start_time-time.time(),"Solved"])
                test(name=save_name)
                break
                
            if i_episode % 20 == 0:
                running_reward = running_reward/20
                print('Episode {}\tlength: {}\treward: {}'.format(i_episode, t, running_reward))
                c.writerow([i_episode, t, running_reward, start_time-time.time()])
                running_reward = 0
        height*=step_rate
        step+=1
if __name__ == '__main__':
    train()
