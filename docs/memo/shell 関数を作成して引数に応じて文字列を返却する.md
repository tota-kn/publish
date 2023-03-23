```sh
function get_animal_cry() {  
  case $1 in  
    "dog" ) echo "/bow" ;;  
    "cat" ) echo "/miao" ;;  
  esac
}

animal_cry="$(get_animal_cry dog)"
echo animal_cry # dog
```