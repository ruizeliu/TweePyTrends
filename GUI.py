import GoogleTrends
import go
import sys
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class WelcomeWindow(QWidget):

    switch_window = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('TweePyTrends')

        layout = QGridLayout()

        t1 = QLabel(self)
        t1.setText('Welcome to TweePyTrends!')
        layout.addWidget(t1)
        t2 = QLabel(self)
        t2.setText('	It is developed by Dominic, Ruize, Jiaqi and Ya-Han')
        layout.addWidget(t2)
        t3 = QLabel(self)
        t3.setText(' ')
        layout.addWidget(t3)
        t4 = QLabel(self)
        t4.setText('This app helps users get a clearer picture of trending topics on Twitter and Google:')
        layout.addWidget(t4)
        t5 = QLabel(self)
        t5.setText('	1.GoogleTrends shows top search by country, search frequency over time, and key word cloud')
        layout.addWidget(t5)
        t6 = QLabel(self)
        t6.setText('	2.Real-time Twi searches keyword as hashtag and visualizes it with related tweets and hashtags')
        layout.addWidget(t6)
        t7 = QLabel(self)
        t7.setText('	3.Historical Twi uses a seperate program, searches and visualizes all historical tweets')
        layout.addWidget(t7)
        t8 = QLabel(self)
        t8.setText(' ')
        layout.addWidget(t8)
        t9 = QLabel(self)
        t9.setText('!! NOTICE !!')
        layout.addWidget(t9)
        t10 = QLabel(self)
        t10.setText('To collect historical tweets, please run')
        layout.addWidget(t10)
        t11 = QLabel(self)
        t11.setText('           python3 go2.py word start_date end_date')
        layout.addWidget(t11)
        t12 = QLabel(self)
        t12.setText('in command line BEFORE entering the app')
        layout.addWidget(t12)


        self.button = QPushButton('Try TweePyTrends now')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit()


class InsertWindow(QWidget):

    switch_window1 = pyqtSignal(str, str, str)
    switch_window2 = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('TweePyTrends Main Control Page')

        layout = QGridLayout()

        t1 = QLabel(self)
        t1.setText('Please enter a word for analysis')
        layout.addWidget(t1,0,0)
        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit,0,1)

        t2 = QLabel(self)
        t2.setText('Please enter start date (yyyy-mm-dd)')
        layout.addWidget(t2,1,0)
        self.date_edit1 = QLineEdit()
        layout.addWidget(self.date_edit1,1,1)

        t3 = QLabel(self)
        t3.setText('Please enter end date (yyyy-mm-dd)')
        layout.addWidget(t3,2,0)
        self.date_edit2 = QLineEdit()
        layout.addWidget(self.date_edit2,2,1)

        self.button1 = QPushButton('Start analysis for your own word')
        self.button1.clicked.connect(self.switch1)
        layout.addWidget(self.button1,3,0)

        t4 = QLabel(self)
        t4.setText('Search "coronavirus" from 2019-12-01 to 2020-03-01')
        layout.addWidget(t4,4,0)

        self.button2 = QPushButton('Sample from previous scrapped word')
        self.button2.clicked.connect(self.switch2)
        layout.addWidget(self.button2,5,0)

        self.setLayout(layout)

    def switch1(self):
        self.switch_window1.emit(self.line_edit.text(), \
                                 self.date_edit1.text(), self.date_edit2.text())

    def switch2(self):
        self.switch_window2.emit()


############# Previous Search #######################
class PreviousWindow(QWidget):

    switch_window1 = pyqtSignal()
    switch_window2 = pyqtSignal()
    switch_window3 = pyqtSignal()
    switch_window4 = pyqtSignal()

    def __init__(self):

        QWidget.__init__(self)
        self.setWindowTitle('Previous scraping example')

        layout = QGridLayout()

        t1 = QLabel(self)
        t1.setText('Search "coronavirus" from 2019-12-01 to 2020-03-01')
        layout.addWidget(t1)

        self.button1 = QPushButton('See Google Trends')
        self.button1.clicked.connect(self.switch1)
        layout.addWidget(self.button1)

        self.button2 = QPushButton('See Historical Twi')
        self.button2.clicked.connect(self.switch2)
        layout.addWidget(self.button2)

        self.button3 = QPushButton('See Real-time Twi')
        self.button3.clicked.connect(self.switch3)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('Go back')
        self.button4.clicked.connect(self.switch4)
        layout.addWidget(self.button4)

        self.setLayout(layout)

    def switch1(self):
        self.switch_window1.emit()

    def switch2(self):
        self.switch_window2.emit()

    def switch3(self):
        self.switch_window3.emit()

    def switch4(self):
        self.switch_window4.emit()


