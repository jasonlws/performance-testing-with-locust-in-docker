docker-compose -f locust.yml --scale master=1 --scale worker=1 --scale nginx=1 up
docker-compose -f locust.yml down -v