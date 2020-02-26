"""
Dialog
======

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Dialogs <https://material.io/design/components/dialogs.html>`_

Example
-------

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.utils import get_hex_from_color

from kivymd.uix.dialog import MDInputDialog, MDDialog
from kivymd.theming import ThemeManager


Builder.load_string('''
<ExampleDialogs@BoxLayout>
    orientation: 'vertical'
    spacing: dp(5)

    MDToolbar:
        id: toolbar
        title: app.title
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color

    FloatLayout:
        MDRectangleFlatButton:
            text: "Open input dialog"
            pos_hint: {'center_x': .5, 'center_y': .7}
            opposite_colors: True
            on_release: app.show_example_input_dialog()

        MDRectangleFlatButton:
            text: "Open Ok Cancel dialog"
            pos_hint: {'center_x': .5, 'center_y': .5}
            opposite_colors: True
            on_release: app.show_example_okcancel_dialog()
''')


class Example(MDApp):
    title = "Dialogs"

    def build(self):
        return Factory.ExampleDialogs()

    def callback_for_menu_items(self, *args):
        from kivymd.toast.kivytoast import toast
        toast(args[0])

    def show_example_input_dialog(self):
        dialog = MDInputDialog(
            title='Title', hint_text='Hint text', size_hint=(.8, .4),
            text_button_ok='Yes',
            events_callback=self.callback_for_menu_items)
        dialog.open()

    def show_example_okcancel_dialog(self):
        dialog = MDDialog(
            title='Title', size_hint=(.8, .3), text_button_ok='Yes',
            text="Your [color=%s][b]text[/b][/color] dialog" % get_hex_from_color(
                self.theme_cls.primary_color),
            text_button_cancel='Cancel',
            events_callback=self.callback_for_menu_items)
        dialog.open()


Example().run()
"""

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView

from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDTextButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.theming import ThemableBehavior
from kivymd import images_path
from kivymd.material_resources import DEVICE_IOS


