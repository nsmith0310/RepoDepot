# ViZDoom DDQN 


## Summary

A DDQN training and evaluation framework for VizDoom supporting multiple scenarios and architectures. Allows training and testing either a DDQN from scratch or using MobileNetV2 as a base. Includes a demo of a pretrained network's performance on the 'Corridor' scenario. 

---

## Description

This project was developed to explore the ability of DDQN to achieve quality performance on the classic video game Doom. It uses a training framework that selects different scenarios and reward-shaping values, chooses DDQN network architecture, then trains the agent via the DDQN reinforcement learning algorithm. The training method includes reward-shaping, experience replay buffer, frame stacking, frame skipping, and two networks to stabilize training. This project also includes a script to evaluate the trained agent on a number of metrics like win rate, time-per-episode, and number of kills. The final best model achieves over 94% win rate on the "Deadly Corridor" scenario.   

---

## DDQN agent

Option A: Train a DDQN network entirely from scratch. 

Option B: Utilize pretrained MobileNetV2 as base and only train head.

---

## Tech Stack

- Language: Python
- ML / DL: PyTorch
- Data: NumPy, Pillow
- Visualization: Matplotlib
- MLOps / Tools: Git, Docker

---

## Folder Structure
<br>
doom_ddqn/<br>
├── src/ # Scripts <br>
│ ├── demo.py # Demo script <br>
│ ├── test.py # Evaluate trained model on 500 trials <br>
│ ├── train.py # Train DDQN; supports training using MobileNetv2 base or from scratch<br>
│ ├── ddqn.py # DDQN class and methods<br>
│ ├── utility.py # Utility library <br>
│ └── model/ # Pretrained model<br>
├── Dockerfile # Container for running the interactive demo<br>
├── requirements.txt # Dependencies for running the interactive demo<br>
├── local_requirements.txt # Dependencies for full functionality of all scripts<br>
└── README.md # This file<br>

---

## Demo

Observe the trained agent perform on "Deadly Corridor".

## Quick Start for Docker

1\. Build the Docker image

docker build -t demo .

2\. Run the demo

docker run --init -p 5000:5000 demo

Note: if prompted, please allow permission

3\. View the demo

open a web browser and navigate to http://localhost:5000

4\. End the demo

press CTRL+C

Note: you may have to press this multiple times 

---

## Running Locally

1\. Clone the repository

git clone --depth 1 --no-checkout https://github.com/nsmith0310/RepoDepot.git<br>
cd RepoDepot<br>
git sparse-checkout init --cone<br>
git sparse-checkout set doom_ddqn<br>
git checkout main<br>

2\. Install dependencies

pip install -r local_requirements.txt

3\. Run script of choice

python demo.py 
python test.py
python train.py

---

## License

All scripts, notebooks, and models are free to explore for educational purposes 

---

## Sources

Primary guide used for implementing the DDQN in PyTorch:

https://medium.com/@hkabhi916/mastering-convolutional-deep-q-learning-with-pytorch-a-comprehensive-guide-0114742a0a62

A very helpful article on understanding frame skipping:

https://danieltakeshi.github.io/2016/11/25/frame-skipping-and-preprocessing-for-deep-q-networks-on-atari-2600-games/





