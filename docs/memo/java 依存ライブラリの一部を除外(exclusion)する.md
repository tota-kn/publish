# java 依存ライブラリの一部を除外(exclusion)する
pom.xmlで`<exclusion>`タグを利用する

以下はhogeライブラリがfugaライブラリに依存してるが、fugaは利用したくない場合の例
```xml
<dependency>
    <groupId>hoge.org</groupId>
    <artifactId>hoge</artifactId>
    <version>1.0.0</version>
    <exclusions>
        <exclusion>
            <groupId>fuga.org</groupId>
            <artifactId>fuga</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

## 参考
- [Mavenのexclusionsタグを知らなかった… - Challenge Engineer Life !](https://kikutaro777.hatenablog.com/entry/2013/05/29/211405)