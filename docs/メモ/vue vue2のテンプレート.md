# vue vue2のテンプレート
```vue
<template>
	<div> Hello Vue!</div>
</template>

<script>
import Hoge from '@/components/hoge/Hoge';
export default {
	name: 'HelloVue',
	components: {
		'hoge': Hoge
	},
	
	data(){
		return{
			key: 'value'
		}
	},
	
	computed: {},
	mounted() {},
	methods: {
		aaa() {}
	}
},
</script>



```

----
### Related Notes
- 

### References
- 

### Tags
- 