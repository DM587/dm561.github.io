
build:
	bundle exec jekyll build

publish:
	bundle exec jekyll build --trace -d /home/marco/public_html/Teaching/AY2019-2020/DM561

clean:
	rm -fr /home/marco/WWWpublic/DM561/*

show:
	bundle show minima
