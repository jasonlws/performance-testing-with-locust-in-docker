docker-compose -f performance-testing-locust.yml up --scale master=1 --scale worker=1 --scale nginx=1
docker-compose -f performance-testing-locust.yml down -v