from database.DB_connect import DBConnect
from model.team import Team


class DAO():

    @staticmethod
    def getAllAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year 
            from teams t 
            where year>=1980"""
        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllSquadreAnno(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                from teams t 
                where year=%s"""
        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(Team(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSalarioSquadra(anno, codSquadra):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t.teamCode, t.name, sum(s.salary) as salario, t.ID
        from teams t , salaries s
        where t.year=s.`year` and t.teamCode =s.teamCode and t.`year` =%s and t.teamCode=%s
        group by t.teamCode, t.name"""
        cursor.execute(query, (anno, codSquadra))

        for row in cursor:
            result.append((row["teamCode"], row["name"], row["salario"], row["ID"]))
        cursor.close()
        conn.close()
        return result
