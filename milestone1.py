{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "milestone1.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPyLtsn5IasH0hvSQaTwWKE",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kathannah/milestone1.py/blob/main/milestone1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "styUil2Hkcr7",
        "outputId": "81abaf2a-1d7f-490e-919c-32fd847628f2"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2, '60.91954022988506')"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ],
      "source": [
        "def gc_content(dna_list):\n",
        "    \n",
        "    c = 'C'\n",
        "    g = 'G'\n",
        "    \n",
        "    highest_gc = ''\n",
        "    GC_holder = ''\n",
        "    GC_content = []\n",
        "    \n",
        "    for i in range (len(dna_list)):      #for each string in gc_content,add the gc value to GC_content\n",
        "        length = len(dna_list[i])\n",
        "        count_c = float(dna_list[i].count(c))\n",
        "        count_g = float(dna_list[i].count(g))\n",
        "        GC_holder = str(((count_c + count_g)/length)*100)\n",
        "        GC_content.append(GC_holder)\n",
        "                       \n",
        "    \n",
        "    for i in range(len(GC_content)):         #the highest gc value is put in the variable highest_gc\n",
        "        if GC_content[i] > GC_content[i-1]:\n",
        "            highest_gc = (i, GC_content[i])\n",
        "            \n",
        "    return (highest_gc)\n",
        "\n",
        "gc_content([\"CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG\",\n",
        "     \"CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC\",\n",
        "     \"CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT\"])"
      ]
    }
  ]
}