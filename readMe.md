# Palmprint contactless for biometric purpose 


### Contributors 
- _Anirudh Sathish_ 
- _K Hitesh Gupta_

### Database 
- Birjland university db 
- Currently all tasks are being run on this 

### Progress 
- Till now we have implemented a CNN to perform classification task on the above database
- CNN when run on the complete image without ROI , gave an accuracy of 64.68% , when run for 3 epochs . Suspected overfitting - 06:00 pm IST - 23/04/23
- CNN when run on the complete image without ROI , gave an accuracy of 77.33% , when run for 8 epochs using CUDA (MX350). - 09:00 pm IST - 23/04/23
- Applied Transfer Learning i.e , used Resnet18 by modifying only the final layer , when run on the complete image without ROI , gave an accuracy of 76.39% , when run for 3 epochs using CPU - 05:45 pm IST - 25/04/23