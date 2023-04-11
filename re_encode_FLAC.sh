mkdir -p tmp
for filename in *.flac; do 
echo $filename
mv "$filename" "tmp/$filename"

sox "tmp/$filename" "$filename"
done
