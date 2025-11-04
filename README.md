# python-misc
The best way to learn Python is to write it. There's always odd jobs around the home and office that can be quickly done with a Python script. Here is my collection.

## instagram-html.py
Takes the HTML output of Instagram's follower (or following) data export, and converts it into a .csv (from there you can open it in a spreadsheet etc.)

## instagram-json.py
Same as the above, for JSON output. Note some manual preprocessing that needs to be done beforehand:

1. The followers file has a `_1` suffix, manually remove this

2. The following file has a:

```
{
  "relationships_following":
```

That is not in the followers file. Copy-paste this exact text and append it to the head of the followers file. Then add a matching `}` at the tail.

