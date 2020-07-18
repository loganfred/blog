find . -name "*.md" | while IFS= read -r pathname; do
    base=$(basename "$pathname"); name=${base%.*}; ext=${base##*.}
    pandoc "$pathname" -so "${name}.html"
done