Builder.load_string(
    """
#:import images_path kivymd.images_path


<ContentInputDialog>
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)

    MDLabel:
        font_style: 'H6'
        text: root.title
        halign: 'left' if not root.device_ios else 'center'

    BoxLayout:
        id: box_input
        size_hint: 1, None

    Widget:
    Widget:

    MDSeparator:
        id: sep

    BoxLayout:
        id: box_buttons
        size_hint_y: None
        height: dp(20)
        padding: dp(20), 0, dp(20), 0

#:import webbrowser webbrowser
#:import parse urllib.parse
<ThinLabel@MDLabel>:
    size_hint: 1, None
    valign: 'middle'
    height: self.texture_size[1]

<ThinLabelButton@ThinLabel+MDTextButton>:
    size_hint_y: None
    valign: 'middle'
    height: self.texture_size[1]

<ThinBox@BoxLayout>:
    size_hint_y: None
    height: self.minimum_height
    padding: dp(0), dp(0), dp(10), dp(0)


<ListMDDialog>
    title: ""
    BoxLayout:
        orientation: 'vertical'
        padding: dp(15)
        spacing: dp(10)
    
        MDLabel:
            id: title
            text: root.title
            font_style: 'H6'
            halign: 'left' if not root.device_ios else 'center'
            valign: 'top'
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1]
    
        ScrollView:
            id: scroll
            size_hint_y: None
            height:
                root.height - (title.height + dp(48)\
                + sep.height)
    
            canvas:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    #source: '{}dialog_in_fade.png'.format(images_path)
                    source: '{}transparent.png'.format(images_path)
    
            MDList:
                id: list_layout
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(15)
                canvas.before:
                    Rectangle:
                        pos: self.pos
                        size: self.size
                    Color:
                        rgba: [1,0,0,.5]   
                ThinBox:
                    ThinLabel:
                        text: "Address: "
                    ThinLabelButton:
                        text: root.address
                        on_release:
                            webbrowser.open("http://maps.apple.com/?address="+parse.quote(self.text))
                ThinBox:
                    ThinLabel:
                        text: "Website: "
                    ThinLabelButton:
                        text: root.Website
                        on_release:
                            webbrowser.open(self.text)
                ThinBox:
                    ThinLabel:
                        text: "Facebook: "
                    ThinLabelButton:
                        text: root.Facebook
                        on_release:
                            webbrowser.open(self.text)
                ThinBox:
                    ThinLabel:
                        text: "Twitter: "
                    ThinLabelButton:
                        text: root.Twitter
                        on_release:
                            webbrowser.open(self.text)
                ThinBox:
                    ThinLabel:
                        text: "Season1 Date: "
                    ThinLabel:
                        text: root.Season1_date
                ThinBox:
                    ThinLabel:
                        text: "Season1 Hours: "
                    ThinLabel:
                        text: root.Season1_hours
                ThinBox:
                    ThinLabel:
                        text: "Season2 Date: "
                    ThinLabel:
                        text: root.Season2_date
                ThinBox:
                    ThinLabel:
                        text: "Season2 Hours: "
                    ThinLabel:
                        text: root.Season2_hours
                ThinBox:
                    ThinLabel:
                        text: "Season3 Date: "
                    ThinLabel:
                        text: root.Season3_date
                ThinBox:
                    ThinLabel:
                        text: "Season3 Hours: "
                    ThinLabel:
                        text: root.Season3_hours
                ThinBox:
                    ThinLabel:
                        text: "Season4 Date: "
                    ThinLabel:
                        text: root.Season4_date
                ThinBox:
                    ThinLabel:
                        text: "Season4 Hours: "
                    ThinLabel:
                        text: root.Season4_hours
                ThinBox:
                    ThinLabel:
                        text: "Credit: "
                    ThinLabel:
                        text: root.Credit
                ThinBox:
                    ThinLabel:
                        text: "WIC: "
                    ThinLabel:
                        text: root.WIC
                ThinBox:
                    ThinLabel:
                        text: "WICcash: "
                    ThinLabel:
                        text: root.WICcash
                ThinBox:
                    ThinLabel:
                        text: "SFMNP: "
                    ThinLabel:
                        text: root.SFMNP
                ThinBox:
                    ThinLabel:
                        text: "SNAP: "
                    ThinLabel:
                        text: root.SNAP
                ThinBox:
                    ThinLabel:
                        text: "Organic: "
                    ThinLabel:
                        text: root.Organic
                ThinBox:
                    ThinLabel:
                        text: "Baked Goods: "
                    ThinLabel:
                        text: root.Bakedgoods
                ThinBox:
                    ThinLabel:
                        text: "Cheese: "
                    ThinLabel:
                        text: root.Cheese
                ThinBox:
                    ThinLabel:
                        text: "Crafts: "
                    ThinLabel:
                        text: root.Crafts
                ThinBox:
                    ThinLabel:
                        text: "Flowers: "
                    ThinLabel:
                        text: root.Flowers
                ThinBox:
                    ThinLabel:
                        text: "Eggs: "
                    ThinLabel:
                        text: root.Eggs
                ThinBox:
                    ThinLabel:
                        text: "Seafood: "
                    ThinLabel:
                        text: root.Seafood
                ThinBox:
                    ThinLabel:
                        text: "Herbs: "
                    ThinLabel:
                        text: root.Herbs
                ThinBox:
                    ThinLabel:
                        text: "Vegetables: "
                    ThinLabel:
                        text: root.Vegetables
                ThinBox:
                    ThinLabel:
                        text: "Honey: "
                    ThinLabel:
                        text: root.Honey
                ThinBox:
                    ThinLabel:
                        text: "Jams: "
                    ThinLabel:
                        text: root.Jams
                ThinBox:
                    ThinLabel:
                        text: "Maple: "
                    ThinLabel:
                        text: root.Maple
                ThinBox:
                    ThinLabel:
                        text: "Meat: "
                    ThinLabel:
                        text: root.Meat
                ThinBox:
                    ThinLabel:
                        text: "Nursery: "
                    ThinLabel:
                        text: root.Nursery
                ThinBox:
                    ThinLabel:
                        text: "Nuts: "
                    ThinLabel:
                        text: root.Nuts
                ThinBox:
                    ThinLabel:
                        text: "Plants: "
                    ThinLabel:
                        text: root.Plants
                ThinBox:
                    ThinLabel:
                        text: "Poultry: "
                    ThinLabel:
                        text: root.Poultry
                ThinBox:
                    ThinLabel:
                        text: "Prepared: "
                    ThinLabel:
                        text: root.Prepared
                ThinBox:
                    ThinLabel:
                        text: "Soap: "
                    ThinLabel:
                        text: root.Soap
                ThinBox:
                    ThinLabel:
                        text: "Trees: "
                    ThinLabel:
                        text: root.Trees
                ThinBox:
                    ThinLabel:
                        text: "Wine: "
                    ThinLabel:
                        text: root.Wine
                ThinBox:
                    ThinLabel:
                        text: "Coffee: "
                    ThinLabel:
                        text: root.Coffee
                ThinBox:
                    ThinLabel:
                        text: "Beans: "
                    ThinLabel:
                        text: root.Beans
                ThinBox:
                    ThinLabel:
                        text: "Fruits: "
                    ThinLabel:
                        text: root.Fruits
                ThinBox:
                    ThinLabel:
                        text: "Grains: "
                    ThinLabel:
                        text: root.Grains
                ThinBox:
                    spacing: dp(10)
                    ThinLabel:
                        id: juices
                        text: "Juices: "
                    ThinLabel:
                        text: root.Juices
                ThinBox:
                    spacing: dp(10)
                    ThinLabel:
                        text: "Mushrooms: "
                    ThinLabel:
                        text: root.Mushrooms
                ThinBox:
                    ThinLabel:
                        text: "Pet Food: "
                    ThinLabel:
                        text: root.PetFood
                ThinBox:
                    ThinLabel:
                        text: "Tofu: "
                    ThinLabel:
                        text: root.Tofu
                ThinBox:
                    ThinLabel:
                        text: "Wild Harvested: "
                    ThinLabel:
                        text: root.WildHarvested
        MDSeparator:
            id: sep


<ContentMDDialog>
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)

    text_button_ok: ''
    text_button_cancel: ''

    MDLabel:
        id: title
        text: root.title
        font_style: 'H6'
        halign: 'left' if not root.device_ios else 'center'
        valign: 'top'
        size_hint_y: None
        text_size: self.width, None
        height: self.texture_size[1]

    ScrollView:
        id: scroll
        size_hint_y: None
        height:
            root.height - (box_buttons.height + title.height + dp(48)\
            + sep.height)

        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                #source: f'{images_path}dialog_in_fade.png'
                source: f'{images_path}transparent.png'

        MDLabel:
            text: '\\n' + root.text + '\\n'
            size_hint_y: None
            height: self.texture_size[1]
            valign: 'top'
            halign: 'left' if not root.device_ios else 'center'
            markup: True

    MDSeparator:
        id: sep

    BoxLayout:
        id: box_buttons
        size_hint_y: None
        height: dp(20)
        padding: dp(20), 0, dp(20), 0
"""
)

