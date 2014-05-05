This is made for Mac/Linux and manage and start scripts are hard wired to use virtualenv called pyve

# Setup
````sh
git clone https://github.com/goodes/djanjo-simple-static.git
cd djanjo-simple-static
virtualenv --no-site-packages pyve
./pyve/bin/pip install -r requirements.txt
````
#Configuration
Place your content in staticsite/pages/templates/

#Run
````sh
./start.sh
````
