#!/usr/bin/env python2

from __future__ import division, print_function

import yaml

import rospy

import time

import numpy as np
import cv2
from tf import transformations as tft

from darknet_ros_msgs.msg import BoundingBoxes
import cv_bridge
bridge = cv_bridge.CvBridge()

ALPHABAT = "abcdefghi"

class Semantic:
    def __init__(self, label, xmin, xmax, ymin, ymax):
        self.label = label
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

class Semantic_Dfa:
    def __init__(self):
        '''
        Semantic_Dfa is a controller that finish system to do LTL task
        
        '''
        self.objects = rospy.Subscriber('/darknet_ros/bounding_boxes',BoundingBoxes, self._semantic_information_callback, queue_size=1)
        self.objects_semantic_dict = {}
        self.objects_semantic = []
        self.waiting = False
        self.recevied = False
        rospy.loginfo("Semantic_Dfa node is up")
        self.state2semantic = {}
        self.semantic2state = {}
        self.trace = None

    def _semantic_information_callback(self, msg):
        rospy.loginfo("callbackfunction up")
        # print(msg.bounding_boxes[0].Class)
        for ob in msg.bounding_boxes:
            semantic = Semantic(ob.Class, ob.xmin, ob.xmax, ob.ymin, ob.ymax)
            print("label:", ob.Class)
            print("xmin:", ob.xmin)
            print("xmax:", ob.xmax)
            print("ymin:", ob.ymin)
            print("ymax:", ob.ymax)
            self.objects_semantic_dict[ob.Class] = semantic
            self.objects_semantic.append(ob.Class)
        for i in range(len(set(self.objects_semantic))):
            self.semantic2state[self.objects_semantic[i]] = ALPHABAT[i]
            self.state2semantic[ALPHABAT[i]] = self.objects_semantic[i]
        print("the initial state are: ", set(self.objects_semantic))
        print(self.state2semantic)
        print(self.semantic2state) 
        self.recevied = True
        rospy.Subscriber.unregister(self.objects)
    
    # def follow_trace(self):
    #     '''
    #         automata's trace
    #     '''
    #     for i in self.trace:
    #         for t in self.state:
    #             if self.state[t] == i:

            
    
    def attention_semantic(self, semantic):
        '''
            semantic is a class object, which has label, xmin, xmax, ymin, ymax parameters
            object_semantic: the type is str, this is object label, if you decide to do action "bottle", then this function will return the square of the bottle
        '''
        return self.objects_semantic_dict[semantic]
    



    
    
if __name__ == '__main__':
    rospy.init_node('semantic_dfa')
    SMDFA = Semantic_Dfa()
    rospy.spin()
