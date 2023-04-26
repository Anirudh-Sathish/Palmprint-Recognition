# Palmprint contactless for biometric purpose 


### Contributors 
- _Anirudh Sathish_ 
- _K Hitesh Gupta_

### Database 
- Birjland university db
###### Description 
```
Birjand University Mobile Palmprint Database (BMPD), contains 1640 images from both the left and right hands of 41 Iranian females in two sessions with the interval of two weeks. In the first session, the users were requested to put their hand on a black background and six images of each palm were taken from the distance of 20 cm of the user hand in a free environment. Although the hand orientation was not controlled during the image capturing, there are not much hand pose variations in images. In the second session, 16 images were taken per each user’s palm like the first session but the user’s hands
have more rotation in comparison to the first session. It should be noted that the users were asked to close and open
their hands after each image capturing to increase the intraclass variability among palmprint images.
```
- Currently all tasks are being run on this 

### Progress 
- Till now we have implemented a CNN to perform classification task on the above database
- CNN when run on the complete image without ROI , gave an accuracy of 64.68% , when run for 3 epochs . Suspected overfitting - 06:00 pm IST - 23/04/23
- CNN when run on the complete image without ROI , gave an accuracy of 77.33% , when run for 8 epochs using CUDA (MX350). - 09:00 pm IST - 23/04/23
- Applied Transfer Learning i.e , used Resnet18 by modifying only the final layer(TL1) , when run on the complete image without ROI , gave an accuracy of 76.39% , when run for 3 epochs using CPU - 05:45 pm IST - 25/04/23
- Applied Transfer Learning i.e , used Resnet18 by modifying only the final layer (TL2), when run on the complete image without ROI , gave an accuracy of 81.05% , when run for 3 epochs using CPU - 10:00 pm IST - 25/04/23
- Applied Transfer Learning i.e , used Resnet18 by modifying only the final layer(TL1) , when run on the complete image without ROI , gave an accuracy of 81.67% , when run for 8 epochs using CUDA (MX350) - 10:15 pm IST - 25/04/23
- Applied Transfer Learning i.e , used Resnet18 by modifying only the final layer(TL1) , when run on the complete image without ROI , gave an accuracy of 97.2% , when run for 20 epochs using CUDA (MX350) - 06:45 am IST - 26/04/23


### Citations 
- **Izadpanahkakhk M, Razavi SM, Taghipour-Gorjikolaie M, Zahiri SH, Uncini A.** Novel mobile palmprint databases for biometric authentication. International Journal of Grid and Utility Computing. 2019;10(5):465-74.