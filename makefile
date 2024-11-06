
startx :
	python py2xml.py
#	python convert_mjcf.py

commit :
	git commit -a -m xxx
	git push

start :
#	python test_mujoco.py --xml 2.xml
#	python mujoco_viewer.py --mjcf=toto.xml
	python mujoco_viewer.py --py=example.py

yy:
	python reader.py --urdf 1.urdf


xx:
	python essai.py
