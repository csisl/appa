# appa

![alt text](https://github.com/stncal/appa/blob/master/avatar_appa.png)

Appa is an educational steganography tool aimed at teaching the user how steganography works by outputting changes made to an image as binary data is injected into it. This was completed at UTSA's 2019 RowdyHacks.

### prereqs

[Pillow](https://pillow.readthedocs.io/en/stable/)

`pip3 install Pillow`

### usage 

`python3 appa.py [-h] [-d] [-e message] image`

## how it works 

### encoding 

Appa takes in an image and some text and injects the text into the image by modifying the individual pixels. 

Pixels are arranged something like this:

`[(86, 127, 179), (87, 128, 179), (90, 132, 182), (92, 135, 185), (96, 137, 188)]`

To inject some text into the image, we want to get the 8-bit binary representation of each letter in the string we want to include. Say for example we want to put the letter "A" into an image. If it had the above pixel layout, this would be the process: 

1. First convert A to binary (`01000001`)
2. For every bit, we want to modify a pixel. If the bit is 0, we make it even, if the bit is 1, we make it odd, both by subtracting 1 from that specific pixel. 
3. At the end of the 8 bit letter, we set the last value in the pixel array to an even number if we want to keep encoding and an odd number if the encoding is complete. 

So if our image had the following arrangement for the first 3 pixels

[(86, 127, **179**), (**87**, 128, **179**), (90, **132**, **182**)]

we could inject "A" by changing the things in bold by subtracting 1 from it. Notice letters are 8 bit, but we are dealing with every 9 values for the pixel. Recall that the last bit is set to via the step 3 from above.

You can map the bits from A to the pixels as follows:

![alt text](https://github.com/stncal/appa/blob/master/encoding.jpg)

### decoding 

Decoding should now be pretty trivial. If we look at the steps above we can possibly extract some text by reversing the algorithm. Appa reads up to the first 9th value in a set of pixels that is odd and then begins to attempt decoding. It will figure out what binary data is represented by these pixels by knowing all even numbers represent a 0 and all odd numbers represent a 1, then translating that to it's correct ASCII value. 


### before & after

Here's an image before encoding:

![alt text](https://github.com/stncal/appa/blob/master/flying_appa.png)

This image has around 83,000 pixels. After modifying about 81,000 of those pixels to inject 27,000 letters into the image, this is what the image looks like:

![alt text](https://github.com/stncal/appa/blob/master/flying_appa_new.png)

