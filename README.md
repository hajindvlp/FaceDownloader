# About The Project

This project is a preparation stage for making a good GAN, more specifically a big dataset for face generation

you can get theoretically (Video Duration (seconds) ) * (fps) faces.

### Built With

- Python `3.6` 
    - face_recognition `1.3.0`
    - opencv-python `4.2.0.32`
    
# Getting Started

My CPU had 12 cores so I ran 10 processes simultaneously using `multiprocessing` however you could set the number of process by changing the value of SEGMENT

### Prerequisites

install pipenv
```
pip3 install pipenv
```

### Installation

1. clone this repo
   
    ```
    git clone https://github.com/hajindvlp/Sebom.git
    cd Sebom
    ```
2. install packages
   
    ```
    pipenv install    
    ``` 
  
### Usage

1. Make required directories
    
   ```shell script
   mkdir videos
   mkdir faces 
    ```
2. Put a video that has faces
3. Run the program
    
   ```shell script
   pipenv shell
   python3 main.py
    ``` 
   
# Acknowledgements

- [Ageitgey's Face Recognition](https://github.com/ageitgey/face_recognition)