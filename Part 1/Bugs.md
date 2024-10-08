# Part 1

## Part 1

1. [Calendar](https://clubs.iiit.ac.in/calendar) ([Issue image](https://i.imgur.com/hR13SLn.png))- There is no support for recurring events as can be seen for Trivia Tuesday. The event itself is only on Tuesdays, but because there is no option to set recurring events, one can either set it for every Tuesday manually or set a long time limit event. Ideally, this should not be the case. A potential fix could be to make a *periodic* (weekly?) function that adds these events to the database.

2. [Gallery](https://clubs.iiit.ac.in/gallery) ([Issue video](https://i.imgur.com/MHsXa5B.mp4)) - Opening the gallery while non-cached (Ctrl+F5), the images jump around while loading, even when one image loads, it does not load in it's correct place/placeholder as it should. Potential Fix - Image placeholders have their [height/width parameters as set to 0](https://i.imgur.com/zNlN4Kz.png), changing this to desired size before dynamic loading can fix this.

3. [List of Events](https://clubs.iiit.ac.in/events) ([Issue image](https://i.imgur.com/q77B32W.png )) - Half the posters are just blurry even when their source images are a good resolution. Some googling led me to find out that [next.js has an image optimisation option](https://nextjs.org/docs/pages/building-your-application/optimizing/images) which could be the culprit behind this. Maybe [this github issue](https://github.com/vercel/next.js/issues/53329) is related to it, there are some workarounds given which could work.

4. Can't find more, website is too good :p