# Part 1

## Part 

> Try finding atleast 5 technical/UI-UX issues you feel in the clubs or life website. (Not to give things like "I don't like the color of the website" or "I don't like the font of the website" as they are subjective and not technical/UI-UX issues). Write how can you solve them/potential solutions.

1. [Calendar](https://clubs.iiit.ac.in/calendar) ([Issue image](https://i.imgur.com/hR13SLn.png))- There is no support for recurring events as can be seen for Trivia Tuesday. The event itself is only on Tuesdays, but because there is no option to set recurring events, one can either set it for every Tuesday manually or set a long time limit event. Ideally, this should not be the case. <br> 
Potential Fix - Make a *periodic* (weekly?) function that adds these events to the database.

2. [Gallery](https://clubs.iiit.ac.in/gallery) ([Issue video](https://i.imgur.com/MHsXa5B.mp4)) - Opening the gallery while non-cached (Ctrl+F5), the images jump around while loading, even when one image loads, it does not load in it's correct place/placeholder as it should. <br>
Potential Fix - Image placeholders have their [height/width parameters set to 0](https://i.imgur.com/zNlN4Kz.png), changing this to desired size before dynamic loading can fix this.

3. [List of Events](https://clubs.iiit.ac.in/events) ([Issue image](https://i.imgur.com/q77B32W.png )) - Half the posters are just blurry even when their source images are a good resolution. <br>
Potential Fix - Some googling led me to find out that [next.js has an image optimisation option](https://nextjs.org/docs/pages/building-your-application/optimizing/images) which could be the culprit behind this. Maybe [this github issue](https://github.com/vercel/next.js/issues/53329) is related to it, there are some workarounds given which could work.

4. Can't find more, website is too good :p

## Part 2

> Go through the codebase of Clubs Council Website, and try to explain that how, in your opinion, the whole structure works. How there are different components, how they interact with each other, etc. (In a very basic way, you don't need to go into the details of the codebase)