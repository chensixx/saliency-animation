# Saliency-Aware Animation
Si Chen, William Zhang, Michael Behrisch, Remco Chang
June-August ongoing 2019

## Abstract

Visualization animation are often used show time elapsed data. But the speed of how data changes can make it difficult for the audience to grasp all the information at the same time. Sometimes the animation goes too fast and both the audience and presenter can feel overwhelmed . Or there is a big leap from the current frame to the next that we can’t process quickly enough. In this project, we want to build a tool that changes speed of the animation according to how much information is on the screen and how overwhelming the audience feels.­­­We will incorporate data with a saliency map model and then measure how much a data cluster change from frame to frame. Our tool is beneficial for both audience and presenters to get the message across without tiring out everyone. It will change the way people communicate with web animation from now on.

## Set up
If you just want to see the sample running, In terminal, go to "web/" folder, type in 

	"python -m SimpleHTTPServer 1337"

Done

To start from scratch, follow these steps

Step 1: set up the saliency model with instructions here: https://github.com/marcellacornia/sam. Fulfill all requirements.
Good luck!
Make sure it works.

Step 2: Download all files. Open web/index.html, uncomment line 470:
	saveSvgAsPng(document.getElementById("vis"), year(t)+"diagram.png");
and uncomment line 431: .ease("linear") , then comment line 430, save;
//give purpose

Step 3: In terminal, go to "web/" folder, type in 
	python -m SimpleHTTPServer 1337
Then in your browser type in "http://localhost:1337/index.html". When you run this, it will start downloading 137 frames of the animation.
Go to your download folder and copy these frames to a folder with any name you like, mine is called "screenshots/". Move the folder to your saliency model folder 

Step 4: In terminal, go to your saliency folder run 
	python main.py test screenshots/ 
In about 20 minutes, all the saliency maps will be in folder "predictions/"
Then run 
	python img.py 
now you will get an array of numbers. they are motion magnitude of the change between every frame. If you want difference between every n frames just change line 20 into range(n,size,n) and line 21 into [x-5] line 22 to [x].
I already have all the motion magnitude arrays in index.html from line 221.

Step 5: Now comment line 470 and 431, uncomment line 430, save; refresh your page on browser now it will run in the custom speed.
//give purpose

Step 6: On the page, in the input box, type in a number and hit submit to see different speed according to the lookback parameter. For example, "5" means custom speed was built upon differences between every 5 frames. 

Scroll down to see the speed. Blue line is custom, orange is constant speed. When blue is above orange, means faster, vice versa.


## Sample pictures
![table](TABLE.png)

## Evaluation Design

See powerpoint from above



