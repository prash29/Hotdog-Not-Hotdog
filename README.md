# Hotdog-Not-Hotdog
Personal implementation of HBO Silicon Valley's app Not Hotdog ( Identifies if a given picture is a Hotdog or not )
 
 I have used Google's Inception model (2015) . Inception-v3 is trained for the ImageNet Large Visual Recognition Challenge using the data from 2012. The model classifies images to about 1000 classes.
 The retraining is done by replacing last layer of this model. Training has been done with 450 pictures. Thus, accuracy for a certain images might be low. Better the dataset, better the result.
 
 **Prerequisites**
  * Need to have Python and Tensorflow installed on the system.
  
  
 **Steps**
 * Clone the repository.
 * Open a terminal and run the following commmand on any of the images in the Test images folder or any other image of your choice.
    python label.py Test\ images/jianyang.jpeg
    * E.g. 1
    
    ![1. Jianyang](https://github.com/prash29/Hotdog-Not-Hotdog/blob/master/Test%20images/jianyang.jpeg)
   
   
   
   
   * *(Wait for the prediction)
    **Result**
    * not hotdog  =  0.98556
    * hotdog  =  0.01444
   
   
 * E.g. 2
   * To check on another image, run this : 
     python label.py Test\ images/hotdog1.jpeg
   
   
   ![2. Hotdog](https://github.com/prash29/Hotdog-Not-Hotdog/blob/master/Test%20images/hotdog1.jpeg)
   
   *  *(Wait for the prediction)
   
   
    **Result**
    * hotdog  =  0.99714
    * not hotdog  =  0.00286
    
