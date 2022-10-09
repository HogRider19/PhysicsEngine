import matplotlib.pyplot as plt


class PloterInfo:

    def __init__(self, info: list, num_obgect: list, drawspace=False) -> None:
        self.info = []
        self.drawspace = drawspace
        if num_obgect:
            for i in num_obgect:
                self.info.append(info[i])
        else:
            self.info = info

    def show(self) -> None:
        for object_num in range(len(self.info)):
            for index, key in enumerate(self.info[object_num].keys()):
                plt.subplot(3,3,index+1)
                plt.plot(self.info[object_num][key])
                if self.drawspace:
                    l = len(self.info[object_num][key])
                    plt.fill_between(list(range(l)),self.info[object_num][key], [0]*l, color='deepskyblue')
                plt.title(key, x=0.1, y=0.85)
                plt.grid(True)

            plt.suptitle(f"Object: {object_num}")
            plt.show()

    def show_once(self, *keys: str):
        plot_counter = 1
        for object_num in range(len(self.info)):

            for imdex, key in enumerate(keys):
                
                plt.subplot(len(self.info), len(keys), plot_counter)
                plt.plot(self.info[object_num][key])
                if self.drawspace:
                    l = len(self.info[object_num][key])
                    plt.fill_between(list(range(l)),self.info[object_num][key], [0]*l, color='deepskyblue')
                plt.title(f"{object_num}:{key}", x=0.1, y=0.85)
                plt.grid(True)

                plot_counter += 1

        plt.show()