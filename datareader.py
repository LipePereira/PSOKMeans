class DataReader:
    def __init__(self, file, ignore_start, ignore_end, separator):
        self.file = file
        self.ignore_start = ignore_start
        self.ignore_end = ignore_end
        self.separator = separator

    def getRealClusters(self):
        pass

    def getPoints(self):
        points = []
        classes = []

        with open(self.file) as f:
            content = f.readlines()

            first = content[0].split(self.separator)
            mini = [float(i) for i in first[0 + self.ignore_start: len(first) - self.ignore_end]]
            maxi = [float(i) for i in first[0 + self.ignore_start: len(first) - self.ignore_end]]
            dimens = len(first) - self.ignore_start - self.ignore_end

            for line in content:
                splitted = line.split(self.separator)
                point = [float(i) for i in splitted[0 + self.ignore_start: len(splitted) - self.ignore_end]]
                classes.append(splitted[len(splitted) - 1])
                points.append(point)

                mini, maxi = self.minmax(mini, maxi, point)

        return points, mini, maxi, dimens, classes

    def minmax(self, cmin, cmax, cpoint):
        mini = []
        maxi = []
        for i, j, k in zip(cmin, cmax, cpoint):
            mini.append(min(i, k))
            maxi.append(max(j, k))
        return mini, maxi