class PreviousGoogle(QWidget):

    switch_window = pyqtSignal()

    def __init__(self):

        QWidget.__init__(self)
        self.setWindowTitle('Previous scraping example')

        layout = QGridLayout()

        t = QLabel(self)
        t.setText('Search "coronavirus" from 2019-12-01 to 2020-03-01')
        layout.addWidget(t,0,0)

        g = QLabel(self)
        graph = QPixmap('image/example_google_country.png')
        graph = graph.scaledToWidth(600)
        g.setPixmap(graph)
        layout.addWidget(g,1,0)

        g2 = QLabel(self)
        graph2 = QPixmap('image/example_google_freq.png')
        graph2 = graph2.scaledToWidth(600)
        g2.setPixmap(graph2)
        layout.addWidget(g2,1,1)

        g3 = QLabel(self)
        graph3 = QPixmap('image/example_google_topics.png')
        graph3 = graph3.scaledToWidth(600)
        g3.setPixmap(graph3)
        layout.addWidget(g3,2,0)

        g4 = QLabel(self)
        graph4 = QPixmap('image/example_google_wordcloud.png')
        graph4 = graph4.scaledToWidth(600)
        g4.setPixmap(graph4)
        layout.addWidget(g4,2,1)

        self.button = QPushButton('Go back')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button,0,1)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit()


class PreviousHisTweet(QWidget):

    switch_window = pyqtSignal()

    def __init__(self):

        QWidget.__init__(self)
        self.setWindowTitle('Previous scraping example')

        layout = QGridLayout()

        t = QLabel(self)
        t.setText('Search "coronavirus" from 2019-12-01 to 2020-03-01')
        layout.addWidget(t,0,0)

        g = QLabel(self)
        graph = QPixmap('image/example_twitter_hist_freq.png')
        graph = graph.scaledToWidth(600)
        g.setPixmap(graph)
        layout.addWidget(g,1,0)

        g2 = QLabel(self)
        graph2 = QPixmap('image/example_twitter_hist_KOL.png')
        graph2 = graph2.scaledToWidth(600)
        g2.setPixmap(graph2)
        layout.addWidget(g2,1,1)

        g3 = QLabel(self)
        graph3 = QPixmap('image/example_twitter_hist_wordcloud.png')
        graph3 = graph3.scaledToWidth(600)
        g3.setPixmap(graph3)
        layout.addWidget(g3,2,0)

        self.button = QPushButton('Go back')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button,0,1)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit()


class PreviousCurrTweet(QWidget):

    switch_window = pyqtSignal()

    def __init__(self):

        QWidget.__init__(self)
        self.setWindowTitle('Previous scraping example')

        layout = QGridLayout()

        t = QLabel(self)
        t.setText('Search "coronavirus" at 2020-03-15 13:30')
        layout.addWidget(t,0,0)

        g = QLabel(self)
        graph = QPixmap('image/example_twitter_wordcloud_hashtag.png')
        graph = graph.scaledToWidth(600)
        g.setPixmap(graph)
        layout.addWidget(g,2,0)

        g2 = QLabel(self)
        graph2 = QPixmap('image/example_twitter_wordcloud_text.png')
        graph2 = graph2.scaledToWidth(600)
        g2.setPixmap(graph2)
        layout.addWidget(g2,2,1)

        g3 = QLabel(self)
        graph3 = QPixmap('image/example_twitter_network.png')
        graph3 = graph3.scaledToWidth(600)
        g3.setPixmap(graph3)
        layout.addWidget(g3,1,0)

        g4 = QLabel(self)
        graph4 = QPixmap('image/example_twitter_bar_plot.png')
        graph4 = graph4.scaledToWidth(600)
        g4.setPixmap(graph4)
        layout.addWidget(g4,1,1)

        self.button = QPushButton('Go back')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button,0,1)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit()


