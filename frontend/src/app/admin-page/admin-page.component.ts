import { Component } from '@angular/core';
import { MatCard, MatCardContent, MatCardHeader } from '@angular/material/card';
import { MatCalendarCellClassFunction } from '@angular/material/datepicker';
import { provideNativeDateAdapter } from '@angular/material/core';
import { StatisticsService } from '../service/statistics.service';
import { DatePipe } from '@angular/common';
import {UserService} from "../service/user.service";

@Component({
  selector: 'app-admin-page',
  templateUrl: './admin-page.component.html',
  providers: [provideNativeDateAdapter(), DatePipe],
  styleUrl: './admin-page.component.scss',
})
export class AdminPageComponent {
  // @ts-ignore
  selected: Date | null;
  percentage: number = 100;

  users:number=0;

  constructor(
    private statisticsService: StatisticsService,
    private datepipe: DatePipe,
    private userService: UserService,
  ) {
    this.selected = new Date();
    this.updatePercentage();

    this.userService.getUsers().subscribe({
      next: (response) => {
        this.users = response.length;
      },
      error: (error) => {
        console.log(error);
      },
    });

  }
  // Function to handle date selection
  onDateSelected(date: Date | null): void {
    this.selected = date;
    this.updatePercentage();
  }

  // Function to determine date class
  dateClass(date: Date): string {
    const day = date.getDay();
    return day === 0 || day === 6 ? 'weekend-date' : '';
  }

  updatePercentage() {
    let date = String(this.datepipe.transform(this.selected, 'MM/dd/yyyy'));
    this.statisticsService.getOfficeOccupancy(date).subscribe({
      next: (response) => {
        this.percentage = response;
      },
      error: (error) => {
        console.log(error);
      },
    });
  }
}
