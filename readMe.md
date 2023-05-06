# Palmprint contactless for biometric purpose 


### Contributors 
- _Anirudh Sathish_ 
- _K Hitesh Gupta_

### Databases
- Birjand University Mobile Palmprint Database (BMPD)
- Tongji Contactless Palmprint Dataset
###### Description 
- Birjand University Mobile Palmprint Database (BMPD) :-
```
1.Birjand University Mobile Palmprint Database (BMPD), contains 1640 images from both the left and right hands of 41 Iranian females in two sessions with the interval of two weeks.
2.In the first session, the users were requested to put their hand on a black background and six images of each palm were taken from the distance of 20 cm of the user hand in a free environment.
3.Although the hand orientation was not controlled during the image capturing, there are not much hand pose variations in images.
4.In the second session, 16 images were taken per each user’s palm like the first session but the user’s hands have more rotation in comparison to the first session.
5. It should be noted that the users were asked to close and open
their hands after each image capturing to increase the intraclass variability among palmprint images.
```
- Tongji Contactless Palmprint Dataset:-
```
1. The Tongji Contactless Palmprint Dataset is a large-scale dataset of contactless palmprint images.
2. It was collected using a novel contactless palmprint acquisition device developed by the researchers.
3. The device includes a CCD camera, a lens, a ring white LED light source, a power regulator for the light source, an industrial computer, and a thin LCD with a touch screen.
4. The device is user-friendly and comfortable to use, with real-time video stream display to guide the user in adjusting their hand pose.
5. The collected images are of high quality, with high contrast and signal-to-noise ratio, and a simple dark background.
6. The dataset contains 12,000 images captured from 600 different palms of 300 volunteers, including 192 males and 108 females.
7. The dataset was collected in two sessions with an average time interval of about 61 days between them.
8. The dataset can be used for research on contactless palmprint recognition and related applications.
```
- Currently all tasks are being run on these.

### Progress 
- Till now we have implemented a CNN to perform classification task on the above database
- CNN when run on the complete image without ROI , gave an accuracy of 64.68% , when run for 3 epochs . Suspected overfitting - 06:00 pm IST - 23/04/23
- CNN when run on the complete image without ROI , gave an accuracy of 77.33% , when run for 8 epochs using CUDA (MX350). - 09:00 pm IST - 23/04/23
- Applied Transfer Learning i.e , used Resnet18 by modifying only the final layer(TL1) , when run on the complete image without ROI , gave an accuracy of 76.39% , when run for 3 epochs using CPU - 05:45 pm IST - 25/04/23
- Applied Transfer Learning i.e , used Resnet18 by modifying only the final layer (TL2), when run on the complete image without ROI , gave an accuracy of 81.05% , when run for 3 epochs using CPU - 10:00 pm IST - 25/04/23
- Applied Transfer Learning i.e , used Resnet18 by modifying only the final layer(TL1) , when run on the complete image without ROI , gave an accuracy of 81.67% , when run for 8 epochs using CUDA (MX350) - 10:15 pm IST - 25/04/23
- Applied Transfer Learning i.e , used Resnet18 by modifying only the final layer(TL1) , when run on the complete image without ROI , gave an accuracy of 97.2% , when run for 20 epochs using CUDA (MX350) - 06:45 am IST - 26/04/23
- CNN when run on the complete image with ROI , gave an accuracy of 89.83% , when run for 6 epochs using CUDA (MX350). - 09:00 am IST - 26/04/23
- Applied the DINOv2 model on the complete image with ROI, gave a test accuracy of 98% and validation accuracy of 98% - 10:00 pm IST - 05/05/23


### Citations 
- **Izadpanahkakhk M, Razavi SM, Taghipour-Gorjikolaie M, Zahiri SH, Uncini A.** Novel mobile palmprint databases for biometric authentication. International Journal of Grid and Utility Computing. 2019;10(5):465-74.
