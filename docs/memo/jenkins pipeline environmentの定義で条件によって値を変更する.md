 三項演算子、または関数を利用する

引用：[Conditional environment variables in Jenkins Declarative Pipeline - Stack Overflow](https://stackoverflow.com/questions/44007034/conditional-environment-variables-in-jenkins-declarative-pipeline)

```groovy
pipeline {
    agent any
    environment {
        ENV_NAME = "${env.BRANCH_NAME == "develop" ? "staging" : "production"}"
    }
}
```

```groovy
pipeline {
        agent any
        environment {
           ENV_NAME = getEnvName(env.BRANCH_NAME)
        }
    }

// ...

def getEnvName(branchName) {
    if("int".equals(branchName)) {
        return "int";
    } else if ("production".equals(branchName)) {
        return "prod";
    } else {
        return "dev";
    }
}
```