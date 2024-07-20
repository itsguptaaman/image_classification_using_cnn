### Clone the repo
```
git clone https://github.com/itsguptaaman/image_classification_using_cnn
```

### go inside the dir
```
cd image_classification_using_cnn 
```
### Create a conda environment
```
conda create -n task python=3.8 -y
```

### Activate the environment
```
conda activate task
```

### Install the Requirements file
```
pip install -r requiremnts.txt
```

### To start the flask server 
```
uvicorn main:app --reload
```