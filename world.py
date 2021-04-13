import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
class WORLD:
	# defines a constructor for this class
	def __init__(self):
		# Creates an object, physicsClient, which handles the physics, and draws the results to a Graphical User Interface (GUI).
		# self.physicsClient = p.connect(p.GUI)
		# p.setAdditionalSearchPath(pybullet_data.getDataPath())
		
		# Load a world
		# p.loadSDF("world.sdf")
		# Adding a floor
		self.planeId = p.loadURDF("plane.urdf")
		#Simulate the box
		p.loadSDF("boxes.sdf")
		

		
