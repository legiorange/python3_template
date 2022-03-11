import json


def day_money_cont(mouth_money):
    pay_day = 21.75
    return mouth_money / pay_day


def hours_money_cont(mouth_money):
    pay_day = 21.75
    return mouth_money / (pay_day * 8)


def delay_hours_money_cont(mouth_money):
    pay_day = 21.75
    return (mouth_money / (pay_day * 8)) * 1.5


def rest_money_cont(mouth_money):
    pay_day = 21.75
    return (mouth_money / (pay_day * 8)) * 2


if __name__ == '__main__':
    # 计算脚本
    # 月薪
    mouth_money = 35000
    # 日工资= 月工资的收入/月薪天数

    day_money = day_money_cont(mouth_money)
    print("日薪:{}", day_money)
    # 小时工资=月薪的收入/(月计薪天数 21*8h)
    h_money = hours_money_cont(mouth_money)
    print("时薪:{}", h_money)

    #
    delay_hours_money = delay_hours_money_cont(mouth_money)
    print("工作日加班时薪:{}", delay_hours_money)

    # 休息日加班计算: 小时加班费用标准= 劳动合同规定的月工资标准/(月计薪天数21 75*8小时)*200%
    rest_day_money = rest_money_cont(mouth_money)
    print("休息日加班时薪:{}", rest_day_money)

    # 11月日新计算
    # 19、22、23、24、25、26、29、30 8天
    tem_11 = day_money * 8
    print("11月工作日加班计算:{}", tem_11)

    tem_11_hour = (1.5 * 4) + (9.6 - 8) + (9.7 - 8) + (9.7 - 8)
    print("11月工作日共计加班工时", tem_11_hour)
    tem_11_hour_money = 11 * delay_hours_money_cont(mouth_money)
    print("11月工作日共计加班工资", tem_11_hour_money)

    #    11月加班计算
    #     27、28
    tem_11_rest = rest_day_money * (9.5 * 2)
    print("11月非工作日加班计算:{}", tem_11_rest)
    print("共计:", tem_11 + tem_11_rest + tem_11_hour_money)
