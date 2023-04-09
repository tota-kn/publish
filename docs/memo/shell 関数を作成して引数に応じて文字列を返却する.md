# shell 関数を作成して引数に応じて文字列を返却する
```sh
function get_animal_cry() {  
  case $1 in  
    "dog" ) echo "/bow" ;;  
    "cat" ) echo "/miao" ;;  
  esac
}

animal_cry="$(get_animal_cry dog)"
echo animal_cry ## dog
```