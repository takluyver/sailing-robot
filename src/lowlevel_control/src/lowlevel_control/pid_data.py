import rospy


class PID_Data:
    def __init__(self):
        self.tack_rudder = 0.
        self.update_sailing_state = ''
        self.goal_heading = 0.
        self.heading = 0.

    def update_goal_heading(self, msg):
        """
        Update goal heading data from higher level controller for PID controller
        :param msg:
        """
        self.goal_heading = msg.data

    def update_sailing_state(self, msg):

        self.update_sailing_state = msg.data

    def update_heading(self, msg):
        """
        Get continuous update of current heading from sensors
        :param msg:

        """
        self.heading = msg.data

    def update_tack_rudder(self,msg):
        self.tack_rudder = msg.data
