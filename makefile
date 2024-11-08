
startx :
	python py2xml.py
#	python convert_mjcf.py

commit :
	git commit -a -m xxx
	git push

start :
#	python test_mujoco.py --xml 2.xml
#	python mujoco_viewer.py --mjcf=toto.xml
#	python mujoco_viewer.py --py=example.py
	python carport.py
#	python build_3D.py; openscad example.scad


yy:
	python reader.py --urdf 1.urdf


xx:
	python essai.py
