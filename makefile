
startxx :
	python py2xml.py
#	python convert_mjcf.py

start:
#	python test_mujoco.py --xml 2.xml
#	python mujoco_viewer.py --mjcf=2.xml
	python mujoco_viewer.py --py=example.py

yy:
	python reader.py --urdf 1.urdf


xx:
	python essai.py
