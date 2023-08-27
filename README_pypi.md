# Duplicate Image Finder (difPy)

**Tired of going through all images in a folder and comparing them manually to check if they are duplicates?**

The Duplicate Image Finder (difPy) Python package **automates** this task for you!

Read more on how the algorithm of difPy works in my Medium article **[Finding Duplicate Images with Python](https://towardsdatascience.com/finding-duplicate-images-with-python-71c04ec8051)**.

For a **detailed usage guide**, please view the official **[difPy Usage Documentation](https://difpy.readthedocs.io/)**.

**Try the [difPy Web App](https://difpy.app/)!**

-------

## Description
difPy searches for images in **one or more different folders**, compares the images it found and checks whether these are duplicates. It then outputs the **image files classified as duplicates** as well as the **images having the lowest resolutions**, so you know which of the duplicate images are safe to be deleted. You can then either delete them manually, or let difPy delete them for you.

difPy does not compare images based on their hashes. It compares them based on their tensors i. e. the image content - this allows difPy to **not only search for duplicate images, but also for similar images**.

## Basic Usage
To make difPy search for duplicates **within one folder**:

```python
from difPy import dif
search = dif("C:/Path/to/Folder/")
``` 
To search for duplicates **within multiple folders**:

```python
from difPy import dif
search = dif(["C:/Path/to/Folder_A/", "C:/Path/to/Folder_B/", "C:/Path/to/Folder_C/",...])
``` 
Folder paths can be specified as standalone Python strings, or within a list.

## Output
difPy returns various types of output that you may use depending on your use case: 

A **JSON formatted collection** of duplicates/similar images (i. e. **match groups**) that were found, where the keys are a **randomly generated unique id** for each image file:

```python
search.result

> Output:
{20220819171549 : {"location" : "C:/Path/to/Image/image1.jpg",
                   "matches" : {30270813251529 : "location": "C:/Path/to/Image/matched_image1.jpg",
                                                 "mse": 0.0},
                               {72214282557852 : "location": "C:/Path/to/Image/matched_image2.jpg",
                                                 "mse": 0.0},
                   ... }
 ...
}
``` 

A **list** of duplicates/similar images that have the **lowest quality** among match groups: 

```python
search.lower_quality

> Output:
["C:/Path/to/Image/duplicate_image1.jpg", 
 "C:/Path/to/Image/duplicate_image2.jpg", ...]
``` 
A **JSON formatted collection** with statistics on the completed difPy process:

```python
search.stats

> Output:
{"directory" : ("C:/Path/to/Folder_A/", "C:/Path/to/Folder_B/", ... ),
 "duration" : {"start_date" : "2023-02-15",
               "start_time" : "18:44:19",
               "end_date" : "2023-02-15",
               "end_time" : "18:44:38",
               "seconds_elapsed" : 18.6113},
 "fast_search" : True,
 "recursive" : True,
 "match_mse" : 0,
 "px_size" : 50,
 "files_searched" : 1032,
 "matches_found" : {"duplicates" : 52, 
                    "similar" : 0},
 "invalid_files" : {"count" : 4},
 "deleted_files" : {"count" : 0},
 "skipped_files" : {"count" : 0}}
```

## Additional Parameters
difPy supports the following parameters:

```python
dif(*directory, fast_search=True, recursive=True, similarity='duplicates', px_size=50, 
    move_to=None, limit_extensions=False, show_progress=True, show_output=False, 
    delete=False, silent_del=False, logs=False)
```

## CLI Usage
difPy can also be invoked through the CLI by using the following commands:

```python
python dif.py -D "C:/Path/to/Folder/"

python dif.py -D "C:/Path/to/Folder_A/" "C:/Path/to/Folder_B/" "C:/Path/to/Folder_C/"
```
It supports the following arguments:

```python
dif.py [-h] -D DIRECTORY [-Z OUTPUT_DIRECTORY] [-f {True,False}]
       [-r {True,False}] [-s SIMILARITY] [-px PX_SIZE] 
       [-mv MOVE_TO] [-le {True,False}] [-p {True,False}]
       [-o {True,False}] [-d {True,False}] [-sd {True,False}] 
       [-l {True,False}]
```

The output of difPy is then written to files and saved in the working directory, where "xxx" in the output filesnames is a unique timestamp:

```python
difPy_results_xxx.json
difPy_lower_quality_xxx.csv
difPy_stats_xxx.json
```

-------

For a **detailed usage guide**, please view the official **[difPy Usage Documentation](https://difpy.readthedocs.io/)**.