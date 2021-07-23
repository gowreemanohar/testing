{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# importing libraries\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: matplot in c:\\users\\mano\\anaconda3\\lib\\site-packages (0.1.9)\n",
      "Requirement already satisfied: pyloco>=0.0.134 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from matplot) (0.0.139)\n",
      "Requirement already satisfied: matplotlib>=3.1.1 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from matplot) (3.3.2)\n",
      "Requirement already satisfied: SimpleWebSocketServer in c:\\users\\mano\\anaconda3\\lib\\site-packages (from pyloco>=0.0.134->matplot) (0.1.1)\n",
      "Requirement already satisfied: typing in c:\\users\\mano\\anaconda3\\lib\\site-packages (from pyloco>=0.0.134->matplot) (3.7.4.3)\n"
     ]
    },
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'pyplot' from 'matplot' (C:\\Users\\mano\\anaconda3\\lib\\site-packages\\matplot\\__init__.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-bec02ccee866>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mget_ipython\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msystem\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'pip install matplot'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mmatplot\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpyplot\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mImportError\u001b[0m: cannot import name 'pyplot' from 'matplot' (C:\\Users\\mano\\anaconda3\\lib\\site-packages\\matplot\\__init__.py)"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: twine in c:\\users\\mano\\anaconda3\\lib\\site-packages (from pyloco>=0.0.134->matplot) (3.3.0)\n",
      "Requirement already satisfied: websocket-client in c:\\users\\mano\\anaconda3\\lib\\site-packages (from pyloco>=0.0.134->matplot) (0.57.0)\n",
      "Requirement already satisfied: ushlex in c:\\users\\mano\\anaconda3\\lib\\site-packages (from pyloco>=0.0.134->matplot) (0.99.1)\n",
      "Requirement already satisfied: python-dateutil>=2.1 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.1->matplot) (2.8.1)\n",
      "Requirement already satisfied: numpy>=1.15 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.1->matplot) (1.19.2)\n",
      "Requirement already satisfied: certifi>=2020.06.20 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.1->matplot) (2020.6.20)\n",
      "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.1->matplot) (2.4.7)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.1->matplot) (0.10.0)\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.1->matplot) (1.3.0)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.1->matplot) (8.0.1)\n",
      "Requirement already satisfied: pkginfo>=1.4.2 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from twine->pyloco>=0.0.134->matplot) (1.6.1)\n",
      "Requirement already satisfied: tqdm>=4.14 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from twine->pyloco>=0.0.134->matplot) (4.50.2)\n",
      "Requirement already satisfied: requests-toolbelt!=0.9.0,>=0.8.0 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from twine->pyloco>=0.0.134->matplot) (0.9.1)\n",
      "Requirement already satisfied: rfc3986>=1.4.0 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from twine->pyloco>=0.0.134->matplot) (1.4.0)\n",
      "Requirement already satisfied: readme-renderer>=21.0 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from twine->pyloco>=0.0.134->matplot) (29.0)\n",
      "Requirement already satisfied: requests>=2.20 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from twine->pyloco>=0.0.134->matplot) (2.24.0)\n",
      "Requirement already satisfied: setuptools>=0.7.0 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from twine->pyloco>=0.0.134->matplot) (50.3.1.post20201107)\n",
      "Requirement already satisfied: keyring>=15.1 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from twine->pyloco>=0.0.134->matplot) (21.4.0)\n",
      "Requirement already satisfied: colorama>=0.4.3 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from twine->pyloco>=0.0.134->matplot) (0.4.4)\n",
      "Requirement already satisfied: six in c:\\users\\mano\\anaconda3\\lib\\site-packages (from websocket-client->pyloco>=0.0.134->matplot) (1.15.0)\n",
      "Requirement already satisfied: bleach>=2.1.0 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from readme-renderer>=21.0->twine->pyloco>=0.0.134->matplot) (3.2.1)\n",
      "Requirement already satisfied: Pygments>=2.5.1 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from readme-renderer>=21.0->twine->pyloco>=0.0.134->matplot) (2.7.2)\n",
      "Requirement already satisfied: docutils>=0.13.1 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from readme-renderer>=21.0->twine->pyloco>=0.0.134->matplot) (0.16)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from requests>=2.20->twine->pyloco>=0.0.134->matplot) (2.10)\n",
      "Requirement already satisfied: chardet<4,>=3.0.2 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from requests>=2.20->twine->pyloco>=0.0.134->matplot) (3.0.4)\n",
      "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\\users\\mano\\anaconda3\\lib\\site-packages (from requests>=2.20->twine->pyloco>=0.0.134->matplot) (1.25.11)\n",
      "Requirement already satisfied: pywin32-ctypes!=0.1.0,!=0.1.1; sys_platform == \"win32\" in c:\\users\\mano\\anaconda3\\lib\\site-packages (from keyring>=15.1->twine->pyloco>=0.0.134->matplot) (0.2.0)\n",
      "Requirement already satisfied: packaging in c:\\users\\mano\\anaconda3\\lib\\site-packages (from bleach>=2.1.0->readme-renderer>=21.0->twine->pyloco>=0.0.134->matplot) (20.4)\n",
      "Requirement already satisfied: webencodings in c:\\users\\mano\\anaconda3\\lib\\site-packages (from bleach>=2.1.0->readme-renderer>=21.0->twine->pyloco>=0.0.134->matplot) (0.5.1)\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "!pip install matplot\n",
    "from matplot import pyplot as plt \n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# importing datas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