############# New Search ###########################
class NewWindow(QWidget):

    switch_window1 = pyqtSignal(str, str, str)
    switch_window2 = pyqtSignal(str, str, str)
    switch_window3 = pyqtSignal(str, str, str)
    switch_window4 = pyqtSignal()

    def __init__(self, text, start, end):

        self.text = text
        self.start = start
        self.end = end

        QWidget.__init__(self)

        self.setWindowTitle('Your scraping result')

        layout = QGridLayout()

        t1 = QLabel(self)
        t1.setText('Search "{}" from {} to {}'.format(text, start, end))
        layout.addWidget(t1)

        self.button1 = QPushButton('See Google Trends')
        self.button1.clicked.connect(self.switch1)
        layout.addWidget(self.button1)

        self.button2 = QPushButton('See Historical Twi')
        self.button2.clicked.connect(self.switch2)
        layout.addWidget(self.button2)

        self.button3 = QPushButton('See Real-time Twi')
        self.button3.clicked.connect(self.switch3)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('Go back')
        self.button4.clicked.connect(self.switch4)
        layout.addWidget(self.button4)

        self.setLayout(layout)

    def switch1(self):
        self.switch_window1.emit(self.text, self.start, self.end)

    def switch2(self):
        self.switch_window2.emit(self.text, self.start, self.end)

    def switch3(self):
    	self.switch_window3.emit(self.text, self.start, self.end)

    def switch4(self):
        self.switch_window4.emit()


class NewGoogle(QWidget):

    switch_window = pyqtSignal(str, str, str)

    def __init__(self, text, start, end):

        self.text = text
        self.start = start
        self.end = end

        QWidget.__init__(self)
        self.setWindowTitle('Your scraping result')

        layout = QGridLayout()

        t = QLabel(self)
        t.setText('Search "{}" from {} to {}'.format(text, start, end))
        layout.addWidget(t,0,0)

        GoogleTrends.go(text, start, end)

        g = QLabel(self)
        graph = QPixmap('image/google_country.png')
        graph = graph.scaledToWidth(600)
        g.setPixmap(graph)
        layout.addWidget(g,1,0)

        g2 = QLabel(self)
        graph2 = QPixmap('image/google_freq.png')
        graph2 = graph2.scaledToWidth(600)
        g2.setPixmap(graph2)
        layout.addWidget(g2,1,1)

        g3 = QLabel(self)
        graph3 = QPixmap('image/google_topics.png')
        graph3 = graph3.scaledToWidth(600)
        g3.setPixmap(graph3)
        layout.addWidget(g3,2,0)

        output = "image/{}_google_wordcloud.png".format(self.text)
        if os.path.exists(output):
            g4 = QLabel(self)
            graph4 = QPixmap(output)
            graph4 = graph4.scaledToWidth(600)
            g4.setPixmap(graph4)
            layout.addWidget(g4,2,1)

        self.button = QPushButton('Go back')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button,0,1)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit(self.text, self.start, self.end)


class NewHisTweet(QWidget):

    switch_window = pyqtSignal(str, str, str)

    def __init__(self, text, start, end):

        self.text = text
        self.start = start
        self.end = end

        QWidget.__init__(self)
        self.setWindowTitle('Your scraping result')

        layout = QGridLayout()

        t = QLabel(self)
        t.setText('Search "{}" from {} to {}'.format(text, start, end))
        layout.addWidget(t,0,0)

        g = QLabel(self)
        graph = QPixmap('image/twitter_hist_freq.png')
        graph = graph.scaledToWidth(600)
        g.setPixmap(graph)
        layout.addWidget(g,1,0)

        g2 = QLabel(self)
        graph2 = QPixmap('image/twitter_hist_KOL.png')
        graph2 = graph2.scaledToWidth(600)
        g2.setPixmap(graph2)
        layout.addWidget(g2,1,1)

        g3 = QLabel(self)
        graph3 = QPixmap('image/twitter_hist_wordcloud.png')
        graph3 = graph3.scaledToWidth(600)
        g3.setPixmap(graph3)
        layout.addWidget(g3,2,0)

        self.button = QPushButton('Go back')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button,0,1)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit(self.text, self.start, self.end)


