# Actor-Critic-Lunar-Lander-Experiment
An experiment with an actor-critic model in OpenAI Gym's Lunar Lander environment. Code is a small variant of https://github.com/nikhilbarhate99/Actor-Critic-PyTorch

Set up (for Windows):

Requirements:
https://github.com/openai/gym  
  `git clone https://github.com/openai/gym.git`  
  `cd gym`    
  `pip install -e .`  
  
Clone this repository locally:  
`git clone https://github.com/BenjaminDantonio/Actor-Critic-Lunar-Lander-Experiment`

Move to the directory. To edit the environment's starting altitude, open   
`gym\gym\envs\box2d\lunar_lander.py`   
and edit the `VIEWPORT_H` constant to change the starting altitude.   

To change the model's hyperparameters such as learning rate and step back multiplier, open    
`Actor-Critic-Lunar-Lander-Experiment\train.py`     
and edit `lr` for learning rate and `step_rate` for step back multiplier.

When all values are set, run   
`python train.py`   
in the `\Actor-Critic-Lunar-Lander-Experiment` directory.

Observe results in terminal. Results will also be written to a csv, and your model will be saved.
