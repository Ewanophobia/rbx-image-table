# rbx-image-table

  

A simple utility for converting any image into a Lua 2D array, designed for Roblox.
**VERY BODGED TOGETHER!**

An example table would be like the following
```lua
return {
	[1] = {
		[1] = Color3.new(0.25, 0.5, 1),
		[1] = Color3.new(0.25, 0.5, 1),
		...
	}
	...
}
```

Where the first array corresponds to the x-axis of the image, and the next nested array corresponds to the y-axis of the image

My motivation behind this was to be able to cache bitmaps into Roblox, as a performance optimisation technique (as it means the CPU will not die trying to decode a PNG buffer using MaximumADHDs PNG library). If we can cache large 16k level images (such as the textures I'm using for my game), it means we don't have to repeatedly request a domain for a PNG buffer, which is great when you are working for mobile!

# usage

- compile the project
- execute the binary and select an image
- wait
- file will save to a path of your choosing
  

### attributions:

SLPP - https://github.com/SirAnthony/slpp