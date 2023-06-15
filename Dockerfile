# Use this Dockerfile to test the Jekyll pages.
# Run it with:
#    docker run --rm -it -v $(pwd):/usr/src/app -p 4000:4000
FROM ruby

RUN gem install bundler

WORKDIR /usr/src/app

COPY Gemfile .

RUN bundle install

ENTRYPOINT ["/bin/bash"]
CMD ["-c", "bundle exec jekyll serve -H 0.0.0.0 --incremental"]
