import requests, sys, os
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def __init__(self):
        MainWindow.setWindowTitle("Coronavirus cases")

        self.font_labels = QtGui.QFont()
        self.font_labels.setFamily("Calibri Light")
        self.font_labels.setPointSize(14)

        self.country = 'Worldwide'
        self.covidData = dict()

    def is_wifiActive(self):
        '''
        This function checks whether we have wifi or not.
        It returns True in the case we have wifi, otherwise, it returns a false
        '''

        try:
            requests.get('http://www.google.com')
            return True

        except:
            return False

    def bt_retryWifi(self):
        '''
        We enter to the main part of the application if the wifi is active
        '''

        if self.is_wifiActive():
            self.setupUi(MainWindow)
            self.refreshData()

    def setupWifiUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(380, 217)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lab_wifiError = QtWidgets.QLabel(self.centralwidget)
        self.lab_wifiError.setGeometry(QtCore.QRect(40, 0, 320, 111))
        self.lab_wifiError.setFont(self.font_labels)
        self.lab_wifiError.setWordWrap(True)
        self.lab_wifiError.setObjectName("lab_wifiError")
        self.lab_wifiError.setText("<html><head/><body><p>No Wi-Fi connection, try to connect to a Wi-Fi network or click the retry button.</p></body></html>")

        self.bt_retryWifiConnect = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.bt_retryWifi())
        self.bt_retryWifiConnect.setGeometry(QtCore.QRect(40, 120, 300, 40))
        self.bt_retryWifiConnect.setFont(self.font_labels)
        self.bt_retryWifiConnect.setObjectName("bt_retryWifiConnect")
        self.bt_retryWifiConnect.setText("Retry")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

    def setupUi(self, MainWindow):
        '''
        We initialize all the widgets of the app, such as buttons, labels, etc
        '''
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(380, 632)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lineEdit_country = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_country.setGeometry(QtCore.QRect(40, 20, 300, 40))
        self.lineEdit_country.setFont(self.font_labels)
        self.lineEdit_country.setStyleSheet("border:none;")
        self.lineEdit_country.setClearButtonEnabled(True)
        self.lineEdit_country.setObjectName("lineEdit_country")
        self.lineEdit_country.returnPressed.connect(lambda: self.searchCountry(self.lineEdit_country.text()))
        
        self.lab_totCas = QtWidgets.QLabel(self.centralwidget)
        self.lab_totCas.setGeometry(QtCore.QRect(40, 250, 131, 21))
        self.lab_totCas.setFont(self.font_labels)
        self.lab_totCas.setObjectName("lab_totCas")
        
        self.bt_search = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.searchCountry(self.lineEdit_country.text()))
        self.bt_search.setGeometry(QtCore.QRect(40, 80, 300, 40))
        self.bt_search.setFont(self.font_labels)
        self.bt_search.setObjectName("bt_search")
        
        self.bt_searchWorldwideCases = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.searchCountry('Worldwide'))
        self.bt_searchWorldwideCases.setGeometry(QtCore.QRect(40, 140, 300, 40))
        self.bt_searchWorldwideCases.setFont(self.font_labels)
        self.bt_searchWorldwideCases.setObjectName("bt_searchWorldwideCases")
        
        self.lab_country = QtWidgets.QLabel(self.centralwidget)
        self.lab_country.setGeometry(QtCore.QRect(0, 190, 380, 41))
        self.lab_country.setFont(self.font_labels)
        self.lab_country.setObjectName("lab_country")
        
        self.lab_totCasNum = QtWidgets.QLabel(self.centralwidget)
        self.lab_totCasNum.setGeometry(QtCore.QRect(70, 280, 271, 31))
        self.lab_totCasNum.setFont(self.font_labels)
        self.lab_totCasNum.setObjectName("lab_totCasNum")
        
        self.lab_totDeathsNum = QtWidgets.QLabel(self.centralwidget)
        self.lab_totDeathsNum.setGeometry(QtCore.QRect(70, 350, 271, 31))
        self.lab_totDeathsNum.setFont(self.font_labels)
        self.lab_totDeathsNum.setObjectName("lab_totDeathsNum")
        
        self.lab_totDeaths = QtWidgets.QLabel(self.centralwidget)
        self.lab_totDeaths.setGeometry(QtCore.QRect(40, 320, 131, 21))
        self.lab_totDeaths.setFont(self.font_labels)
        self.lab_totDeaths.setObjectName("lab_totDeaths")
        
        self.lab_totRec = QtWidgets.QLabel(self.centralwidget)
        self.lab_totRec.setGeometry(QtCore.QRect(40, 390, 171, 21))
        self.lab_totRec.setFont(self.font_labels)
        self.lab_totRec.setObjectName("lab_totRec")
        
        self.lab_totRecNum = QtWidgets.QLabel(self.centralwidget)
        self.lab_totRecNum.setGeometry(QtCore.QRect(70, 420, 271, 31))
        self.lab_totRecNum.setFont(self.font_labels)
        self.lab_totRecNum.setObjectName("lab_totRecNum")
        
        self.lab_pop = QtWidgets.QLabel(self.centralwidget)
        self.lab_pop.setGeometry(QtCore.QRect(40, 460, 131, 21))
        self.lab_pop.setFont(self.font_labels)
        self.lab_pop.setObjectName("lab_pop")
        
        self.lab_popNum = QtWidgets.QLabel(self.centralwidget)
        self.lab_popNum.setGeometry(QtCore.QRect(70, 490, 271, 31))
        self.lab_popNum.setFont(self.font_labels)
        
        self.lab_popNum.setObjectName("lab_popNum")

        self.bt_refreshData = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.refreshData())
        self.bt_refreshData.setGeometry(QtCore.QRect(40, 530, 300, 40))
        self.bt_refreshData.setFont(self.font_labels)
        self.bt_refreshData.setObjectName("bt_refreshData")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

    def setWidgetsTexts(self, txt_totCas = '---', txt_totDeaths = '---', txt_totRec = '---', txt_pop = '---'):   
        '''
        It changes the text of the labels to the correct value of it

        It takes 4 parameters:
        1) txt_totCas are the total cases values
        2) txt_totDeaths are the total deaths values
        3) txt_totRec are the total recovered values
        4) txt_pop is the population value
        '''     
        
        self.bt_search.setText("Search")
        self.bt_searchWorldwideCases.setText("Search worldwide cases")
        
        # We align the country to be in the center
        self.lab_country.setText("<p align=\"center\">{}:</p>".format(self.country))

        self.lab_totCas.setText("Total cases:")
        self.lab_totCasNum.setText(txt_totCas)
        
        self.lab_totDeaths.setText("Total deaths:")
        self.lab_totDeathsNum.setText(txt_totDeaths)
        
        self.lab_totRec.setText("Total recovered:")
        self.lab_totRecNum.setText(txt_totRec)
        
        self.lab_pop.setText("Population:")
        self.lab_popNum.setText(txt_pop)

        self.bt_refreshData.setText("Refresh")
        

    def searchCountry(self, country):
        '''
        Takes the coronavirus data of the country passed as a parameter through a dictionary we had created before
        '''
        
        # We check if the country is empty
        if country == '':
            msg = QMessageBox()
            msg.setWindowTitle('Country not valid')
            msg.setText('Please enter a valid country')
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

        # If the country is not empty, we get all the data through the dictionary self.covidData
        else:
            self.lineEdit_country.setText('')
            self.country = country.title()
            
            # We return '---' if we couldn't find the country
            cases = self.covidData.get(country.lower(), ['---'])[0]
            deaths = self.covidData.get(country.lower(), ['', '---'])[1]
            recovered = self.covidData.get(country.lower(), ['', '', '---'])[2]
            population = self.covidData.get(country.lower(), ['', '', '', '---'])[3]
            
            # We replace the text of the labels to the correct values
            self.setWidgetsTexts(txt_totCas = cases, txt_totDeaths = deaths, txt_totRec = recovered, txt_pop = population)

    def refreshData(self):
        ''''
        We update all the coronavirus cases and also the population of each country through two webs and then we append all the information into a dictionary

        Webpages used:
        1) https://www.worldometers.info/coronavirus
        2) https://countrymeters.info/en/World
        '''
        
        if self.is_wifiActive():
            self.source1 = requests.get('https://www.worldometers.info/coronavirus').text
            self.soup1 = BeautifulSoup(self.source1, 'lxml')

            self.source2 = requests.get('https://countrymeters.info/en/World').text
            self.soup2 = BeautifulSoup(self.source2, 'lxml')

            # We add all coronavirus cases to the list 'countries'
            countries = self.soup1.find_all('tr', style = '')[2:221]

            # We introduce the values of the key 'worldwide' individually in the dictionary because those values aren't in a table so they have different HTML labels
            self.covidData['worldwide'] = [
                self.soup1.find_all('div', class_ = 'maincounter-number')[0].span.text, # Worldwide cases
                self.soup1.find_all('div', class_ = 'maincounter-number')[1].span.text, # Worldwide deaths
                self.soup1.find_all('div', class_ = 'maincounter-number')[2].span.text, # Worldwide recovered
                self.soup2.find('div', id = 'cp1').text # Worldwide populations
                ]

            # We iterate through our list 'countries' and add each country to the dictionary self.covidData
            for i in countries:
                try:
                    if len(i.find_all('td', style = 'font-weight: bold; text-align:right;')) == 1:
                        deaths_ = i.find_all('td', style = 'font-weight: bold; text-align:right;')[0].text

                    else:
                        deaths_ = i.find_all('td', style = 'font-weight: bold; text-align:right;')[1].text

                    self.covidData[i.find('td', style = 'font-weight: bold; font-size:15px; text-align:left;').a.text.lower()] = [
                        i.find_all('td', style = 'font-weight: bold; text-align:right')[0].text, # Total cases
                        deaths_, # Total deaths
                        i.find_all('td', style = 'font-weight: bold; text-align:right')[1].text, # Total recovered
                        i.find_all('td', style = 'font-weight: bold; text-align:right')[7].text # Total population
                    ]

                except:
                    pass

            self.searchCountry(self.country)

        else:
            msg = QMessageBox()
            msg.setWindowTitle('No Wi-Fi connection')
            msg.setText('Please connect to a Wi-Fi network to refresh the data')
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    # We check if the wifi is active to initialize all the app, otherwise, we put a different screen telling the user that there's no wifi connection
    if ui.is_wifiActive():
        ui.setupUi(MainWindow)
        ui.refreshData()
        ui.searchCountry('Worldwide')

    else:
        ui.setupWifiUi(MainWindow)


    MainWindow.show()
    sys.exit(app.exec_())
