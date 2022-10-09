import matplotlib.pyplot as plt


class PloterInfo:

    def __init__(self, info: list, num_obgect: list) -> None:
        self.exclude = []
        self.info =  []
        if num_obgect:
            for i in num_obgect:
                self.info.append(info[i])
        else:
            self.info = info

    def exclude(self, exclude_list: list):
        self.exclude = exclude_list

    def show(self) -> None:
        for object_num in range(len(self.info)):
            for index, key in enumerate(self.info[object_num].keys()):
                plt.subplot(3,3,index+1)
                plt.plot(self.info[object_num][key])
                plt.title(key, x=0.1, y=0.85)
                plt.grid(True)

            plt.suptitle(f"Object: {object_num}")
            plt.show()

    def show_once(self, key: str):
        for object_num in range(len(self.info)):
            plt.subplot(len(self.info), 1, object_num+1)
            plt.plot(self.info[object_num][key])
            plt.title(object_num, x=0.1, y=0.85)
            plt.grid(True)

        plt.suptitle(f"Key: {key}")
        plt.show()