serve:
	hugo server --disableFastRender -w

deploy:
	hugo
	sh deployhg.sh
