from typing import List

from PySide6.QtCharts import QLineSeries, QChart, QChartView
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtGui import QPainter


class LineChart(QChartView):
    def __init__(self, name: str, x_axis: int, y_axis: (int,int), line_name: List[str]=None, line_count: int=1):
        QChartView.__init__(self)
        if line_name is None:
            line_name = ["" for i in range(line_count)]
        self.count = 0
        self.chart_range = x_axis
        self.line_count = line_count

        self.series_list = []

        for i in range(self.line_count):
            series = QLineSeries()
            series.setName(f"{line_name[i]}")
            self.series_list.append(series)

        self.line_chart = QChart()
        #self.line_chart.legend().hide()
        for series in self.series_list:
            self.line_chart.addSeries(series)

        self.line_chart.createDefaultAxes()
        self.line_chart.setTitle(name)

        self.setChart(self.line_chart)
        self.chart().setTheme(QChart.ChartTheme.ChartThemeDark)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.grab().setDevicePixelRatio(2)

        size_policy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(0, 300)
        self.line_chart.axisX().setRange(0, x_axis)
        self.line_chart.axisY().setRange(y_axis[0], y_axis[1])

    def update_chart(self, tlaskan_data: List[int]):
        try:
            for i, value in enumerate(tlaskan_data):
                self.series_list[i].append(round(self.count, 1), value)

            if self.count > self.chart_range:
                for i in range(self.line_count):
                    self.series_list[i].remove(0)
                self.line_chart.axisX().setRange(min(self.series_list[0].pointsVector(), key=lambda p: p.x()).x(),
                                                 round(self.count, 1))

            self.update()
            self.count += 1
        except Exception as e:
            print(e)
