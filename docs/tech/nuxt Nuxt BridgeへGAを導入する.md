# nuxt Nuxt BridgeへGAを導入する
`package.json`
```
npm install @types/gtag.js
```

`nuxt.config.js`
```js
export default defineNuxtConfig({
	head: {
		script: [
			{ src: 'https://www.googletagmanager.com/gtag/js?	id=XXXXXXXX'},
      		{innerHTML: 'window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag("js", new Date());gtag("config", "XXXXXXXXXXXX");'}
		]
	}
})
```

@types/windows-module.d.ts
```
import {Gtag} from "@types/gtag.js"
export{}

declare global {
    interface Window {
        gtag: Gtag
    }
}
```

以下を実行でクリックイベント送信
```ts
   gtag('event', eventAction, {
       event_category
	   event_label
	   value
    })
```

----
### Related Notes
- 

### References
- 

### Tags
- 