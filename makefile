
install :
	pip install mujoco
	pip install xmltodict
	mamba install pyhull numpy-stl
	mamba install solidpython
	pip install glfw


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
	python mujoco_viewer.py --mjcf=4-bar.xml

carport :
	python carport.py
#	python build_3D.py; openscad example.scad


yy:
	python reader.py --urdf 1.urdf


xx:
	python essai.py
