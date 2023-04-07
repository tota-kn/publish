# js S3のtxtファイルの中身を読み取る
```ts
import * as AWS from 'aws-sdk'

const s3Client = new AWS.S3()
const result = await new Promise((resolve, reject) =>{
        s3Client.getObject(
          {
            Bucket: "bucket-name",
            Key: "directory/path.txt"
          },
          (err, response) => {
            if(err) { reject(err); }
            else { resolve(response.Body.toString('utf-8')); }
          }
        )
      })
console.log(result)
```

## 参考
[AWS S3のバケットからテキストファイルを取り出そうとしてハマった件 | KZ-WORKS](https://kz-works.blogspot.com/2018/05/aws-s3-get-object-body.html)