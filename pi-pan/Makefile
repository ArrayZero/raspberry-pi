#
# (c) OpenElectrons.com 
# Not for public consumption.
# For internal use only.
#
# History:
# Date     Author       Changes
# 02/03/14 Deepak       Created to make distribution of Pi-Pan code.
#


FILES= check-pan.py \
	check-pilight.py \
	check-tilt.py \
	demo-pi-pan.py \
	demo-with-pilight.py \
	install-pilight.bash \
	install-pi-pan.bash \
	neutral_servo.py \
	pano_with_light.py \
	pan-test.py \
	pictures-color.py \
	pilight.py \
	pipan.py \
	revision.py \
	servoblaster.sh \
	servod \
	take_pano.py \
	uninstall-pilight.bash \
	uninstall-pi-pan.bash \
	video-with-pilight.py \
	OpenElectrons_i2c.py \
	README

PI_PAN_GZ=pi-pan.tar.gz

$(PI_PAN_GZ): $(FILES) 
	tar -zcvf $(PI_PAN_GZ) $(FILES)

distro:	$(PI_PAN_GZ)

clean:
	rm -f $(PI_PAN_GZ)


