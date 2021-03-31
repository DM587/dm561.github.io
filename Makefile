JEKYLL_VERSION=latest


build:
	bundle exec jekyll build

#publish:
#	bundle exec jekyll build --trace -d /home/marco/public_html/Teaching/AY2019-2020/DM561

clean:
	rm -fr /home/marco/WWWpublic/DM561/*

show:
	bundle show minima


dockupdate:
	docker run --rm \
		--volume="${PWD}:/srv/jekyll" \
		--volume="${PWD}/vendor/bundle:/usr/local/bundle" \
		-it jekyll/jekyll:${JEKYLL_VERSION} \
		bundle update

dockbuild:
	docker run --rm \
		--volume="${PWD}:/srv/jekyll" \
		--volume="${PWD}/vendor/bundle:/usr/local/bundle" \
		-it jekyll/jekyll:${JEKYLL_VERSION} \
		jekyll build --trace



dockserve:
	docker run --name dm561 \
		--volume="${PWD}:/srv/jekyll" \
		--volume="${PWD}/vendor/bundle:/usr/local/bundle" \
		-p 4000:4000 \
		-it jekyll/jekyll:${JEKYLL_VERSION} \
		jekyll serve --watch #--drafts
