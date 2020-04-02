import pymysql
from flask import jsonify


def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(
        user="root",
        password="111111",
        db="go",
        charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def get_data():
    sql = """select education from crawofzhenai"""
    res = query(sql)
    return res


def sort_data(data):
    sort = ['高中及以下', '中专', '大专', '大学本科', '硕士', '博士']
    lis = []
    senior = 0
    technical = 0
    junior = 0
    college = 0
    master = 0
    doctor = 0

    for i in data:
        if i[0] in sort:
            if i[0] == sort[0]:
                senior += 1
            elif i[0] == sort[1]:
                technical += 1
            elif i[0] == sort[2]:
                junior += 1
            elif i[0] == sort[3]:
                college += 1
            elif i[0] == sort[4]:
                master += 1
            elif i[0] == sort[5]:
                doctor += 1

    lis.append(senior)
    lis.append(technical)
    lis.append(junior)
    lis.append(college)
    lis.append(master)
    lis.append(doctor)
    return jsonify({"sort": sort, "lis": lis})


def get_l_data():
    sql = """select age, gender from crawofzhenai"""
    res = query(sql)
    return res


def age_data(data):
    age_man_20 = 0
    age_man_35 = 0
    age_man_50 = 0
    age_man_65 = 0
    age_man_other = 0
    age_wom_20 = 0
    age_wom_35 = 0
    age_wom_50 = 0
    age_wom_65 = 0
    age_wom_other = 0
    lis_man = []
    lis_wom = []
    for i in data:
        d = i[0]
        sex = i[1]
        if len(d) != 3:
            pass
        else:
            try:
                num = eval(d[:2])
                if num <= 20:
                    if sex == '男士':
                        age_man_20 += 1
                    else:
                        age_wom_20 += 1
                elif num <= 35:
                    if sex == '男士':
                        age_man_35 += 1
                    else:
                        age_wom_35 += 1
                elif num <= 50:
                    if sex == '男士':
                        age_man_50 += 1
                    else:
                        age_wom_50 += 1
                elif num <= 65:
                    if sex == '男士':
                        age_man_65 += 1
                    else:
                        age_wom_65 += 1
                else:
                    if sex == '男士':
                        age_man_other += 1
                    else:
                        age_wom_other += 1

            except TypeError:
                print("error", d[:2])
    name = ['20岁以下', '20-35岁', '35-50岁', '50-65岁', '65岁以上']
    lis_man.append(age_man_20)
    lis_man.append(age_man_35)
    lis_man.append(age_man_50)
    lis_man.append(age_man_65)
    lis_man.append(age_man_other)

    lis_wom.append(age_wom_20)
    lis_wom.append(age_wom_35)
    lis_wom.append(age_wom_50)
    lis_wom.append(age_wom_65)
    lis_wom.append(age_wom_other)
    return jsonify({"name": name, "lis_man": lis_man, "lis_wom": lis_wom})


def get_r_data():
    sql = """select income from crawofzhenai"""
    res = query(sql)
    return res


def income_data(data):
    sal_3k_ = 0
    sal_3k_5k = 0
    sal_5k_8k = 0
    sal_8k_12k = 0
    sal_12k_20k = 0
    sal_20_50k = 0
    sal_50k_ = 0
    lis = []
    for i in data:
        d = i[0][4:]

        if d == '3千以下':
            sal_3k_ += 1
        elif d == '3-5千':
            sal_3k_5k += 1
        elif d == '5-8千':
            sal_5k_8k += 1
        elif d == '8千-1.2万':
            sal_8k_12k += 1
        elif d == '1.2-2万':
            sal_12k_20k += 1
        elif d == '2-5万':
            sal_20_50k += 1
        elif d == '5万以上':
            sal_50k_ += 1
        else:
            print(type(d))

    name = ['3千以下', '3-5千', '5-8千', '8千-1.2万', '1.2-2万', '2-5万', '5万以上']

    lis.append({'value': sal_3k_, 'name': '3千以下'})
    lis.append({'value': sal_3k_5k, 'name': '3-5千'})
    lis.append({'value': sal_5k_8k, 'name': '5-8千'})
    lis.append({'value': sal_8k_12k, 'name': '8千-1.2万'})
    lis.append({'value': sal_12k_20k, 'name': '1.2-2万'})
    lis.append({'value': sal_20_50k, 'name': '2-5万'})
    lis.append({'value': sal_50k_, 'name': '5万以上'})

    return jsonify({'data': lis, 'name': name})

    # lis.append(sal_3k_)
    # lis.append(sal_3k_5k)
    # lis.append(sal_5k_8k)
    # lis.append(sal_8k_12k)
    # lis.append(sal_12k_20k)
    # lis.append(sal_20_50k)
    # lis.append(sal_50k_)
    # return jsonify({"name": name, "lis": lis})


if __name__ == '__main__':
    # res = get_data()
    # sort_data(res)

    print(get_r_data())
