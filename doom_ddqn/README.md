## ViZDoom DDQN 

A DDQN training and evaluation framework for VizDoom supporting multiple scenarios and architectures. Allows training and testing either a DDQN from scratch or using MobileNetV2 as a base. Includes a demo of a pretrained network's performance on the 'Corridor' scenario. 

This project highlights:
- Model evaluation: achieves over 94% win rate on Corridor
- Experimentation: select different scenarios, architectures, and agent hyperparameters (reward shaping and frame skipping) 
- Clean, production-like structure

---

## Features
- View trained DDQN winning VizDoom Corridor scenario
- Trainer for different VizDoom scenarios, alternate DDQN architectures, and agent hyperparameters (reward shaping and frame skipping)
- Test trained DDQN and view testing metrics
- No dataset required

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
│        └── main_model.pth # Pretrained model<br>
├── Dockerfile # Container for running the interactive demo<br>
├── requirements.txt # Dependencies for running the interactive demo<br>
├── local_requirements.txt # Dependencies for full functionality of all scripts<br>
└── README.md # This file<br>

---

## Quick Start for Docker

1\. Build the Docker image

docker build -t demo .

2\. Run the demo

docker run --init -p 5000:5000 demo

Note: if prompted, please allow permission

3\. View the demo

open a web browser and navigate to 127.0.0.1:5000

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





