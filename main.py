from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
#-*- coding:utf8 -*-
import tfui2
import output

class TestDialog(QDialog,tfui2.Ui_Tf_dialog):
    def __init__(self,parent=None):
        super(TestDialog,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.Tf_button, SIGNAL("clicked()"),self.myclicked)
        self.Tf_text.setText('(A | ~B | ~C) & (~A | ~B | ~C) & (A | B | ~C) & (A | ~B | C)')
        self.Tf_text.selectAll()
        self.Tf_text.setFocus()
        
    def myclicked(self):
        self.Tf_table.clear()
        qex = self.Tf_text.text()
        expression = str(qex)
        
        try:
            output.formatprint(expression)
        except Exception , e:
            self.Tf_table.setText(e)
        self.Tf_table.setText(output.routput.getvalue())
        pass
        
app=QApplication(sys.argv)
dialog=TestDialog()
dialog.show()
app.exec_()