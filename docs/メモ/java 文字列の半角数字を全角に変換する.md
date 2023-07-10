# java 文字列の半角数字を全角に変換する
```java
    /**
     * <pre>
     * 半角数字⇒全角数字への変換
     * </pre>
     * @param  str 変換対象文字列
     * @return 変換後文字列
     */
    public static String convertNumHalfToFull(String str) {
        if(str == null){ return null; }

        StringBuilder sb = new StringBuilder(str);
        for (int i = 0; i < sb.length(); i++) {
            int c = sb.charAt(i);
            if (c >= 0x30 && c <= 0x39) {
                sb.setCharAt(i, (char) (c + 0xFEE0));
            }
        }
        return sb.toString();
    }
```

----
### Related Notes
- 

### References
- 

### Tags
- 