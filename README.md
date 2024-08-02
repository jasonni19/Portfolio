# Website Energy Usage and Carbon Emission Calculator
#### Video Demo: https://www.youtube.com/watch?v=GPUbaGSCrOQ&t=8s

#### Description:
During the development of this program, I utilized the Website Carbon API. Libaries I imported included plotext, requests, validator_collection and pytest.

I programmed a Website Energy Usage and Carbon Emission Calculator. The purpose of the Website Energy Usage calculator is to spread awareness of the impact that websites can have on energy usage and carbon emissions on each pageload. This is done by allowing users to input the url of a website of their choice, and the program returns the statistics for energy usage, carbon emissions, and more. The program also creates the visual representation of a bar graph to represent the statistics for energy usage and carbon emissions.

To begin, in my main function, I utilize a count variable in order to limit the number of websites that the user can input to 2. I made this design choice in order to prevent the user from send too many requests to the API (flooding it). If too many requests are sent to the API at once, it will temporarily shut down. The main function then prompts the user for url to a website. This is stored in the variable url and passed to the validateInput function.

The purpose of the validateInput function is to check whether the user's input is a valid url. This is made possible by a function from the validator_collection library: validators.url(). If this function does not throw a ValueError exception, it means the user inputted a valid url. That url is then returned. However, if it does throw a ValueError exception, valideatInput returns 0 and the user is prompted to input another url. The user may also input "s" or "S" to stop them from being prompted to enter a url. If they do this without having entered any valid websites prior, the program exits with no data outputted.

Next, if the user inputted a valid url, the url will be passed into the website function. The purpose of the website function is to simply return the name of a website from its url. For example, if "https://youtube.com" were to be passed into website, "youtube" would be returned. In order to accomplish this, regex is used. If the regex condition is passed, the website name is extracted using matches.group and returned.

Next, the function processUrl is called with a website name as its parameter. processUrl is the source of the statistics. To begin, it makes an http get request to the Website Carbon API. It then turns the API response to a dictionary using response.json(). Next, it parses the dictionary to check whether the website uses green hosting, provde the carbon emission rating, and cleanliness compared to other websites. If no KeyError exceptions are thrown during this process, a match statement is used to print different emojis based on the carbon emission rating. Finally, it appends energy usage data to the global array called energy, carbon emission data to the global array called carbon, and the name of the website to the global array called nameList. These global arrays will be used in the graph function.

In processUrl, if a KeyError exception is thrown, this usually means that the user inputted a valid url that did not lead to an accessible website. Thus, it is not found in the Website Carbon API. In this case, the user is prompted to enter another url. There's also the rare case that the KeyError exception is a result of the API being temporarily down.

Finally, the graph function may be called if the user input passes the prior functions successfuly. First, in the main function, the user is prompted on what graph they want to view: energy, carbon, or both. If they input something else, they are prompted again. Their answer is then passed into the graph function. If the user inputted "e" or "E", the energy graph is outputted which is made possible by functions of the plotext library. This process is the same for the carbon graph. The graph function can also output both the energy and carbon graph if the user chooses that option.


