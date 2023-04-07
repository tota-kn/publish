# flutter flavorで環境判別
今は[[flutter Dart-defineで環境判別]]のほうがよさげ

## 共通
以下のファイルを作成
`lib/flavor.dart`
```dart
enum FlavorType {
  dev, // 開発環境
  cus, // 検収環境
  prd, // 本番環境
}

class Flavor {
  static Flavor _instance = Flavor._internal(FlavorType.dev);
  final FlavorType type;

  factory Flavor() {
    return _instance;
  }

  factory Flavor.initialize(FlavorType type) {
    _instance = Flavor._internal(type);
    return _instance;
  }

  Flavor._internal(this.type);
}

```

`lib/main/main_dev.dart`
```dart
import 'package:app/flavor.dart';
import 'package:app/main.dart';

void main() {
  Flavor.initialize(FlavorType.dev);
  startApp();
}
```

`lib/main/main_cus.dart`
```dart
import 'package:app/flavor.dart';
import 'package:app/main.dart';

void main() {
  Flavor.initialize(FlavorType.cus);
  startApp();
}
```

`lib/main/main_prd.dart`
```dart
import 'package:app/flavor.dart';
import 'package:app/main.dart';

void main() {
  Flavor.initialize(FlavorType.prd);
  startApp();
}
```

`lib/main.dart`
```dart
Future<void> startApp() async {
  runApp(<任意の画面Widget>);
}

```

起動設定を作成
![[Pasted image 20220112221707.png]]

## Android
以下を追記
`android/app/build.gradle`
```gradle
android {
    flavorDimensions "server"
    productFlavors {
        dev {
            dimension "server"
            applicationIdSuffix ".dev"
        }
        cus {
            dimension "server"
            applicationIdSuffix ".cus"
        }
        prd {
            dimension "server"
        }
    }
}
```


## iOS
https://medium.com/flutter-jp/flavor-b952f2d05b5d


---
## Related Notes
- 

## References
- 

## Tags
- `#flutter` 