# Kidcom_v4
Website : http://143.244.135.235:8036

**Note** :
The website is not secure yet. 
To enable microphone on your chrome browser;

1. Use "chrome://flags#unsafely-treat-insecure-origin-as-secure" to enable microphone support in chrome browser
2. Add "http://143.244.135.235:8036" in the box below
3. Press the "Relaunch" button in the right bottom corner

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

**Contributions**

**Raghul PK**
1. Creating the Frontend, UI and Drawings for Story application to display the story, keeping in mind the interests of the target users - "kids" (Animated and Colourful frontend)
2. Integrating Speech services with the app using Websockets and Deepgram speech API. Later, switched to JS Speech Recognition and Fetch API to achieve speech-to-text transcription
3. Integrating different parts of the Project

**Mahesh Kumar**
1. Database : Set up and managed the Google firebase for all storage needs;
     --> Real-time database : To store user performance data
     --> Storage : To store story images and story text
     --> Firestore database : For storing files as CSV
     --> Authentication
2. Connecting the Database with Flask backend for putting data when the user reads the story and retrieveing data when performance analysis charts has to be displayed.
3. Deployment of the web application on server
4. Creating the Landing page : Homepage

**Utkarsh Rajauria**
1. Performance Analysis : Using data collected from voice input like Accuracy, Speed(words/min), Time(time taken/line) to present analysis charts to understand the kid's language capability better
2. Designing charts and graphs that are user-friendly and easier to understand 
3. Creating the Frontend for Outputs and Performance analysis keeping in mind about our target users - "Parents" (Professional looking frontend)


