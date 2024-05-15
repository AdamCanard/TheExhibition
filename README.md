<h2>Running The Game (Build)</h2>

Download Ren'Py<br />
https://www.renpy.org/latest.html<br />

Run renpy-8.2.1-sdk.7z <br />
Extract to Desktop (Or another folder you can access easily) <br />

Open extracted folder, Run renpy.exe <br />
Navigate to the bottom right of the screen and hit preferences <br />
Change Projects Directory to a new folder on your Desktop <br />

Download The Exhibition project as ZIP <br />
Extract TheExhibition-main to the new Project Directory folder <br />

From the Ren'Py main menu, hit refresh and select "The Exhibition" <br />
Click Launch Project <br />

<h2>Prefered Script Structure</h2>
<h5>(This is just a guideline, dont worry about following it perfectly)</h5>

If you would like any special features to your script<br />
Please just write a description of what you want to happen in between lines of dialogue and I will do my best to replicate it in the game<br />

<h3>List the characters of the scene and the different assets for each character</h3>
List of Characters: <br />
<ul>
<b>Guide</b>
    <li>Guide Happy</li>
    <li>Guide Sad</li>
    <li>Guide Angry</li>
  <br />
<b>Character</b>
  <li>Character Happy</li>
  <li>Character Sad</li>
  <li>Character Angry</li>
</ul>

<h3>List the backgrounds of the scene</h3>
List of Backgrounds <br />
<ul>
<li>Inside</li>
<li>Outside</li>
</ul>

<h3>Example script</h3>

Scene Start (this signifies the start of a scene)

BG Black (screen starts black)<br />

Narrator "Welcome to the example script"<br />
Narrator "Every new line is another click from the user to continue"<br />
Narrator "So"<br />
Narrator "This"<br />
Narrator "Takes"<br />
Narrator "Five"<br />
Narrator "Clicks"<br />
Narrator "Lets change our background"<br />

BG Outside<br />

Narrator "We are now Outside"<br />
Narrator "Walk inside and meet your guide"<br />

BG Inside<br />

Narrator "We are now inside"<br />
Narrator "Look your guide is about to come on screen"<br />

Show Guide<br />

Guide "This is now the guide talking. With default expression"<br />
Guide Happy "This line will be displayed with my happy sprite"<br />
Guide Angry "This line will be displayed with my angry sprite"<br />
Guide "What do you think Character"<br />

Chose: (when the character makes a decision it will switch to a new scene based on the character choice) <br />
Character "Sounds great!"<br />
&nbsp;&nbsp;&nbsp;&nbsp;Scene Great<br />
Character "Im Confused"<br />
&nbsp;&nbsp;&nbsp;&nbsp;Scene Confused<br />
Character "Placeholder Text"<br />
&nbsp;&nbsp;&nbsp;&nbsp;Scene Placeholder Scene<br />

Scene Great:<br />

BG Black (screen starts black)<br />
Narrator "You chose the first option"<br />

Scene Confused:<br />

BG Black (screen starts black)<br />
Narrator "You chose the second option"<br />

Scene Placeholder Scene:<br />

BG Black (screen starts black)<br />
Narrator "Placeholder response"<br />
