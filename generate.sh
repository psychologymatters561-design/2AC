#!/bin/bash

mkdir -p blog

# Common variables
WEB3FORMS_KEY="YOUR_WEB3FORMS_ACCESS_KEY"

# Extract the actual key from index.html if possible, but the prompt says "find it in index.html"
# Let's assume the user will replace it or we can grep it.
# Wait, I can just read index.html to find it.
