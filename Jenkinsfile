pipeline {

  agent any 
  
  stages {
  
    stage("build") {
      
      steps {
        sh 'python -m py_compile char.py num.py'
        stash(name: 'compiled-results', includes:'*.py*')
        }
     }  
  }
}
