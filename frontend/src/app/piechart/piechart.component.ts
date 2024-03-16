import { Component } from '@angular/core';
import Chart from 'chart.js/auto';
@Component({
  selector: 'app-piechart',
  //   standalone: true,
  //   imports: [],
  templateUrl: './piechart.component.html',
  styleUrl: './piechart.component.scss',
})
export class PiechartComponent {
  constructor() {}
  ngOnInit(): void {
    this.createChart();
  }
  public chart: any;

  createChart() {
    this.chart = new Chart('MyChart', {
      //       type: 'pie',
      type: 'doughnut',
      data: {
        labels: ['stat 1', 'stat 2', 'stat 3', 'stat 4', 'stat 5'],
        datasets: [
          {
            label: 'MHP Booking Stats',
            data: [9168.2, 1417.8, 3335.1, 1165.0, 2078.9],
            backgroundColor: [
              'rgb(255, 99, 132)',
              'rgb(54, 162, 235)',
              'rgb(255, 205, 86)',
              'rgb(75, 192, 192)',
              'rgb(153, 102, 255)',
            ],
            hoverOffset: 4,
          },
        ],
      },
      options: {
        aspectRatio: 2.5,
        plugins: {
          title: {
            display: true,
            text: 'MHP Booking Stats',
            font: {
              size: 24,
              weight: 'bold',
              family: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
            },
            padding: {
              top: 10,
              bottom: 30,
            },
          },
          legend: {
            display: true,
            labels: {
              font: {
                size: 14,
                family: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
              },
            },
          },
        },
      },
    });
  }
}
