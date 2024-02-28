build:
	rm -rf build
	rm -rf duka_smartfan_sdk.egg-info
	rm -rf dist
	python setup.py sdist bdist_wheel

clean:
	rm -rf build
	rm -rf duka_smartfan_sdk.egg-info
	rm -rf dist

upload:
	twine upload --repository pypi dist/*

