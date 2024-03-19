# Longshot Challenge

---

## Summary

This challenge seems to  involve [web scraping](https://en.wikipedia.org/wiki/Web_scraping), [automation](https://en.wikipedia.org/wiki/Automation), and [reverse engineering](https://en.wikipedia.org/wiki/Reverse_engineering). The goal is to get the final "passcode" to defeat the challenge, with a seemingly simple target website.

---

## Defeating This Challenge

### Examination:
The first thing I did was to examine the target website. I found out that first goal enter the 8 digits and your name to a specified text-fields below as quick as possible to the said digits. Entering it manually seems to impossible as you will need for the digits to appear one after another, not to mention that the specified fields will only appear after all the digits are shown. The timer starts as soon the page is loaded to the browser, not as the digits and text-fields are shown.

### Solution:

I've written a simple python script that will scrape the target website using selenium and Chrome web browser.

As we are dealing with time and Selenium by default only interacts with visible elements in a webpage, and I've also taken note that the numbers are already on the page's source. I decided to use the Selenium webdriver's `execute_script` function. This will enable me to get all the digits directly from the page source using a JavaScript script. I've also used this function to input the digits and my name directly to page source and called the `submit()` JS function of the page to submit the data for the next step.

On the next page, at first I was confused that the page only display a blank white page. I decided to go into the console log and found an error with websocket connection on page with the url https://challenge.longshotsystems.co.uk/ok. I noticed that the error is 401, meaning that the error is session related. I've also taken note the previous page before https://challenge.longshotsystems.co.uk/ok, has a 3-second redirect rule applied on the meta tag. I've concluded that the session will only be active about 3 seconds.

With this fact, I've used `execute_script` again to instantly redirect the page directly to `https://challenge.longshotsystems.co.uk/ok` and when I checked the console logs on the page, alas log results. This is my expected outcome because I've already taken note of the websocket script within the page.

I've noted that logs seems to be a bunch of encoded strings, but when I noticed that some ends with `==` which is common when encoding Base64 strings. I've decoded the first log and when decoded it says:

> "Implement a machine with instructions ADD, MOV, STORE and 16 integer registers.
> 
> Examples:
> 
>"ADD 500 R5 R10" adds 500 to register 5 and puts it in register 10. R5 is unchanged and R10 is updated to 500+R5.
> 
> "MOV R10 R11" copies the contents of reg 10 to reg 11.
> 
> "STORE 500 R0" writes 500 to register 0.
> 
> Execute the program that follows, sum the registers, encode that result in the same way as these instructions are encoded and send it back up the websocket. If you are correct you will get a response."

With these instructions, I've created a simple Python script that will do just that.

1. It will process all the ADD, MOV, and STORE commands.
2. Stores integers on "registers"
3. Gets the sum of all "registers"
4. Encodes the sum back to Base64
5. Sends the encoded string it via webdriver's `execute_script` to preserve session
6. Console log the websocket response
7. Then the script gets the log from browser, decodes it and prints it on the standard/console output.

And this is what I got (hash will change every time you ran the script):

`"Correct! Send the following hash along with your name to Longshot: 2f8d0795564bc8b3242c4df8686fe9745930a74ca29b3f90dcda645aaca6428f"`