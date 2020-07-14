find . -name "*.md" | while IFS= read -r pathname; do
    base=$(basename "$pathname"); name=${base%.*}; ext=${base##*.}
    pandoc "$pathname" -o "${name}.html"
done
