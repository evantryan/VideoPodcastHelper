# VideoPodcastEditHelper

An addon to make editing a 2 person video podcast easier in VSE

## about
---

This addon aims to make editing a a very specific type of video podcast easier. The assumption is that there are two video sources. One from each participant. At a high level, the editing would consist of removing chunks of time you don't want and then switching between person A, person B, and a split screen.

This addon adds a keyable attribute to each sequence strip. Options include ignore, a, b, and c. It also employs app handlers to switch between angles/setups on every frame update.

## why
---

I noticed there's no concept of 'instancing' in VSE. this means any time a cut is made on a meta strip, everything inside the newly created strip is now a completely new strip/object. This means that adjustments made like color corrections, masks, repos, etc made to the original footage inside one meta, doesn't propagate to the 'same' original footage inside all the other meta strips. One would have to copy all of these changes every time to get the footage to match. 

This sidesteps the issue altogether by having all possible setups inside one master meta strip. So, instead of traditionally cutting between setups, switching is done via animating the `mode` property on the master meta strip.
## workflow
---

Recommended workflow is as follows.

1. import source videos and corresponding takes
2. set proxy percentage to 25%
3. ensure audio sync is as you like it
4. add any wanted color correction 
5. add repo/scale to video strips as needed
6. group/meta existing strips
7. go into meta strip and setup the split screen angle (using `Transform` strips with mask modifiers)
8. set any strips that make the split screen to 'c'
9. set any strips that make person A to 'a'
10. set any strips that make person B to 'b'
11. exit the meta strip
12. ensure that switching setups is working by changing the `Podcast Helper` mode dropdown between a, b and c
13. edit the meta strip for time
14. key/animate mode dropdown for angle/setup
15. edit internal audio strips directly for audio changes

## development
---

to run the code directly. execute the following in blender

    import sys
    sys.path.insert(0, '/path/to/parent/directory')
    import VideoPodcastEditHelper
    VideoPodcastEditHelper.register()


## moving forward

Options in the dropdown should probably be user named/definable in some way. Ignore would be the only required attribute. This would make it easier to have more than just the (at the moment) three possible setups.