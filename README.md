<div id="top"></div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
This project will allow you to crawl information from the GitHub search engine to obtain the urls of the first search page. On the other hand, if you search for repositories, it will also give you the author and the languages used for each of them.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With
This project uses the following language:
* [Python](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started
In this section you will find what you need to set up the project locally. To get a local copy up and running follow these simple example steps.

### Prerequisites
You need Python 3 and install the requirements that are in the file requirements.txt .
* npm
  ```sh
  npm install requests~=2.27.1
  npm install beautifulsoup4~=4.11.1
  npm install pytest~=7.1.2
  ```
  
### Installation
1. Download Python 3
2. Clone the repo
3. Install NPM packages
   ````sh
   pip install -r requirements.txt


<!-- USAGE EXAMPLES -->
## Usage
In order to see the correct operation of the project, you have to enter the data in input_data file. The output will be printed by terminal, although in future versions, it could be added to an output file. This last part depends more on the context of use.

Example 1

- Input
````sh
{
  "keywords": [
    "openstack",
    "nova",
    "css"
  ],
  "proxies": [
    "194.126.37.94:8080",
    "13.78.125.167:8080"
  ],
  "type": "Repositories"
}
````
- Output
````sh
[
  {
    "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage",
    "extra": {
      "owner": "atuldjadhav",
      "language_stats": {
        "CSS": 52,
        "JavaScript": 47.2,
        "HTML": 0.8
      }
    }
  }
]
````

<p align="right">(<a href="#top">back to top</a>)</p>


Example 2

- Input
````sh
{
  "keywords": [
    "python",
    "django-rest-framework",
    "jwt"
  ],
  "proxies": [
    "194.126.37.94:8080",
    "13.78.125.167:8080"
  ],
  "type": "Issues"
}
````
- Output
````sh
[
  {
    "url": "https://github.com/GetBlimp/django-rest-framework-jwt"
  },
  {
    "url": "https://github.com/lock8/django-rest-framework-jwt-refresh-token"
  },
  {
    "url": "https://github.com/City-of-Helsinki/tunnistamo"
  },
  {
    "url": "https://github.com/chessbr/rest-jwt-permission"
  },
  {
    "url": "https://github.com/rishabhiitbhu/djangular"
  },
  {
    "url": "https://github.com/vaibhavkollipara/ChatroomApi"
  }
]
````

_For more examples and information, please refer to the [Documentation](https://confluence.rdpnts.com/display/IKB/Python+developer+technical+task)