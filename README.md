# Kidcom_v2
Website : https://kidcomm-v2.onrender.com

**Description**   
&nbsp;Kids today are lost with cartoons, TV and animated shows, which reduces their reading time to almost zero. Kidcomm aims to make the activity of reading books exciting for kids. As kids read the digital book, his/her speech is recognized and the next page of the story loads up if the kid reads that page properly. Also, the performance of the kid is tracked and analysis charts are presented for the parents to help their children learn language better. Words that the kid found difficult to pronounce or read out are also tracked and presented at the end for practice.  
&nbsp;Going forward, we want to make Kidcomm a digital version of "Shakka Lakka Boom-Boom", by making stories come to life with animated movements, sounds and music.

**Working**  
1. Story lines and Story Images are stored in Google Firebase
2. Getting Speech transcript using Javascript's "Web-to-Speech API"
3. Using Fetch API to send Speech Transcript data to server and compare it with original Story lines
4. If Story line and Speech Transcript data is matched, then Story Image link is sent to the frontend, where it gets displayed
5. For each line: "Accuracy", "Speed(words/min)", "Time(taken/line)" is calculated and once the story is done, the average of these values are updated into Real-time database of Firebase
6. Finally the scores are displayed and difficult words are put on screen
7. Pressing the Analysis button, finally opens up the "Performance charts"

**Updations**
1. Speech Recogonation Updated
2. Sounds Effect add on
3. Images to Video add on
4. Multiple Session add on

