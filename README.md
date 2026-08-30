## Capital Guesser
Small geography game. You get a satelite image from the [Copernicus Data Space Ecosystem](https://documentation.dataspace.copernicus.eu/Applications/Browser.html). A random satelite picture of a capital is chosen per round, and a guess of the capital and country can be made. Per round, a total of 1 point can be achieved, 0.5 for country and capital each.
## Prerequisites
Packages needed are [pystac](https://pystac.readthedocs.io/en/stable/), [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/) and [streamlit](https://streamlit.io/).
## Use
To use, run ```main.py```. This will open a streamlit page on port ```8501``` (depending on streamlit configuration) locally. A new game can be started by clicking ```New Game``` (resets points). As the satellite images sometimes are corrupted (there is no check for this, yet), clicking ```Reload Image``` will load a new image without affecting the points. From the dropdown menues, a capital and a country can be chosen. When submitted, the points will be updated. Click ```Help``` for this explanation.
## Note
Copernicus data are available corresponding to the [Legal notice on the use of Copernicus Sentinel Data and Service Information](https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice).
## To-Do
Higher resultion pictures should be available for use. A filter should be included to automatically search a new satelite image if e.g. to many clouds are visible. Same goes for images where less than a certain fraction of the image is actually showing the city.
