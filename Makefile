serve:
	hugo server --disableFastRender -w

deploy:
	hugo
	sh deployrsync.sh