if DEVICE_IOS:
    Heir = BoxLayout
else:
    Heir = MDCard


# FIXME: Not work themes for iOS.
class BaseDialog(ThemableBehavior, ModalView):
    def set_content(self, instance_content_dialog):
        def _events_callback(result_press):
            self.dismiss()
            if result_press and self.events_callback:
                self.events_callback(result_press, self)

        if self.device_ios:  # create buttons for iOS
            self.background = self._background

            if isinstance(instance_content_dialog, ContentInputDialog):
                self.text_field = MDTextFieldRect(
                    pos_hint={"center_x": 0.5},
                    size_hint=(1, None),
                    multiline=False,
                    height=dp(33),
                    cursor_color=self.theme_cls.primary_color,
                    hint_text=instance_content_dialog.hint_text,
                )
                instance_content_dialog.ids.box_input.height = dp(33)
                instance_content_dialog.ids.box_input.add_widget(
                    self.text_field
                )

            if self.text_button_cancel != "":
                anchor = "left"
            else:
                anchor = "center"
            box_button_ok = AnchorLayout(anchor_x=anchor)
            box_button_ok.add_widget(
                MDTextButton(
                    text=self.text_button_ok,
                    font_size="18sp",
                    on_release=lambda x: _events_callback(self.text_button_ok),
                )
            )
            instance_content_dialog.ids.box_buttons.add_widget(box_button_ok)

            if self.text_button_cancel != "":
                box_button_ok.anchor_x = "left"
                box_button_cancel = AnchorLayout(anchor_x="right")
                box_button_cancel.add_widget(
                    MDTextButton(
                        text=self.text_button_cancel,
                        font_size="18sp",
                        on_release=lambda x: _events_callback(
                            self.text_button_cancel
                        ),
                    )
                )
                instance_content_dialog.ids.box_buttons.add_widget(
                    box_button_cancel
                )

        else:  # create buttons for Android
            if isinstance(instance_content_dialog, ContentInputDialog):
                self.text_field = MDTextField(
                    size_hint=(1, None),
                    height=dp(48),
                    hint_text=instance_content_dialog.hint_text,
                )
                instance_content_dialog.ids.box_input.height = dp(48)
                instance_content_dialog.ids.box_input.add_widget(
                    self.text_field
                )
                instance_content_dialog.ids.box_buttons.remove_widget(
                    instance_content_dialog.ids.sep
                )

            box_buttons = AnchorLayout(
                anchor_x="right", size_hint_y=None, height=dp(30)
            )
            box = BoxLayout(size_hint_x=None, spacing=dp(5))
            box.bind(minimum_width=box.setter("width"))
            button_ok = MDRaisedButton(
                text=self.text_button_ok,
                on_release=lambda x: _events_callback(self.text_button_ok),
            )
            box.add_widget(button_ok)

            if self.text_button_cancel != "":
                button_cancel = MDFlatButton(
                    text=self.text_button_cancel,
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: _events_callback(
                        self.text_button_cancel
                    ),
                )
                box.add_widget(button_cancel)

            box_buttons.add_widget(box)
            instance_content_dialog.ids.box_buttons.add_widget(box_buttons)
            instance_content_dialog.ids.box_buttons.height = button_ok.height
            instance_content_dialog.remove_widget(
                instance_content_dialog.ids.sep
            )

