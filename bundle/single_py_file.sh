#!/usr/bin/env bash
app_name="wistia_downloader.py";
dir_path=$(dirname $(realpath $0));
deploy_path="$dir_path/../deploy"
src_path="$dir_path/../src"
mkdir -p $deploy_path;
echo "wrapping python files in a single one";
cd $src_path;
zip "$deploy_path/$app_name.zip" *.py;
echo '#!/usr/bin/env python3' | cat - "$deploy_path/$app_name.zip" > "$deploy_path/$app_name";
chmod a+x "$deploy_path/$app_name";
rm "$deploy_path/$app_name.zip";
echo "wrapping finished! Output file: $app_name"; 
