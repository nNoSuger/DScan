# DScan

## Description

A subdomain blasting tool that is easy to use, easy to use, and has high scanning efficiency

## Merit

1.File saving is automatic

2.Multi-modular, can be maintained and upgraded later, with scalability

3.The scan status code is displayed

4.You can use the default dictionary and default threat factor, just enter the URL you want to scan, and it's easy to get started

## Usage

-h	Help Documentation

-u	'url'	Destination URL

-f	'path'	Dictionary Path By default, this project comes with a dictionary

-t	'thread'	The threat factor defaults to 10

The scan starts

```
Use the default dictionary as well as the default threat factor
python main.py -u "baidu.com"
```

```
Use the specified dictionary and specify the threat factor
python main.py -u "baidu.com" -f "110w.txt" -t 5
```

Test