class ListMDDialog(BaseDialog):
    name = StringProperty("Missing data")
    address = StringProperty("Missing data")
    Website = StringProperty("Missing data")
    Facebook = StringProperty("Missing data")
    Twitter = StringProperty("Missing data")
    Season1_date = StringProperty("Missing data")
    Season1_hours = StringProperty("Missing data")
    Season2_date = StringProperty("Missing data")
    Season2_hours = StringProperty("Missing data")
    Season3_date = StringProperty("Missing data")
    Season3_hours = StringProperty("Missing data")
    Season4_date = StringProperty("Missing data")
    Season4_hours = StringProperty("Missing data")
    Credit = StringProperty("Missing data")
    WIC = StringProperty("Missing data")
    WICcash = StringProperty("Missing data")
    SFMNP = StringProperty("Missing data")
    SNAP = StringProperty("Missing data")
    Organic = StringProperty("Missing data")
    Bakedgoods = StringProperty("Missing data")
    Cheese = StringProperty("Missing data")
    Crafts = StringProperty("Missing data")
    Flowers = StringProperty("Missing data")
    Eggs = StringProperty("Missing data")
    Seafood = StringProperty("Missing data")
    Herbs = StringProperty("Missing data")
    Vegetables = StringProperty("Missing data")
    Honey = StringProperty("Missing data")
    Jams = StringProperty("Missing data")
    Maple = StringProperty("Missing data")
    Meat = StringProperty("Missing data")
    Nursery = StringProperty("Missing data")
    Nuts = StringProperty("Missing data")
    Plants = StringProperty("Missing data")
    Poultry = StringProperty("Missing data")
    Prepared = StringProperty("Missing data")
    Soap = StringProperty("Missing data")
    Trees = StringProperty("Missing data")
    Wine = StringProperty("Missing data")
    Coffee = StringProperty("Missing data")
    Beans = StringProperty("Missing data")
    Fruits = StringProperty("Missing data")
    Grains = StringProperty("Missing data")
    Juices = StringProperty("Missing data")
    Mushrooms = StringProperty("Missing data")
    PetFood = StringProperty("Missing data")
    Tofu = StringProperty("Missing data")
    WildHarvested = StringProperty("Missing data")
    background = StringProperty('{}ios_bg_mod.png'.format(images_path))



class MDInputDialog(BaseDialog):
    title = StringProperty("Title")
    hint_text = StringProperty()
    text_button_ok = StringProperty("Ok")
    text_button_cancel = StringProperty()
    events_callback = ObjectProperty()
    _background = StringProperty(f"{images_path}ios_bg_mod.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.content_dialog = ContentInputDialog(
            title=self.title,
            hint_text=self.hint_text,
            text_button_ok=self.text_button_ok,
            text_button_cancel=self.text_button_cancel,
            device_ios=self.device_ios,
        )
        self.add_widget(self.content_dialog)
        self.set_content(self.content_dialog)
        Clock.schedule_once(self.set_field_focus, 0.5)

    def set_field_focus(self, interval):
        self.text_field.focus = True


class MDDialog(BaseDialog):
    title = StringProperty("Title")
    text = StringProperty("Text dialog")
    text_button_cancel = StringProperty()
    text_button_ok = StringProperty("Ok")
    events_callback = ObjectProperty()
    _background = StringProperty(f"{images_path}ios_bg_mod.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        content_dialog = ContentMDDialog(
            title=self.title,
            text=self.text,
            text_button_ok=self.text_button_ok,
            text_button_cancel=self.text_button_cancel,
            device_ios=self.device_ios,
        )
        self.add_widget(content_dialog)
        self.set_content(content_dialog)


class ContentInputDialog(Heir):
    title = StringProperty()
    hint_text = StringProperty()
    text_button_ok = StringProperty()
    text_button_cancel = StringProperty()
    device_ios = BooleanProperty()


class ContentMDDialog(Heir):
    title = StringProperty()
    text = StringProperty()
    text_button_cancel = StringProperty()
    text_button_ok = StringProperty()
    device_ios = BooleanProperty()
