
build:
	bundle exec jekyll build

publish:
	bundle exec jekyll build --trace -d /home/marco/WWWpublic/DM561
	# cp -fr _site/* /home/marco/WWWpublic/Blog

clean:
	rm -fr /home/marco/WWWpublic/DM561/*

show:
	bundle show minima
