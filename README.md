docker-compose -f locust.yml up --scala master=1 --scala worker=1 --scala nginx=1
docker-compose -f locust.yml down -v