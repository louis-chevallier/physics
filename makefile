
#cd .. ; git clone https://github.com/google-deepmind/mujoco_menagerie.git


models = $(wildcard ../mujoco_menagerie/*/*.xml)
$(warning $(models))

start :
	python mujoco_viewer.py --mjcf=car.xml

start3 :
	$(foreach i , $(models), python mujoco_viewer.py --mjcf=$i; )

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



start1 :
#	python test_mujoco.py --xml toto.xml
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
