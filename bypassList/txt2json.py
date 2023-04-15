import json


def get_content(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.readlines()

        return content


def get_cn_domain():
    domain_dict = {}
    with open("cnDomain.txt", "r", encoding="utf-8") as domain_file:
        for domain in domain_file.readlines():
            domain_str = domain.replace("\n", "")
            domain_dict[domain_str] = 1

    return domain_dict


def build_dict(file_name):
    big_dict = {}

    for line in get_content(file_name):
        line_str = line.replace("\n", "")

        if "#" in line_str:
            domain = line_str.replace("# ", "")
            tmp_var = big_dict[domain] = {}
        elif line_str:
            tmp_var[line_str] = 1

    big_dict["cn_domain"] = get_cn_domain()
    return big_dict


def dict_to_json(file_path):
    my_dict = build_dict(file_path)

    json_str = json.dumps(my_dict)

    # 将json字符串写入文件中
    with open("bypass.json", "w") as json_file:
        json_file.write(json_str)


def main():
    file_path = "test.txt"
    dict_to_json(file_path)


if __name__ == "__main__":
    main()
