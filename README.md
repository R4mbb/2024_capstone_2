
# 프로젝트 - 1. AWS 환경 구축하기
lambda_docker_test 레포지토리에서는 학습시킨 AI 모델을 AWS 서비스를 이용해 구축하는 방법을 설명하고 있습니다.

※ 사용되는 AWS 서비스 : S3, ECR, EC2, Lambda, IAM

### AWS Architecture
![aws 아키텍쳐 수정본 배경 흰색](https://github.com/user-attachments/assets/f0b2e589-ebf8-47ce-83a4-cb14d3855006)

### EC2 생성
EC2 인스턴스를 생성합니다. (저희 팀은 t2.xlarge 사용)  
보안그룹(인바운드) - 8000포트 허용  
보안그룹(아웃바운드)- 모두 허용

### S3 버킷 생성
서로 다른 2개의 버킷을 생성합니다. (권한 : 모든 퍼블릭 차단)

첫번째 버킷 : AI로 악성여부를 검사할 파일을 저장합니다.  
두번째 버킷 : 검사 결과에 따라 파일을 저장합니다. (최종 배포파일 저장)
- 정상 파일일 경우 : 파일 저장 O
- 악성 파일일 경우 : 파일 저장 X

### ECR 레포지토리 생성 및 이미지 Push
ECR 서비스에서 프라이빗 레포지토리를 생성해줍니다.
```
git clone https://github.com/jinsu9758/lambda_docker_test.git

cd lambda_docker_test

aws ecr get-login-password --region [리전] | docker login --username AWS --password-stdin [사용자id].dkr.ecr.[리전].amazonaws.com

docker build --no-cache -t [ECR 레포지토리 이름] .

docker tag [ECR 레포지토리 이름]:latest [사용자id].dkr.ecr.[리전].amazonaws.com/[ECR 레포지토리 이름]:latest

docker push [사용자id].dkr.ecr.[리전].amazonaws.com/[ECR 레포지토리 이름]:latest
```
### Lamda 함수 설정
- 컨테이너 이미지로 람다 함수 생성 후, push한 ECR 이미지 선택
- 첫번째 버킷 (두번째 버킷 아님 주의!)과 트리거 설정 (Event : PUT)
- 역할 설정 >> lambda 실행 권한 + s3 권한
- 일반 구성
    - 메모리 : 1024 MB
    - 임시 스토리지 : 512 MB
    - 제한시간 : 1분 0초
※ 코드 동작 과정은 github 레포지토리를 통해 확인

### IAM 설정
- ec2(django)에서 S3 사용을 위한 사용자 생성 + 사용자 액세스키 발급
- 사용자 정책 설정 (아래 참고)
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObjectAcl",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:DeleteObject",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "[첫번째 버킷 arn]/*",
                "[첫번째 버킷 arn]",
                "[두번째 버킷 arn]/*",
                "[두번째 버킷 arn]"
            ]
        }
    ]
}
```





