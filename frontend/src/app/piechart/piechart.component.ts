import { Component, SimpleChange, SimpleChanges } from '@angular/core';
import { Input } from '@angular/core';
import Chart from 'chart.js/auto';
@Component({
  selector: 'app-piechart',
  templateUrl: './piechart.component.html',
  styleUrl: './piechart.component.scss',
})
export class PiechartComponent {
  @Input() percentage: number = 50;
  constructor() {}
  ngOnInit(): void {
    this.createChart();
  }
  public chart: any;
  ngOnChanges(changes: SimpleChanges) {
    if (changes['percentage']) {
      this.createChart();
    }
  }
  createChart() {
    if (this.chart) {
      this.chart.destroy();
    }
    const remaining = 135 - this.percentage;

    this.chart = new Chart('MyChart', {
      type: 'doughnut',
      data: {
        labels: ['At office', 'At home'],
        datasets: [
          {
            label: 'At home',
            data: [this.percentage, remaining],
            backgroundColor: ['rgb(255, 99, 132)', 'rgb(54, 162, 235)'],
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
