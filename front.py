#!/usr/bin/env python
# encoding: utf-8

import npyscreen

from exercitium import start


data = []


class Interface(npyscreen.NPSApp):
    def main(self):
        F = npyscreen.Form(name="Exercitium")
        # t = F.add(
        #     npyscreen.TitleText,
        #     name="Text:",
        # )
        # fn = F.add(npyscreen.TitleFilename, name="Filename:")
        # fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        # dt = F.add(npyscreen.TitleDateCombo, name="Date:")
        # s = F.add(npyscreen.TitleSlider, out_of=12, name="Slider")
        # ml = F.add(
        #     npyscreen.MultiLineEdit,
        #     value="""try typing here!\nMutiline text, press ^R to reformat.\n""",
        #     max_height=5,
        #     rely=9,
        # )
        # ms = F.add(
        #     npyscreen.TitleSelectOne,
        #     max_height=4,
        #     value=[
        #         1,
        #     ],
        #     name="Pick One",
        #     values=["Option1", "Option2", "Option3"],
        #     scroll_exit=True,
        # )
        ms2 = F.add(
            npyscreen.TitleMultiSelect,
            max_height=-2,
            value=[
                1,
            ],
            name="Pick Several",
            values=["Option1", "Option2", "Option3"],
            scroll_exit=True,
        )

        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())


class ExerciseList(npyscreen.MultiLineAction):
    def __init__(self, *args, **kwargs):
        self.add_handlers({
            "^A": self.when_add_record,
            "^D": self.when_delete_record,
        })

    def display_value(self, value):
        return f"{value[0], value[1], value[2]}"

    def actionHighlighted(self, act, keypress):
        self.parent.parentApp.getForm("EDITRECORDFM").value = act[0]
        self.parent.parentApp.switchForm("EDITRECORDFM")

    def when_add_record(self, *args, **kwargs):
        self.parent.parentApp.getForm("EDITRECORDFM").value = None
        self.parent.parentApp.switchForm("EDITRECORDFM")

    def when_delete_record(self, *args, **kwargs):
        self.parent.parentApp.getForm("EDITRECORDFM").value = None
        self.parent.parentApp.switchForm("EDITRECORDFM")


class RecordListDisplay(npyscreen.FormMutt):
    MAIN_WIDGET_CLASS = ExerciseList


class InterfaceApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.myDatabase = start()
        self.addForm("MAIN", RecordListDisplay)
        self.addForm("EDITRECORDFM", ExerciseList)


if __name__ == '__main__':
    myApp = InterfaceApplication()
    myApp.run()
