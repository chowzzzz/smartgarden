# smartgarden
Smart Garden - IoT Project

The smart garden monitors the temperature,humidity, light levels and soil moisture of the plant. It has an automated system that waters the plant when the soil is too dry and switches on the light when it is too dark. This maintains an ideal and consistent soil condition for the plant, and makes it convenient for those who tend to forget to water their plants regularly. Also, the plant can continuously photosynthesize even when there is no sunlight.

We will be using an Arduino and a Raspberry Pi to receive data from the sensors and control the different actuators. The surrounding temperature, air humidity and brightness values will be recorded, as well as the soil moisture levels. These values will then be displayed on the LCD screen, which allow users to know the environmental conditions of the plants when they check on them.

When the soil moisture level goes above 500 (for our soil moisture sensor, the higher it is the drier the soil), the red LED will light up as a warning to show that the plant needs water. Also the water pump will start to run and pump water into the soil automatically. This is very convenient for users as they do not need to water their plants every time but instead let the system water their plants automatically based on the moisture level of the soil.

As for the automated light, when the LDR records a value higher than 300, the yellow LED will light up and act like the sun, to allow continuous photosynthesis to occur for the plants.

The temperature, humidity, light levels and soil moisture values will also be published to DynamoDB. Through a server (Raspberry Pi), the data will be displayed onto a flask web page where it shows real-time data coming from the sensors. This will allow users to view the real-time environmental conditions of the plants on the go (the latest 15 records through a graph).

The web page will also allow users to control the water pump and decide whether they wish to water the plants automatically or manually. They can turn on or off the water pump whenever they wish to, thus making it very convenient if users wish to water their plants even when they are not around.
