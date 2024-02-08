node(){
    def commit_hash = null
    stage('SCM Checkout'){
        checkout scmGit(branches: [[name: "*/${env.BRANCH_NAME}"]], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkins', url: 'git@github.com:roshanakhade/gcp-terraform-modules.git']])
        commit_hash = sh(returnStdout: true, script: 'git rev-parse --short HEAD').toString().trim()
    }
    stage('Docker Build and Push'){
        sh """az login --identity
        az acr login --name nginxdemoprominent
        docker build -t nginxdemoprominent.azurecr.io/nginx:${commit_hash} docker
        docker push nginxdemoprominent.azurecr.io/nginx:${commit_hash}"""
    }
    stage('Kubectl deploy') {
        withCredentials([file(credentialsId: 'kubeconfig', variable: 'kubeconfig')]) {
            sh '''cp -f ${kubeconfig} ~/.kube/config
            sed -i 's/<IMAGE_TAG>/''' + commit_hash + '''/g' k8s-demo-manifests/deployment.yaml
            kubectl apply -f k8s-demo-manifests -n demo'''
        }
    }
}