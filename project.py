from validator_collection import validators
import plotext
import requests
import re
import sys

carbon = []
energy = []
nameList = []

def main():
    count = 1
    graphResponse = None

    print(r"""
    ,-:` \;',`'-,
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.""")

    print("\n", end = "")
    print("Welcome to the Website Energy Usage and Carbon Emission Calculator!\U0001F30E")
    print("You may input 1-2 websites to view their energy usage or carbon emissions.")

    while(count < 3):
        print("----------------------------------------------------------------------------------------------------------------------------")
        print(f"Website #{str(count)}:")
        print("Enter a website url to view its carbon emissions and energy statistics. INCLUDE https:// or http://, ex. https://youtube.com. Enter S to stop.")
        url = input()
        print("This may take a few seconds...")

        if validateInput(url) == 0:
            continue

        validUrl = validateInput(url)

        if (validUrl == "s" or validUrl == "S"):
            break

        websiteName = website(validUrl)
        count-=processUrl(websiteName)

        count+=1

    if len(nameList) == 0:
        sys.exit("You inputted no websites.\U0001F972")

    valid_responses = {"e", "E", "c", "C", "b", "B"}
    while graphResponse not in valid_responses:
        print("----------------------------------------------------------------------------------------------------------------------------")
        graphResponse = input("Would you like to view the Energy Usage or Carbon Emission Graph for the websites you inputted? Enter e for Energy, c for Carbon, and b for both.")

    graph(graphResponse)


def processUrl(websiteName):
    try:
        response = requests.get("https://api.websitecarbon.com/site?url=https%3A%2F%2Fwww."+websiteName+"%2F")
        o = response.json()

        print("\n", end="")
        print("SOME FACTS:")
        if o['green'] == True:
            print(f"{websiteName.capitalize()} uses green hosting which uses less electricity and produces less CO2 emissions than other types of web hosting!\U0001F333")
        else:
            print(f"{websiteName.capitalize()} does not use green hosting.\U0001FAB5")

        print(f"{websiteName.capitalize()}'s carbon emission rating on a scale of A+ to F is {o['rating']}")
        print(f"{websiteName.capitalize()} is about {round(o['cleanerThan'] * 100)}% cleaner than other websites")

        match o['rating']:
            case "A+"|"A"|"A-":
                print("\U0001F606")
            case "B+"|"B"|"B-":
                print("\U0001f600")
            case "C+"|"C"|"C-":
                print("\U0001F610")
            case "D+"|"D"|"D-":
                print("\U0001F612")
            case "E+"|"E"|"E-":
                print("\U0001F637")
            case "F":
                print("\U0001F480")

        global energy
        energy.append(o["statistics"]["energy"] * 100)

        global carbon
        carbon.append(o["statistics"]["co2"]["grid"]["grams"])

        global nameList
        nameList.append(websiteName.capitalize())
        return 0

    except KeyError:
        if ('error' in o):
            sys.exit("The API is temporarily unavailable, try again later.")
        else:
            print("The url you inputted was not found in the database. Enter another URL.")
            return 1

def graph(letter):
    print("\n",end="")
    plotext.plotsize(70, 30)
    if (letter == "e" or letter == "E"):
        plotext.title("Energy Consumption of Websites")
        plotext.ylabel("Energy Consumption (W)")
        plotext.bar(nameList,energy)
        plotext.show()

        for i in range(len(nameList)):
            print(f"{nameList[i]}: {energy[i]} watts")

        return "Energy Graph"

    elif (letter == "c" or letter == "C"):
       plotext.title("Carbon Emissions of Websites")
       plotext.ylabel("Carbon Emissions (Grams)")
       plotext.bar(nameList,carbon)
       plotext.show()

       for i in range(len(nameList)):
            print(f"{nameList[i]}: {carbon[i]} grams")

       return "Carbon Graph"

    else:
        plotext.title("Energy Consumption of Websites")
        plotext.ylabel("Energy Consumption (W)")
        plotext.bar(nameList,energy)
        plotext.show()
        plotext.cld() # clear the previous graph data

        plotext.title("Carbon Emissions of Websites")
        plotext.ylabel("Carbon Emissions (Grams)")
        plotext.bar(nameList,carbon)
        plotext.show()

        for i in range(len(nameList)):
            print(f"{nameList[i]}: {carbon[i]} grams, {energy[i]} watts")
        return "Both Graphs"

def validateInput(url):
        try:
            if (url == "s" or url == "S"):
                return url
            validators.url(url)
            return url

        except ValueError:
            print("Not a valid URL, try again.")
            return 0


def website(url):
    if matches := re.search(r"^(?:https://|http://)(?:www\.)?(\w+\.\w+).?$",url):
            website = matches.group(1)
            return website

if __name__=="__main__":
    main()
