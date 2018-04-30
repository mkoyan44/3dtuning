# 3dtuning

In order to run selenume with remote stand alone server, it is requred to download:
javaJDK:http://download.oracle.com/otn-pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-macosx-x64.dmg?AuthParam=1525098850_701e685fdeda558385d8fae50f99d9ee
chromeWebDriver:https://chromedriver.storage.googleapis.com/2.38/chromedriver_mac64.zip,
selenumeServer:https://selenium-release.storage.googleapis.com/3.11/selenium-server-standalone-3.11.0.jar

1) make sure chrome webdriver in the same folder as the google chrome itself, and the executable path included in path system variable.
2) run server with java -jar ~/Downloads/selenium-server-standalone-3.11.0.jar &
3) get the server ip address and replace the it in auto_exec.shå bash 

