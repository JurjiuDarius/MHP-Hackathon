import { Component, ViewEncapsulation } from '@angular/core';
import { MatCalendarCellClassFunction } from '@angular/material/datepicker';
import { provideNativeDateAdapter } from '@angular/material/core';
import { MatDialog } from '@angular/material/dialog';
import { BookDeskDialogComponent } from '../book-desk-dialog/book-desk-dialog.component';
import { Booking } from '../models/booking';
import { DatePipe } from '@angular/common';
import { BookableService } from '../service/bookable.service';

@Component({
  selector: 'app-floor-map',
  templateUrl: './floor-map.component.html',
  providers: [provideNativeDateAdapter(), DatePipe],
  styleUrls: ['./floor-map.component.scss'],
})
export class FloorMapComponent {
  selectedDate: string = new Date().toISOString().split('T')[0];
  // @ts-ignore
  booking: Booking;
  buttonIds: string[] = [
    'CLUJ_5_beta_1_1',
    'CLUJ_5_beta_1_2',
    'CLUJ_5_beta_1_3',
    'CLUJ_5_beta_1_4',
    'CLUJ_5_beta_2_1',
    'CLUJ_5_beta_2_2',
    'CLUJ_5_beta_2_3',
    'CLUJ_5_beta_2_4',
    'CLUJ_5_beta_3_1',
    'CLUJ_5_beta_3_2',
    'CLUJ_5_beta_3_3',
    'CLUJ_5_beta_3_4',
    'CLUJ_5_beta_4_1',
    'CLUJ_5_beta_4_2',
    'CLUJ_5_beta_4_3',
    'CLUJ_5_beta_4_4',
    'CLUJ_5_beta_5_1',
    'CLUJ_5_beta_5_2',
    'CLUJ_5_beta_5_3',
    'CLUJ_5_beta_5_4',
    'CLUJ_5_beta_6_1',
    'CLUJ_5_beta_6_2',
    'CLUJ_5_beta_6_3',
    'CLUJ_5_beta_6_4',
    'CLUJ_5_beta_7_1',
    'CLUJ_5_beta_7_2',
    'CLUJ_5_beta_7_3',
    'CLUJ_5_beta_7_4',
    'CLUJ_5_beta_8_1',
    'CLUJ_5_beta_8_2',
    'CLUJ_5_beta_8_3',
    'CLUJ_5_beta_8_4',
    'CLUJ_5_beta_9_1',
    'CLUJ_5_beta_9_2',
    'CLUJ_5_beta_9_3',
    'CLUJ_5_beta_9_4',
    'CLUJ_5_beta_10_1',
    'CLUJ_5_beta_10_2',
    'CLUJ_5_beta_10_3',
    'CLUJ_5_beta_10_4',
    'CLUJ_5_beta_11_1',
    'CLUJ_5_beta_11_2',
    'CLUJ_5_beta_11_3',
    'CLUJ_5_beta_11_4',
    'CLUJ_5_beta_12_1',
    'CLUJ_5_beta_12_2',
    'CLUJ_5_beta_12_3',
    'CLUJ_5_beta_12_4',
    'CLUJ_5_beta_13_1',
    'CLUJ_5_beta_13_2',
    'CLUJ_5_beta_13_3',
    'CLUJ_5_beta_13_4',
    'CLUJ_5_beta_14_1',
    'CLUJ_5_beta_14_2',
    'CLUJ_5_beta_14_3',
    'CLUJ_5_beta_14_4',
    'CLUJ_5_beta_15_1',
    'CLUJ_5_beta_15_2',
    'CLUJ_5_beta_15_3',
    'CLUJ_5_beta_15_4',
    'CLUJ_5_beta_16_1',
    'CLUJ_5_beta_16_2',
    'CLUJ_5_beta_16_3',
    'CLUJ_5_beta_16_4',
    'CLUJ_5_beta_17_1',
    'CLUJ_5_beta_17_2',
    'CLUJ_5_beta_17_3',
    'CLUJ_5_beta_17_4',
    'CLUJ_5_beta_29_1',
    'CLUJ_5_beta_29_2',
    'CLUJ_5_beta_29_3',
    'CLUJ_5_beta_29_4',
    'CLUJ_5_beta_30_1',
    'CLUJ_5_beta_30_2',
    'CLUJ_5_beta_30_3',
    'CLUJ_5_beta_30_4',
    'CLUJ_5_beta_20_1',
    'CLUJ_5_beta_20_2',
    'CLUJ_5_beta_20_3',
    'CLUJ_5_beta_20_4',
    'CLUJ_5_beta_21_1',
    'CLUJ_5_beta_21_2',
    'CLUJ_5_beta_21_3',
    'CLUJ_5_beta_21_4',
    'CLUJ_5_beta_22_1',
    'CLUJ_5_beta_22_2',
    'CLUJ_5_beta_22_3',
    'CLUJ_5_beta_22_4',
    'CLUJ_5_beta_23_1',
    'CLUJ_5_beta_23_2',
    'CLUJ_5_beta_23_3',
    'CLUJ_5_beta_23_4',
    'CLUJ_5_beta_24_1',
    'CLUJ_5_beta_24_2',
    'CLUJ_5_beta_24_3',
    'CLUJ_5_beta_24_4',
    'CLUJ_5_beta_25_1',
    'CLUJ_5_beta_25_2',
    'CLUJ_5_beta_25_3',
    'CLUJ_5_beta_25_4',
    'CLUJ_5_beta_26_1',
    'CLUJ_5_beta_26_2',
    'CLUJ_5_beta_26_3',
    'CLUJ_5_beta_26_4',
    'CLUJ_5_beta_27_1',
    'CLUJ_5_beta_27_2',
    'CLUJ_5_beta_27_3',
    'CLUJ_5_beta_27_4',
    'CLUJ_5_beta_28_1',
    'CLUJ_5_beta_28_2',
    'CLUJ_5_beta_28_3',
    'CLUJ_5_beta_28_4',
    'CLUJ_5_beta_18_1',
    'CLUJ_5_beta_18_2',
    'CLUJ_5_beta_18_3',
    'CLUJ_5_beta_18_4',
    'CLUJ_5_beta_18_5',
    'CLUJ_5_beta_19_1',
    'CLUJ_5_beta_19_2',
    'CLUJ_5_beta_19_3',
    'CLUJ_5_beta_19_4',
    'CLUJ_5_beta_19_5',
    'CLUJ_5_beta_19_6',
    'CLUJ_5_beta_31_1',
    'CLUJ_5_beta_31_2',
    'CLUJ_5_beta_31_3',
    'CLUJ_5_beta_31_4',
    'CLUJ_5_beta_32_1',
    'CLUJ_5_beta_32_2',
    'CLUJ_5_beta_32_3',
    'CLUJ_5_beta_32_4',
    'CLUJ_5_beta_33_1',
    'CLUJ_5_beta_33_2',
    'CLUJ_5_beta_33_3',
    'CLUJ_5_beta_33_4',
    'Pit-Lane',
    'Dry-Lane',
    'JockerLap',
    'Quick8',
    'PolePosition',
    'Cockpit',
  ];

