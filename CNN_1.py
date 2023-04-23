# CNN implementation 

# import libs
import os
import numpy as np 
import torch 
import glob 
import torch.nn as nn 
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torch.optim import Adam 
from torch.autograd import Variable
import torchvision 
import pathlib

# if cuda available 
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Transforms
transformer = transforms.Compose([
    transforms.Resize((150,150)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize([0.5 , 0.5 , 0.5 ],[0.5 , 0.5 , 0.5 ]),
])

# set directory paths 
base_dir = "basedata"
training = "training"
validationString = "validation"

# training ,validation locations 
training_path = os.path.join(base_dir,training)
test_path = os.path.join(base_dir,"testing")


# DataLoader 
train_loader = DataLoader(
    torchvision.datasets.ImageFolder(training_path , transform = transformer),
    batch_size = 12 , shuffle= True
)
test_loader = DataLoader(
    torchvision.datasets.ImageFolder(test_path , transform = transformer),
    batch_size = 12 , shuffle= True
)

# get class
classes = os.listdir(training_path)

# define the Neural Net 
class ConvNet(nn.Module):
    def __init__(self,num_classes = 41):
        super(ConvNet,self).__init__()

        self.conv1 = nn.Conv2d(in_channels= 3 , out_channels=12 , kernel_size= 3, stride = 1 , padding = 1)
         
        self.bn1 = nn.BatchNorm2d(num_features = 12)

        self.relu1 = nn.ReLU()

        self.pool = nn.MaxPool2d(kernel_size= 2)
        # 
        self.conv2 = nn.Conv2d(in_channels = 12 , out_channels=20 , kernel_size= 3 , stride=1 , padding= 1)

        self.relu2 = nn.ReLU()

        self.conv3 = nn.Conv2d(in_channels= 20 , out_channels= 32 , kernel_size = 3 , stride = 1 , padding = 1)

        self.bn3 = nn.BatchNorm2d(num_features = 32)

        self.relu3 = nn.ReLU()

        self.fc = nn.Linear(in_features= 32*150*150 , out_features= num_classes)
    
    def forward(self,input):
        output = self.conv1(input)
        output = self.bn1(output)
        output = self.relu1(output)
        output = self.conv2(output)
        output = self.relu2(output)

        output = self.conv3(output)
        output = self.bn3(output)
        output = self.relu3(output)
        # resizing 
        output  = output.view(-1,32*150*150)
        # print(output.shape)
        output = self.fc(output)
        return output
    

# Set HyperParameters 
num_epochs = 3 
batch_size = 4 
learning_rate = 0.001
# Tune this later based on performance 


# calculate testing_training , size 
train_count = len(glob.glob(training_path+'/**/*.JPG'))
test_count = len(glob.glob(test_path+'/**/*.JPG'))



# Set model 
model = ConvNet(num_classes=41).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters() , lr = learning_rate)

n_total_steps = len(train_loader)

for epoch in range(num_epochs):
    for i , (images,labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)


        # Forward pass 
        outputs = model(images)
        loss = criterion(outputs,labels)

        # Backward pass 
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


    # if (i+1) % 2 == 0:
    print('Epoch {} , Loss : {}'.format(epoch,loss.item())) 

print('Finished Training')


# For testing 
with torch.no_grad():
    n_correct = 0 
    n_samples = 0 
    n_class_correct = [0 for i in range(len(classes))]
    n_class_samples = [0 for i in range(len(classes))]

    for images,labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        _ , predicted = torch.max(outputs , 1)
        n_samples +=labels.size(0)
        n_correct += (predicted == labels).sum().item()

        for i in range(batch_size):
            label = labels[i]
            pred = predicted[i]

            if (label == pred):
                n_class_correct[label] +=1
            n_class_samples[label]+=1
    
    accuracy = 100.0* n_correct/n_samples 
    print('Accuracy  : {} % '.format(accuracy))

    for i in range(len(classes)):
        acc = 100*n_class_correct[i]/n_class_samples[i]
        print('Accuracy of {}  : {} %'.format(classes[i],acc))