class NewCurrTweet(QWidget):

    switch_window = pyqtSignal(str, str, str)

    def __init__(self, text, start, end):

        self.text = text
        self.start = start
        self.end = end

        QWidget.__init__(self)
        self.setWindowTitle('Your scraping result')

        layout = QGridLayout()

        t = QLabel(self)
        t.setText('Search "{}" on Twitter now'.format(text))
        layout.addWidget(t,0,0)

        go.go(text)

        g = QLabel(self)
        graph = QPixmap('image/twitter_wordcloud_hashtag.png')
        graph = graph.scaledToWidth(600)
        g.setPixmap(graph)
        layout.addWidget(g,2,0)

        g2 = QLabel(self)
        graph2 = QPixmap('image/twitter_wordcloud_text.png')
        graph2 = graph2.scaledToWidth(600)
        g2.setPixmap(graph2)
        layout.addWidget(g2,2,1)

        g3 = QLabel(self)
        graph3 = QPixmap('image/twitter_network.png')
        graph3 = graph3.scaledToWidth(600)
        g3.setPixmap(graph3)
        layout.addWidget(g3,1,0)

        g4 = QLabel(self)
        graph4 = QPixmap('image/twitter_bar_plot.png')
        graph4 = graph4.scaledToWidth(600)
        g4.setPixmap(graph4)
        layout.addWidget(g4,1,1)

        self.button = QPushButton('Go back')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button,0,1)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit(self.text, self.start, self.end)


########### Organize all the buttons #################
class Controller:

    def __init__(self):
        pass

    def show_welcome(self):
        self.welcome = WelcomeWindow()
        self.welcome.switch_window.connect(self.show_insert)
        self.welcome.show()

    def show_insert(self):
        self.insert = InsertWindow()
        self.insert.switch_window1.connect(self.show_new)
        self.insert.switch_window2.connect(self.show_previous)
        self.welcome.close()
        self.insert.show()
        if hasattr(self, 'new'):
            self.new.close()
        if hasattr(self, 'previous'):
            self.previous.close()

    def show_previous(self):
        self.previous = PreviousWindow()
        self.previous.switch_window1.connect(self.show_previous_google)
        self.previous.switch_window2.connect(self.show_previous_histweet)
        self.previous.switch_window3.connect(self.show_previous_currtweet)
        self.previous.switch_window4.connect(self.show_insert)
        self.insert.close()
        self.previous.show()
        if hasattr(self, 'previous_google'):
            self.previous_google.close()
        if hasattr(self, 'previous_histweet'):
            self.previous_histweet.close()
        if hasattr(self, 'previous_currtweet'):
            self.previous_currtweet.close()

    def show_previous_google(self):
        self.previous_google = PreviousGoogle()
        self.previous_google.switch_window.connect(self.show_previous)
        self.previous.close()
        self.previous_google.show()

    def show_previous_histweet(self):
        self.previous_histweet = PreviousHisTweet()
        self.previous_histweet.switch_window.connect(self.show_previous)
        self.previous.close()
        self.previous_histweet.show()

    def show_previous_currtweet(self):
        self.previous_currtweet = PreviousCurrTweet()
        self.previous_currtweet.switch_window.connect(self.show_previous)
        self.previous.close()
        self.previous_currtweet.show()

    def show_new(self, text, start, end):
        self.new = NewWindow(text, start, end)
        self.new.switch_window1.connect(self.show_new_google)
        self.new.switch_window2.connect(self.show_new_histweet)
        self.new.switch_window3.connect(self.show_new_currtweet)
        self.new.switch_window4.connect(self.show_insert)
        self.insert.close()
        self.new.show()
        if hasattr(self, 'new_google'):
            self.new_google.close()
        if hasattr(self, 'new_histweet'):
        	self.new_histweet.close()
        if hasattr(self, 'new_currtweet'):
            self.new_currtweet.close()

    def show_new_google(self, text, start, end):
        self.new_google = NewGoogle(text, start, end)
        self.new_google.switch_window.connect(self.show_new)
        self.new.close()
        self.new_google.show()

    def show_new_histweet(self, text, start, end):
        self.new_histweet = NewHisTweet(text, start, end)
        self.new_histweet.switch_window.connect(self.show_new)
        self.new.close()
        self.new_histweet.show()

    def show_new_currtweet(self, text, start, end):
        self.new_currtweet = NewCurrTweet(text, start, end)
        self.new_currtweet.switch_window.connect(self.show_new)
        self.new.close()
        self.new_currtweet.show()


############# sys #######################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_welcome()
    sys.exit(app.exec_())