import { Component } from '@angular/core';
import {MatCard, MatCardContent, MatCardHeader} from "@angular/material/card";
import {MatCalendarCellClassFunction} from "@angular/material/datepicker";
import {provideNativeDateAdapter} from "@angular/material/core";

@Component({
  selector: 'app-admin-page',
  templateUrl: './admin-page.component.html',
  providers: [provideNativeDateAdapter()],
  styleUrl: './admin-page.component.scss'
})
export class AdminPageComponent {
  // @ts-ignore
  selected: Date | null;

  // Function to handle date selection
  onDateSelected(date: Date | null): void {
    this.selected = date;
  }

  // Function to determine date class
  dateClass(date: Date): string {
    const day = date.getDay();
    return day === 0 || day === 6 ? 'weekend-date' : '';
  }



}
