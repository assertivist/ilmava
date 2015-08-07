#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Spotlight, DirectionalLight, loadPrcFile, AntialiasAttrib
from direct.task import Task
import sys


class MyApp(ShowBase):
    def __init__(self):

        loadPrcFile('config.prc')
        ShowBase.__init__(self)

        base.disableMouse()
        self.render.setShaderAuto()
        self.accept("escape", sys.exit)
        # Model
        model = self.loader.loadModel("twisted")
        model.reparent_to(self.render)
        self.model = model # For reference in the rotation task
        # Light
        light = Spotlight('light')
        light_np = self.render.attachNewNode(light)
        light_np.set_pos(25, 25, 25)
        light_np.look_at(0, 0, 0)
        # Model-light interaction
        light.setShadowCaster(True)
        light.getLens().setNearFar(1, 50)
        self.render.setLight(light_np)
        # Camera
        self.camera.set_pos(0, -60, 30)
        self.camera.look_at(0, 0, 0)
        # Rotating the object
        self.taskMgr.add(self.rotate_object, 'rotate object')
        self.render.setAntialias(AntialiasAttrib.MMultisample)

    def rotate_object(self, task):
        self.model.set_h(task.getElapsedTime() * 60)
        return Task.cont

app = MyApp()
app.run()

