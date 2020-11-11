pipeline {

  agent any 
  
  stages {
  
    stage("build") {
      
      steps {
        //Runs python file to compile results
        sh 'python -m py_compile char.py num.py'
        //create a compile folder for joined py folder
        stash(name: 'compiled-results', includes:'*.py*')
        }
     }  
  }
}
