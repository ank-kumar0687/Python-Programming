class Temperature:

    def convertFarenheit(self):
        self.celcius=float(input("Enter the celsius to convert  it into farenheit"))
        farenheit = (9/5)*self.celcius+32
        print(f"The farenheit of {self.celcius} is {farenheit}")

    def convertCelcius(self):
        self.farenheit=float(input("Enter the farenheit to convert it into celcius"))
        celcius=(9/5)*self.farenheit+32
        print(f"The celcius of {self.farenheit} is {celcius}")


obj=Temperature()
obj.convertFarenheit()
obj.convertCelcius()
