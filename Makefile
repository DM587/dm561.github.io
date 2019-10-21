
build:
	bundle exec jekyll build

publish:
	bundle exec jekyll build --trace -d /home/marco/public_html/Teaching/AY2018-2019/DM561
	# cp -fr _site/* /home/marco/WWWpublic/Blog

clean:
	rm -fr /home/marco/WWWpublic/DM561/*

show:
	bundle show minima
