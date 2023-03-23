RELATIVE_ROOT="`dirname $0`/.."
ROOT=`realpath "$RELATIVE_ROOT"`
DOCS="${ROOT}/docs"

# 画像の用意
mkdir "$DOCS/attachments"
grep -rE "!\[\[.*.(png|jpg|jpeg|pdf)\]\]" "$DOCS/" | grep -oE "!\[\[.*.(png|jpg|jpeg|pdf)\]\]" | sed -e 's/!\[\[//g' -e  's/\]\]//g' | while read line
do
  cp "/Users/yt/Library/CloudStorage/Dropbox/obsidian_PRIVATE/_attachments/$line" "$DOCS/attachments/$line"
done