# flutter アプリ全体のフォントの設定
`pubspec.yaml`
```yaml
dependencies:
  flutter_localizations:
    sdk: flutter         
```
を追加し、
```dart
import 'package:flutter_localizations/flutter_localizations.dart';

const locale = Locale("ja", "JP");
return MaterialApp(
  locale: locale,
  localizationsDelegates: const [
    GlobalMaterialLocalizations.delegate,
    GlobalWidgetsLocalizations.delegate,
    GlobalCupertinoLocalizations.delegate,
  ],
  supportedLocales: const [
    locale,
  ],
);
```

---
## Related Notes
- 

## References
- https://qiita.com/najeira/items/dbf5663d1ed845fb1f51

## Tags
- `#flutter` 