  occupationDict: { [id: string]: number } = {};

  constructor(
    public dialog: MatDialog,
    private datePipe: DatePipe,
    private bookableService: BookableService
  ) {
    this.bookableService.getBookingColors(this.getFormattedDate()).subscribe({
      next: (response) => {
        console.log(response);
      },
      error: (error) => {
        console.log(error);
      },
    });
    this.buttonIds.forEach((id) => {
      this.occupationDict[id] = 0;
    });
  }

  dateClass: MatCalendarCellClassFunction<Date> = (cellDate, view) => {
    if (view === 'month') {
      const dayOfWeek = cellDate.getDay(); // 0 for Sunday, 1 for Monday, ...

      // Check if the day is Saturday (6) or Sunday (0)
      if (dayOfWeek === 0 || dayOfWeek === 6) {
        return 'weekend-date';
      }
    }
    return '';
  };

  getFormattedDate(): string {
    if (this.selectedDate) {
      return this.datePipe.transform(this.selectedDate, 'MM/dd/yyyy') || '';
    }
    return '';
  }

  currentUserId = localStorage.getItem('currentUserId') || '';

  openDialog(id: string) {
    this.selectedDate = this.getFormattedDate();
    this.booking = {
      id: 0,
      user_id: this.currentUserId,
      bookable_id: id,
      date: this.selectedDate,
      start: '',
      end: '',
    };

    this.dialog.open(BookDeskDialogComponent, {
      data: this.booking,
    });
  }

  onDateSelected(date: any): void {
    this.selectedDate = this.getFormattedDate();
    console.log(this.selectedDate);
    this.bookableService.getBookingColors(this.getFormattedDate()).subscribe({
      next: (response) => {
        for (const [key, value] of Object.entries(response)) {
          this.occupationDict[key] = value;
        }
      },
      error: (error) => {
        console.log(error);
      },
    });
  }
}
